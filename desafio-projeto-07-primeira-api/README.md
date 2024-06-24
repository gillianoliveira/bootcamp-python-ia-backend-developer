<h1>Desenvolvendo sua primeira API com FastAPI, Python e Docker</h1>
Instrutora: Nayanna Nara


Sumário:

- [Repositório Oficial do Lab](#repositório-oficial-do-lab)
- [💻Recursos utilizados](#recursos-utilizados)
- [Desafio final](#desafio-final)
  - [Anotações](#anotações)
    - [Criação do ambiente virtual](#criação-do-ambiente-virtual)
      - [Ambiente virtual usando virtualenv](#ambiente-virtual-usando-virtualenv)
      - [Ambiente virtual usando Pyenv](#ambiente-virtual-usando-pyenv)
  - [Instalação das dependências](#instalação-das-dependências)
  - [Testando o servidor](#testando-o-servidor)
  - [Makefile](#makefile)


# Repositório Oficial do Lab

Repo da workout_api: [https://github.com/digitalinnovationone/workout_api](https://github.com/digitalinnovationone/workout_api)

# 💻Recursos utilizados

[FastAPI](https://fastapi.tiangolo.com/)(async): framework moderno, rápido de alto desempenho, fácil de aprender, rápido de codar e pronto para produção voltado para construir APIs com Python.

[uvicorn](https://pypi.org/project/uvicorn/): Uvicorn é uma implementação de servidor web ASGI para Python. A especificação ASGI preenche essa lacuna e significa que agora podemos começar a construir um conjunto comum de ferramentas utilizáveis ​​em todas as estruturas assíncronas.Documentação: [https://www.uvicorn.org/](https://www.uvicorn.org/)

[alembic](https://pypi.org/project/alembic/): Alembic é uma ferramenta de migração de banco de dados escrita pelo autor de SQLAlchemy . Uma ferramenta de migração oferece as seguintes funcionalidades. Documentação: [https://alembic.sqlalchemy.org/en/latest/](https://alembic.sqlalchemy.org/en/latest/)

[SQLAlchemy](https://pypi.org/project/SQLAlchemy/): SQLAlchemy é o kit de ferramentas Python SQL e mapeador relacional de objetos que oferece aos desenvolvedores de aplicativos todo o poder e flexibilidade do SQL. SQLAlchemy fornece um conjunto completo de padrões de persistência de nível empresarial bem conhecidos, projetados para acesso eficiente e de alto desempenho ao banco de dados, adaptados em uma linguagem de domínio simples e Pythonica.
Documentação: [https://www.sqlalchemy.org/](https://www.sqlalchemy.org/)

[pydantic](https://pypi.org/project/pydantic/): Validação de dados usando dicas de tipo Python. Artigo de referência: [Pydantic: Simplifying Data Validation in Python](https://realpython.com/python-pydantic/)

[PostgresSQL](https://www.postgresql.org/): PostgreSQL é um poderoso sistema de banco de dados relacional de objeto de código aberto com mais de 35 anos de desenvolvimento ativo que lhe rendeu uma forte reputação de confiabilidade, robustez de recursos e desempenho.

[Docker](https://www.docker.com/): Docker é uma plataforma de software que permite criar, implantar e gerenciar aplicações em contêineres. Um contêiner é uma unidade leve, portátil e autosuficiente que inclui tudo o que a aplicação precisa para rodar: código, runtime, bibliotecas e dependências do sistema. Ele permite o isolamento da aplicação, é portável, escalável e permite a integração com sistemas CI/CD para automatizar o desenvolvimento.

Python 3.12.3 e ambiente virtual Venv.

# Desafio final

```txt
1 - adicionar query parameters nos endpoints
    - atleta
        - nome
        - cpf
2 - customizar response de retorno de endpoints
    - get all
        - atleta
            - nome
            - centro_treinamento
            - categoria
3 - Manipular exceção de integridade dos dados em cada módulo/tabela
    - sqlalchemy.exc.IntegrityError e devolver a seguinte mensagem: “Já existe um atleta cadastrado com o cpf: x”
    - status_code: 303
4 - Adicionar paginação utilizando a lib: fastapi-pagination
    - limit e offset
```

## Anotações

### Criação do ambiente virtual
A seguir você encontra duas opções para criar seu ambiente virtual usando:
* virtualenv ou
* pyenv

#### Ambiente virtual usando virtualenv

Nativo do Python a partir da versão 3.3.

Criação do ambiente virtual via CMD:

```txt
py -m venv .venv_workout
```

Ativação do ambiente virtual via CMD:

```txt
.venv_workout\Scripts\activate
```

#### Ambiente virtual usando Pyenv
É necessário instalar o [Pyenv](https://pypi.org/project/pyenv/) previamente. Depois execute no cmd o comando a seguir. Nele você pode especificar a versão do Python que será utilizada, seguido do nome do ambiente.

```txt
pyenv virtualenv 3.11.4 workoutapi
```

Para ativar o ambiente virtual criado use o comando a seguir também no cmd, onde workoutapi é o nome do ambiente criado.

```txt
pyenv activate workoutapi
```

## Instalação das dependências
Depois de ativar o ambiente virtual, execute o comando a seguir no CMD para instalar de uma só vez todos os pacotes necessários para o início da api. Pode ser que outros sejam utilizados mais adiante.

```txt
pip install fastapi uvicorn sqlalchemy pydantic
```

## Testando o servidor
Utilize o comando a seguir no CMD para subir o servidor:

```txt
uvicorn diretorio.arquivo:app
```
No nosso exemplo seria:

```txt
uvicorn workout_api.main:app
```

O CMD deve exibir uma mensagem de sucesso com o link a seguir:

```txt
http://127.0.0.1:8000
```

Você também poderá acessar a documentação através do link a seguir, mas no começo do projeto, ela estará vazia.
```txt
http://127.0.0.1:8000/docs
```

## Makefile
O arquivo Makefile não tem extensão.

Para funcionar corretamente, o arquivo Makefile precisa estar no mesmo nível da pasta do projeto. Este projeto está na pasta workout_api.

No presente projeto temos a seguinte estrutura:
```txt
📁 desafio-projeto-07-primeira-api
    📁 .venv_workout
    📁 workout_api
    ⚙️ Makefile
    📑 README.md
```
Caso o arquivo Makefile estivesse dentro da pasta workout_api, por exemplo ocorreria o erro:

```txt
make: *** No rule to make target 'run'.  Stop.
```
Exemplo de comando criado no Makefile:

```txt
run:
	@uvicorn workout_api.main:app --reload

```

Para executar o comando exemplificado acima, use a palavra make acompanhada do nome do comando. Se estiver trabalhando em um ambiente virtual, lembre-se de ativá-lo primeiro. No CMD digite:

```
make run
```

