import os
import requests
import yaml
import json
import csv
from base64 import b64encode
from dotenv import load_dotenv
import logging
from typing import List, Dict, Any, Optional

# Configurações ajustáveis através de variáveis de ambiente
load_dotenv()
personal_access_token = os.getenv('AZURE_DEVOPS_PAT')
organization_name = os.getenv('AZURE_DEVOPS_ORG')
project_name = os.getenv('AZURE_DEVOPS_PROJECT')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_message(message: str):
    logging.info(message)

def get_azure_repos(pat: str, org: str, project: str) -> Optional[Dict[str, Any]]:
    auth = b64encode(f":{pat}".encode()).decode()
    headers = {
        'Authorization': f'Basic {auth}'
    }
    repos_url = f'https://dev.azure.com/{org}/{project}/_apis/git/repositories?api-version=6.0'
    try:
        response = requests.get(repos_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        log_message(f"Erro HTTP: {err}")
    except Exception as e:
        log_message(f"Erro ao obter repositórios: {e}")
    return None

def get_pipeline_file(pat: str, org: str, project: str, repo_id: str) -> Optional[str]:
    auth = b64encode(f":{pat}".encode()).decode()
    headers = {
        'Authorization': f'Basic {auth}'
    }
    file_url = f'https://dev.azure.com/{org}/{project}/_apis/git/repositories/{repo_id}/items?path=/azure-pipelines.yml&api-version=6.0'
    try:
        response = requests.get(file_url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as err:
        log_message(f"Erro HTTP: {err}")
    except requests.exceptions.RequestException as e:
        log_message(f"Erro de rede: {e}")
    return None

def analyze_pipeline(data: Dict[str, Any], repo_name: str) -> Dict[str, Any]:
    results = {
        'repository': repo_name,
        'git_tag_present': False,
        'continueOnError': []
    }

    def check_step(step: Dict[str, Any], job_name: str):
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
    if not all([personal_access_token, organization_name, project_name]):
        log_message("Erro: As variáveis de ambiente não estão todas definidas.")
        return

    all_results = []
    repos = get_azure_repos(personal_access_token, organization_name, project_name)
    if repos:
        for repo in repos.get('value', []):
            repo_id = repo['id']
            file_content = get_pipeline_file(personal_access_token, organization_name, project_name, repo_id)
            if file_content:
                try:
                    data = yaml.safe_load(file_content)
                    analysis_results = analyze_pipeline(data, repo['name'])
                    all_results.append(analysis_results)
                except yaml.YAMLError as exc:
                    log_message(f"Erro ao analisar o conteúdo do arquivo {repo['name']}: {exc}")

        # Gerando relatórios em formato JSON e CSV
        with open('pipeline_analysis_report.json', 'w') as report_file:
            json.dump({'results': all_results}, report_file, indent=4)

        with open('pipeline_analysis_report.csv', 'w', newline='') as csv_file:
            fieldnames = ['repository', 'git_tag_present', 'continueOnError']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for result in all_results:
                writer.writerow(result)

if __name__ == "__main__":
    main()
