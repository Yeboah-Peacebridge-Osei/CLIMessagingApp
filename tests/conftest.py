import pytest
from src.app import create_app
import websockets
import asyncio

@pytest.fixture
def app():
    yield create_app()



@pytest.fixture
def client(app):    
    return app.test_client()