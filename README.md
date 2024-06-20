Descri��o do Projeto: An�lise de Pipelines do Azure DevOps
T�tulo do Projeto: An�lise de Pipelines do Azure DevOps

Objetivo:
O projeto visa desenvolver uma ferramenta automatizada para analisar os arquivos de configura��o de pipelines do Azure DevOps, identificando a presen�a de tags de Git e a utiliza��o do par�metro continueOnError nos passos dos jobs. A an�lise detalhada � gerada em relat�rios JSON e CSV, proporcionando uma vis�o clara do estado dos pipelines e potenciais �reas de melhoria.

Principais Funcionalidades:

Coleta de Reposit�rios:

Conex�o com a API do Azure DevOps utilizando o token de acesso pessoal (PAT) para obter uma lista de todos os reposit�rios de um projeto espec�fico.
Recupera��o de Arquivos de Pipeline:

Extra��o do conte�do do arquivo azure-pipelines.yml de cada reposit�rio, permitindo a an�lise do pipeline de integra��o cont�nua e entrega cont�nua (CI/CD).
An�lise de Configura��o:

Verifica��o da presen�a de tags de Git e do par�metro continueOnError nos passos dos jobs dentro dos pipelines, destacando jobs e passos espec�ficos onde esses par�metros s�o encontrados.
Gera��o de Relat�rios:

Cria��o de relat�rios em formato JSON e CSV que consolidam os resultados da an�lise, incluindo logs detalhados de erros e eventos importantes durante o processo.
Registro de Logs:

Utiliza��o da biblioteca de logging para registrar mensagens e eventos, facilitando a identifica��o e resolu��o de problemas.
Benef�cios:

Automa��o: Reduz o esfor�o manual na verifica��o de pipelines, permitindo uma an�lise r�pida e consistente.
Transpar�ncia: Proporciona uma vis�o clara e detalhada das configura��es de pipelines, ajudando equipes a identificar e corrigir potenciais problemas de configura��o.
Confiabilidade: Melhora a qualidade dos pipelines ao garantir que pr�ticas recomendadas, como a presen�a de tags de Git, sejam seguidas.
Efici�ncia: Gera��o automatizada de relat�rios em m�ltiplos formatos (JSON e CSV) para facilitar a an�lise e compartilhamento de informa��es.
Tecnologias Utilizadas:

Python: Linguagem de programa��o principal utilizada para desenvolver a ferramenta.
Requests: Biblioteca para fazer requisi��es HTTP � API do Azure DevOps.
PyYAML: Biblioteca para carregar e analisar arquivos YAML.
CSV: M�dulo padr�o do Python para gerar relat�rios em formato CSV.
JSON: M�dulo padr�o do Python para gerar relat�rios em formato JSON.
Logging: Biblioteca padr�o do Python para registro de logs.
dotenv: Biblioteca para carregar vari�veis de ambiente a partir de um arquivo .env.
Requisitos:

Vari�veis de Ambiente: Configura��o de vari�veis de ambiente para o token de acesso pessoal (PAT), nome da organiza��o e nome do projeto no Azure DevOps.
Pacotes Python: Instala��o dos pacotes necess�rios (requests, PyYAML, python-dotenv) utilizando o pip.
Como Utilizar:

Configura��o: Certifique-se de que as vari�veis de ambiente AZURE_DEVOPS_PAT, AZURE_DEVOPS_ORG e AZURE_DEVOPS_PROJECT est�o corretamente definidas.
Instala��o de Depend�ncias: Instale as depend�ncias do projeto com pip install requests pyyaml python-dotenv.
Execu��o: Execute o script principal check_pipelines.py para iniciar a an�lise e gerar os relat�rios.
Conclus�o:
Este projeto oferece uma solu��o eficiente e automatizada para a an�lise de pipelines no Azure DevOps, facilitando a manuten��o de pr�ticas recomendadas e a melhoria cont�nua dos processos de CI/CD. Com a gera��o de relat�rios detalhados e o registro de logs, as equipes podem rapidamente identificar �reas de melhoria e garantir a qualidade e confiabilidade de seus pipelines.
