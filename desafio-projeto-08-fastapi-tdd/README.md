<h1>Criando uma API com FastAPI utilizando TDD</h1>

```txt
Plataforma: dio.me
Inscrição: 13-05-2024
Término: em andamento
Carga horária: 67h
Promovido por: Vivo
```

SUMÁRIO:
- [Sobre](#sobre)
- [Desafio](#desafio)
- [TDD](#tdd)
  - [O que é?](#o-que-é)
  - [Vantagens](#vantagens)
- [Repositório Oficial do projeto](#repositório-oficial-do-projeto)
- [Anotações](#anotações)
  - [Ambiente Virtual](#ambiente-virtual)
    - [Criação do Ambiente Virtual com Pyenv e Poetry no Windows](#criação-do-ambiente-virtual-com-pyenv-e-poetry-no-windows)
    - [Comandos extras:](#comandos-extras)
    - [Poetry](#poetry)
- [Referências](#referências)


# Sobre
Repositório dedicado a solução do desafio do Lab "Criando uma API com FastAPI utilizando TDD" do Bootcamp Python AI Backend Developer promovido pela DIO em parceria com a Vivo.

# Desafio
Create
* Mapear uma exceção, caso dê algum erro de inserção e capturar na controller

Update
* Modifique o método de patch para retornar uma exceção de Not Found, quando o dado não for encontrado
* A exceção deve ser tratada na controller, pra ser retornada uma mensagem amigável pro usuário
* Ao alterar um dado, a data de updated_at deve corresponder ao time atual, permitir modificar updated_at também

Filtros
* cadastre produtos com preços diferentes
* aplique um filtro de preço, assim: (price > 5000 and price < 8000)

# TDD

## O que é?
Em andamento...
## Vantagens
Em andamento...


# Repositório Oficial do projeto

Repositório oficial: [https://github.com/digitalinnovationone/store_api?tab=readme-ov-file](https://github.com/digitalinnovationone/store_api?tab=readme-ov-file)

Instruções para a criação do ambiente virtual com poetry e pyenv.
[https://github.com/nayannanara/poetry-documentation/blob/master/poetry-documentation.md](https://github.com/nayannanara/poetry-documentation/blob/master/poetry-documentation.md)

# Anotações

## Ambiente Virtual

### Criação do Ambiente Virtual com Pyenv e Poetry no Windows

1 - Acesse o Quick Start da url a seguir: [https://github.com/pyenv-win/pyenv-win](https://github.com/pyenv-win/pyenv-win).

2 - Abra o Power Shell como Admin.

3 - Cole o comando abaixo no Power Shell:

Esse comando vai criar 3 variáveis de ambiente no seu usuário Windows, além de fazer a instalação.

```txt
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```

4 - Feche o Power Shell e abra novamente ou abra o CMD e digite o comando a seguir para ver se o pyenv foi instalado corretamente. Ele deve retornar a versão do pyenv instalada na máquina.

```txt
pyenv --version
```

5 - Instalar a versão do Python no ambiente do pyenv.

Navegue até a pasta do projeto onde o ambiente será criado e digite o comando a seguir no terminal. Os números que aparecem no comando representam a versão do Python que será instalada naquele ambiente. No meu caso será a versão 3.12.4.

Você pode repetir esse comando várias vezes com versões diferentes e cada uma delas será instalada em um ambiente diferente.

```txt
pyenv install 3.12.4
```
6 - Para verificar as versões de ambiente criadas utilize o comando:

```txt
pyenv versions
```

7 - Determinar a versão global da máquina:
```txt
pyenv global 3.12.4
```

8 - Linkar o projeto com o pyenv:

Mesmo uma uma versão global estabelecida, você precisa criar uma versão local. Naveque até a pasta do projeto pelo terminal e use o comando a seguir:

```txt
pyenv local 3.12.1
```
Feche o terminal e abra novamente.

9 - Criar o ambiente virtual na pasta do projeto:

```txt
py -m venv .venv
```

10 - Ativar o ambiente virtual na pasta do projeto:
```txt
.venv\Scripts\activate
```
11 - Sair do ambiente virtual:
```txt
deactivate
```

### Comandos extras:

Lista todas as bibliotecas instaladas no computador.
```txt
pip list
```

Lista todas as bibliotecas também:
```txt
pip freeze
```

Remove as bibliotecas já instaladas no computador:

```txt
pip freeze | grep -v "^-e" | xargs pip uninstall -y
```

Criar pasta:
```txt
mkdir nome_pasta
```

Deletar pasta vazia:
```txt
rmdir nome_da_pasta
```

Deletar pasta:
```txt
rm -r nome_da_pasta
```

### Poetry

Instalando o Poetry:
O Poetry é instalado para o usuário e deve ter a variável de ambiente adicionada ao path do Windows. Para instalar, abra o Power Shell como Admin.
```txt
pip install poetry
```

Caso a variável de ambiente do Poetry não seja adicionada automaticamente ao path, use o comando a seguir no Power Shell como Admin:

```txt
[System.Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";$env:USERPROFILE\AppData\Roaming\Python\Scripts", [System.EnvironmentVariableTarget]::User)
```

Para verificar se o poetry.exe está no diretório esperado use o comando a seguir. Ele deve retornar True.
```txt
Test-Path "$env:USERPROFILE\AppData\Roaming\Python\Scripts\poetry.exe"
```

Para verificar se o Poetry está sendo reconhecido pela como um comando no terminal, use o comando a seguir. Deve retornar a versão do Poetry instalada.
```txt
poetry --version
```

Colocando o Poetry para gerenciar o projeto:
```txt
poetry config virtualenvs.in-project true
```
O Poetry init vai fazer uma série de perguntas, como: nome do projeto, versão, se você quer instalar alguma dependência. Basta responder de acordo com a necessidade.
```txt
poetry init
```

Abrir o terminal do Poetry:
```txt
poetry shell
```

Instalar os pacotes informados no init no Poetry Shell:
```txt
poetry install
```

Criando um novo projeto com poetry:

O Poetry vai criar automaticamente o README, a pasta do projeto e a pasta de testes.
```txt
poetry new nome_projeto
```
Depois de criar a pasta do projeto não esqueça de usar o comando Pyenv local que já foi mostrado.

Informar ao Poetry a versão do Python que vai ser usada.
```txt
poetry env local 3.12.2
```

Remover uma dependência com Poetry:
```txt
poetry remove nome_dependencia
```

Lista de comandos do Poetry:
```txt
poetry config --list
```

# Referências

GAUVÃO FILHO, Luciano. Como instalar Python em 2024 + Pyenv, PIP, VENV, PIPX e Poetry. YouTube. Disponível em: https://www.youtube.com/watch?v=9LYqtLuD7z4 Acesso em: 26-06-2024

MARTINS, Daniel.Configurando um Ambiente de Desenvolvimento Python.ilegra.Disponível em: [https://ilegra.com/blog/configurando-um-ambiente-de-desenvolvimento-python/](https://ilegra.com/blog/configurando-um-ambiente-de-desenvolvimento-python/). Acessado em: 27-06-2024.

