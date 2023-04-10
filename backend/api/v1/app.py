#!/usr/bin/python3
"""This Module Route Every Request Receive By The Server To The Rightful View."""
from fastapi import FastAPI, Depends, Request
from models import storage
from api.v1.view import app_view
from api.v1.view.user import user_view


app = FastAPI()


@app.middleware('http')
async def close_session(request: Request, call_next):
    try:
        response = await call_next(request);
    except Exception as err:
        response = {'error': str(err)}
        raise
    finally:
        storage.close()
    return response


app.include_router(app_view)
app.include_router(user_view)
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
