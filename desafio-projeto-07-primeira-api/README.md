<h1>Desenvolvendo sua primeira API com FastAPI, Python e Docker</h1>
Instrutora: Nayanna Nara


Sumário:

- [Repositório Oficial do Lab](#repositório-oficial-do-lab)
- [💻Recursos utilizados](#recursos-utilizados)
  - [Comandos úteis](#comandos-úteis)
- [Desafio final](#desafio-final)


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

Python 3.10.4 e ambiente virtual Venv.

## Comandos úteis

Criação do ambiente virtual
```txt
py -m venv .venv_workout
```

Ativação do ambiente virtual via cmd
```txt
.venv_workout\Scripts\activate
```

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
