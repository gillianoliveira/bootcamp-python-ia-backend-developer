# Makefile

# Definir a variável PYTHONPATH com o caminho correto para o site-packages
PYTHONPATH := $(pwd)/Lib/site-packages


# Regra para rodar a aplicação usando uvicorn
run:
	@PYTHONPATH=$(PYTHONPATH) uvicorn workout_api.main:app --reload

# Regra para criar uma nova revisão com Alembic
create-migrations:
	@PYTHONPATH=$(PYTHONPATH) alembic revision --autogenerate -m "$(d)"

# Regra para rodar as migrações
run-migrations:
	@PYTHONPATH=$(PYTHONPATH) alembic upgrade head

