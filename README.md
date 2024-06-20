Descrição do Projeto: Análise de Pipelines do Azure DevOps
Título do Projeto: Análise de Pipelines do Azure DevOps

Objetivo:
O projeto visa desenvolver uma ferramenta automatizada para analisar os arquivos de configuração de pipelines do Azure DevOps, identificando a presença de tags de Git e a utilização do parâmetro continueOnError nos passos dos jobs. A análise detalhada é gerada em relatórios JSON e CSV, proporcionando uma visão clara do estado dos pipelines e potenciais áreas de melhoria.

Principais Funcionalidades:

Coleta de Repositórios:

Conexão com a API do Azure DevOps utilizando o token de acesso pessoal (PAT) para obter uma lista de todos os repositórios de um projeto específico.
Recuperação de Arquivos de Pipeline:

Extração do conteúdo do arquivo azure-pipelines.yml de cada repositório, permitindo a análise do pipeline de integração contínua e entrega contínua (CI/CD).
Análise de Configuração:

Verificação da presença de tags de Git e do parâmetro continueOnError nos passos dos jobs dentro dos pipelines, destacando jobs e passos específicos onde esses parâmetros são encontrados.
Geração de Relatórios:

Criação de relatórios em formato JSON e CSV que consolidam os resultados da análise, incluindo logs detalhados de erros e eventos importantes durante o processo.
Registro de Logs:

Utilização da biblioteca de logging para registrar mensagens e eventos, facilitando a identificação e resolução de problemas.
Benefícios:

Automação: Reduz o esforço manual na verificação de pipelines, permitindo uma análise rápida e consistente.
Transparência: Proporciona uma visão clara e detalhada das configurações de pipelines, ajudando equipes a identificar e corrigir potenciais problemas de configuração.
Confiabilidade: Melhora a qualidade dos pipelines ao garantir que práticas recomendadas, como a presença de tags de Git, sejam seguidas.
Eficiência: Geração automatizada de relatórios em múltiplos formatos (JSON e CSV) para facilitar a análise e compartilhamento de informações.
Tecnologias Utilizadas:

Python: Linguagem de programação principal utilizada para desenvolver a ferramenta.
Requests: Biblioteca para fazer requisições HTTP à API do Azure DevOps.
PyYAML: Biblioteca para carregar e analisar arquivos YAML.
CSV: Módulo padrão do Python para gerar relatórios em formato CSV.
JSON: Módulo padrão do Python para gerar relatórios em formato JSON.
Logging: Biblioteca padrão do Python para registro de logs.
dotenv: Biblioteca para carregar variáveis de ambiente a partir de um arquivo .env.
Requisitos:

Variáveis de Ambiente: Configuração de variáveis de ambiente para o token de acesso pessoal (PAT), nome da organização e nome do projeto no Azure DevOps.
Pacotes Python: Instalação dos pacotes necessários (requests, PyYAML, python-dotenv) utilizando o pip.
Como Utilizar:

Configuração: Certifique-se de que as variáveis de ambiente AZURE_DEVOPS_PAT, AZURE_DEVOPS_ORG e AZURE_DEVOPS_PROJECT estão corretamente definidas.
Instalação de Dependências: Instale as dependências do projeto com pip install requests pyyaml python-dotenv.
Execução: Execute o script principal check_pipelines.py para iniciar a análise e gerar os relatórios.
Conclusão:
Este projeto oferece uma solução eficiente e automatizada para a análise de pipelines no Azure DevOps, facilitando a manutenção de práticas recomendadas e a melhoria contínua dos processos de CI/CD. Com a geração de relatórios detalhados e o registro de logs, as equipes podem rapidamente identificar áreas de melhoria e garantir a qualidade e confiabilidade de seus pipelines.
