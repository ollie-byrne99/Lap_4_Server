import pytest
from application import app as application, db
from application import router

@pytest.fixture
def app():
    application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qsvzyace:gqPw0yrmK9WaDzeC9EJaBCy5K1z2_-GV@tai.db.elephantsql.com/qsvzyace'
    application.config['TESTING'] = True
    with application.app_context():
        # db.create_all()
        print("Seeding database")
        yield application
       # db.drop_all()


@pytest.fixture
def client(app): 
    return app.test_client()

def test_api_index(client):
    res = client.get('/recipes')
    data = res.get_json()
    print(data)
   

def test_home(client):
    response = client.get("/")
    data = response.get_json()
    
    assert response.status_code == 200
    
    expected_data = {
        "message": "Welcome",
        "description": "Recipes API",
        "endpoints": ["GET /"]
    }

    
    

