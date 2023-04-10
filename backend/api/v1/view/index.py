from api.v1.view import app_view
"""This Module Give The API Serve Status."""

@app_view.get('/status')
def server_status():
    """Return the status of the api server."""
    return {'status': 'OK'}
