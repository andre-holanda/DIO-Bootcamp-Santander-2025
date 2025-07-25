from typing import Annotated
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(descripition='Nome do atleta', example='João', max_length=50)]
    cpf: Annotated[str, Field(descripition='CPF do atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(descripition='Idade do atleta', example='30')]
    peso: Annotated[PositiveFloat, Field(descripition='Peso do atleta', example='75.30')]
    altura: Annotated[PositiveFloat, Field(descripition='Altura do atleta', example='1.75')]
    sexo: Annotated[str, Field(descripition='Sexo do atleta', example='m', max_length=1)]
    