from application import db, app

app.app_context().push()

class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)
    
    comments = db.relationship('Comment', back_populates='recipe', cascade='all, delete-orphan')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='recipes')

    def __repr__(self):
        return f"Recipe(id: {self.id}, name: {self.name}, description: {self.description}, ingredients: {self.ingredients})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "ingredients": self.ingredients,
            "user_id": self.user_id
        }
