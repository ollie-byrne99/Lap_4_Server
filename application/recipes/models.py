from application import db, app

app.app_context().push()

class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    comments = db.relationship('Comment', back_populates='recipe', cascade='all, delete-orphan')
    image = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='recipes')

    likes = db.relationship('Like', back_populates='recipe', cascade='all, delete-orphan')


    def __repr__(self):
        return f"Recipe(id: {self.id}, name: {self.name}, season: {self.season}, image: {self.image}, description: {self.description}, ingredients: {self.ingredients})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "ingredients": self.ingredients,
            "season": self.season,
            "image": self.image,
            "user_id": self.user_id
        }
