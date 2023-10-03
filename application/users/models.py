from application import db, app

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(345), nullable=False)
    password = db.Column(db.String(200), nullable=False)  
    
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete-orphan')
    recipes = db.relationship('Recipe', back_populates='user', cascade='all, delete-orphan')
    likes = db.relationship('Like', back_populates='user', cascade='all, delete-orphan')
    lists = db.relationship('List', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"User(id: {self.id}, username: {self.username}, email: {self.email})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
