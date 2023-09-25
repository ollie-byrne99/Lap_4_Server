import pytest
#from app import app
from application import db
import json



def test_api_index(api):
    res = api.get('/recipes')
    assert res == 0
    

