from typing import Annotated
from pydantic import Field
from fitarena_api.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Categoria do atleta', example='Scale', max_length=10)]
