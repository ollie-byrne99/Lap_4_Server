from application import db, app

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)  
    
    tokens = db.relationship('Token', back_populates='user', cascade='all, delete-orphan')
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"User(id: {self.id}, username: {self.username}, email: {self.email})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
