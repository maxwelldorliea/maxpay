#!/usr/bin/python3
"""This Module Route Every Request Receive By The Server To The Rightful View."""
from fastapi import FastAPI, Depends, Request
from models import storage
from api.v1.view import app_view

async def close_session() -> None:
    """Close current after every request."""
    print('Closing current session')
    yield
    storage.close()
    print('db session closed.')

app = FastAPI(dependencies=[Depends(close_session)])
app.include_router(app_view)
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # do things before the request
    print("Middle", "Closing session")
    response = await call_next(request)
    # do things after the response
    print("Middle", "Closed session")
    return response

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
