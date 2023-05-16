def test_app_created(app):
    assert app.name == "taskList.app"

def test_request_returns_404(client):
    """ Test if non canonical URLs leads to 404"""
    assert client.get("/non_existing_url").status_code == 404

def test_request_returns_200(client):
    """ Test if canonical URLs leads to 200"""
    assert client.get("/").status_code == 200