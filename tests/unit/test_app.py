import pytest
from src.app import create_app  
from utils.utils import get_news,get_nba
import websocket

   
def test_get_news(): 
    headlines = get_news() 
    assert isinstance(headlines, str)
    assert len(headlines) > 0

def test_get_nba():
    games = get_nba()
    assert isinstance(games,str)



# Have to run parallel server fixture nto possible
def test_handle_connection(client):
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:5000/connect")
    assert ws.connected is True
    ws.close()


