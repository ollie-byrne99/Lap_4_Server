import pytest
from application import app, db, router
from application.recipes import controllers
from werkzeug import exceptions
import json
from dotenv import load_dotenv
load_dotenv('')
import os
from flask_jwt_extended import create_access_token  

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    #application.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DB_URL"]
    # with application.app_context():
    #     db.create_all()
    with app.test_client() as client:
        return client

    # with application.app_context():
    #     db.drop_all()

@pytest.fixture
def jwt_token(client):
    payload = {'user_id': 1}
    token = create_access_token(identity=payload)
    return token



def test_home(client):
    response = client.get("/")
    data = response.get_json()

    assert response.status_code == 200
    
    expected_data = {
        "message": "Welcome",
        "description": "Recipe API",
        "endpoints": ["GET /"]
    }

    assert data == expected_data
    
    
def test_api_index_get(client):
    res = client.get('/recipes')
    data = res.get_json()    
    assert len(data['recipes']) > 0 
   

def test_api_index_post(client, jwt_token):
    mock_data = json.dumps({
   "name" : "bob",
   "description": "juicy",
   "ingredients": "stuff",
   "user_id": 1,
   "season": "summer",
   "image": "james"
})
    mock_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {jwt_token}'
        }   

    res = client.post('/recipes', data=mock_data, headers=mock_headers)
    assert res.status_code ==201


def test_api_index_post_error(client):
    mock_data = json.dumps({
   "name" : "bob",
   "description": "juicy",
   "ingredients": "stuff",
   "user_id": 1
})
    mock_headers = {'Content-Type': 'application/json'}
    client.post('/recipes', data=mock_data, headers=mock_headers)
    assert(exceptions.InternalServerError("We cannot process your requessast."))


def test_api_get_recipe(client):
    res = client.get('/recipes/1')
    assert res.status_code == 200
    

def test_api_patch_recipe(client, jwt_token):
    mock_data = json.dumps({
   "name" : "bob",
   "description": "very juicy",
   "ingredients": "stuff",
   "user_id": 1,
   "image": "james",
   "season": "spring"
  })
    mock_headers = {'Content-Type': 'application/json',
                    'Authorization': f'Bearer {jwt_token}' }
    res = client.patch('/recipes/1', data=mock_data, headers=mock_headers)
    assert res.status_code == 200
    data = res.get_json()
    assert data['data'] == {'id': 1, 'name': 'bob', 'description': 'very juicy', 'ingredients': 'stuff', 'user_id': 1, 'image': 'james', 'season': 'spring'}


def test_api_delete_recipe(client, jwt_token ):
    mock_headers = {'Authorization': f'Bearer {jwt_token}'}
    res = client.delete('/recipes/1', headers=mock_headers)
    assert res.status_code == 204

def test_api_get_comment(client):
    res = client.get('/comments')
    assert res.status_code == 200


def test_api_post_comment(client, jwt_token):
    mock_data = json.dumps({
    "comment" : "very nice", "recipe_id" : 2, "user_id" : 1
})
    mock_headers = {'Content-Type': 'application/json',
                    'Authorization': f'Bearer {jwt_token}'}

    res = client.post('/comments', data=mock_data, headers=mock_headers)
    assert res.status_code ==201


def test_api_get_commentID(client):

    res = client.get('/comments/2')
    assert res.status_code == 200
    

def test_api_patch_commentID(client, jwt_token):
    mock_data = json.dumps({
    "comment" : "very nice", "recipe_id" : 2, "user_id" : 1
})
    mock_headers = {'Content-Type': 'application/json',
                    'Authorization': f'Bearer {jwt_token}'}

    res = client.patch('/comments/2', data=mock_data, headers=mock_headers)
    assert res.status_code ==200

def test_api_delete_commentID(client, jwt_token):
 
    mock_headers = {'Content-Type': 'application/json',
                    'Authorization': f'Bearer {jwt_token}'}

    res = client.delete('/comments/2', headers=mock_headers)
    assert res.status_code ==204


def test_api_post_register(client):
    mock_data = json.dumps({
    "username" :"bob", "email": "bob@bob", "password" : "bobo"
})
    mock_headers = {'Content-Type': 'application/json'}

    res = client.post('/register', data=mock_data, headers=mock_headers)
    assert res.status_code ==200

def test_api_post_login(client):
     mock_data = json.dumps({
    "username" :"bob", "email": "bob@bob", "password" : "bobo"
})
     mock_headers = {'Content-Type': 'application/json'}

     res = client.post('/login', data=mock_data, headers=mock_headers)
     assert res.status_code ==200

def test_api_get_users(client):
    res = client.get('/users')
    assert res.status_code == 200

def test_api_get_usersID(client):
    res = client.get('/users/1')
    assert res.status_code == 200

def test_api_patch_usersID(client):
     mock_data = json.dumps({
    "username" :"bob", "email": "bob@bob", "password" : "bobo"
})
     mock_headers = {'Content-Type': 'application/json'}

     res = client.patch('/users/1', data=mock_data, headers=mock_headers)
     assert res.status_code ==200

def test_api_delete_usersID(client):

    res = client.delete('/users/1')
    assert res.status_code ==204

def test_api_get_likes(client):

    res = client.get('/likes')
    print(res.data)
    assert res.status_code ==200






