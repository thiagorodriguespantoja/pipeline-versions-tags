from dotenv import load_dotenv
load_dotenv()

import os
import requests
import yaml
import json
import csv

# Configurações ajustáveis através de variáveis de ambiente
personal_access_token = os.getenv('AZURE_DEVOPS_PAT')
organization_name = os.getenv('AZURE_DEVOPS_ORG')
project_name = os.getenv('AZURE_DEVOPS_PROJECT')

def log_message(messages, message):
    print(message)
    messages.append(message)

def get_azure_repos(pat, org, project, messages):
    headers = {
        'Authorization': f'Basic {pat}'
    }
    repos_url = f'https://dev.azure.com/easynextti/JDK/_apis/git/repositories?api-version=6.0'
    try:
        response = requests.get(repos_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        log_message(messages, f"Erro HTTP: {err}")
    except Exception as e:
        log_message(messages, f"Erro ao obter repositórios: {e}")

def get_pipeline_file(pat, org, project, repo_id, messages):
    headers = {
        'Authorization': f'Basic {pat}'
    }
    file_url = f'https://dev.azure.com/{org}/{project}/_apis/git/repositories/{repo_id}/items?path=/azure-pipelines.yml&api-version=6.0'
    try:
        response = requests.get(file_url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            log_message(messages, f"azure-pipelines.yml não encontrado em {repo_id}")
            return None
    except requests.exceptions.RequestException as e:
        log_message(messages, f"Erro de rede: {e}")
        return None

def analyze_pipeline(data, repo_name, messages):
    results = {
        'repository': repo_name,
        'git_tag_present': False,
        'continueOnError': []
    }

    def check_step(step, job_name):
        if step.get('displayName') == 'Git Tag':
            results['git_tag_present'] = True
        if 'continueOnError' in step:
            results['continueOnError'].append({
                'job': job_name,
                'step': step.get('displayName', '<sem nome>'),
                'status': step['continueOnError']
            })

    for job in data.get('jobs', []):
        for step in job.get('steps', []):
            check_step(step, job.get('job', '<sem nome>'))

    return results

def main():
    messages = []
    if not all([personal_access_token, organization_name, project_name]):
        log_message(messages, "Erro: As variáveis de ambiente não estão todas definidas.")
        return

    all_results = []
    repos = get_azure_repos(personal_access_token, organization_name, project_name, messages)
    if repos:
        for repo in repos.get('value', []):
            repo_id = repo['id']
            file_content = get_pipeline_file(personal_access_token, organization_name, project_name, repo_id, messages)
            if file_content:
                try:
                    data = yaml.safe_load(file_content)
                    analysis_results = analyze_pipeline(data, repo['name'], messages)
                    all_results.append(analysis_results)
                except yaml.YAMLError as exc:
                    log_message(messages, f"Erro ao analisar o conteúdo do arquivo {repo['name']}: {exc}")
    
        # Gerando relatórios em formato JSON e CSV
        with open('pipeline_analysis_report.json', 'w') as report_file:
            json.dump({'results': all_results, 'logs': messages}, report_file, indent=4)
        
        with open('pipeline_analysis_report.csv', 'w', newline='') as csv_file:
            fieldnames = ['repository', 'git_tag_present', 'continueOnError']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for result in all_results:
                writer.writerow(result)

        # Salvando logs em um arquivo separado
        with open('pipeline_analysis_logs.txt', 'w') as log_file:
            for message in messages:
                log_file.write(message + '\n')

if __name__ == "__main__":
    main()
