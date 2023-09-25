from application import db, app

app.app_context().push()

class Token(db.Model):
    __tablename__ = "tokens"

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(36), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='tokens')

    def __repr__(self):
        return f"Token(id: {self.id}, token: {self.token}, user_id: {self.user_id})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "token": self.token,
            "user_id": self.user_id
        }
