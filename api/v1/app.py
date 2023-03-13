#!/usr/bin/python3
"""This Module Route Every Request Receive By The Server To The Rightful View."""
from fastapi import FastAPI, Depends, Request
from models import storage
from api.v1.view import app_view
from api.v1.view.user import user_view


async def close_session():
    """Close current after every request."""
    print('Closing current session')
    yield
    storage.close()
    print('db session closed.')

app = FastAPI(dependencies=[Depends(close_session)])
app.include_router(app_view)
app.include_router(user_view)
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
