from python_flask_cnb_example import __version__
import pytest
from python_flask_cnb_example.main import App



def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture()
def app():
    app = App().create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_request_example(client):
    response = client.get("/hello")
    assert b"<p>hello, world</p>" in response.data