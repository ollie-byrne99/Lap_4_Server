from application import db, app

app.app_context().push()

class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(500), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    recipe = db.relationship('Recipe', back_populates='comments')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='comments')

    def __repr__(self):
        return f"Comment(id: {self.id}, comment: {self.comment})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "comment": self.comment,
            "recipe_id": self.recipe_id,
            "user_id": self.user_id
        }
