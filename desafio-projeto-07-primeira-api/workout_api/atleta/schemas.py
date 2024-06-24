from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated


class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome do atleta', example='João', max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", example="1234567897", max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", example=25)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example="75.5")]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.70)]
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M", max_length=1)]

