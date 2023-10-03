from application import db, app

app.app_context().push()

class List(db.Model):
    __tablename__ = "lists"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='lists')
    items = db.Column(db.String(500), nullable=False)


    def __repr__(self):
        return f"List(id: {self.id}, user_id: {self.name}, items: {self.items})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "items": self.items
        }
