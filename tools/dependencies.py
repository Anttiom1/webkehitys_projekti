from os import environ
from typing import Annotated

from fastapi import Depends
from tools.symmetric_token import SymmetricToken
from tools.token_tool_base import TokenToolBase


def get_token():
    return SymmetricToken(environ.get("SECRET_KEY"))

TokenTool = Annotated[TokenToolBase, Depends(get_token)]