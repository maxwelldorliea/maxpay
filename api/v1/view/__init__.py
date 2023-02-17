from fastapi import APIRouter

app_view = APIRouter(prefix='/api/v1')

from api.v1.view.index import *
from api.v1.view.user import *
