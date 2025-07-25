from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    nome: Annotated[str, Field(descripition='Nome da categoria', example='Scale', max_length=10)]