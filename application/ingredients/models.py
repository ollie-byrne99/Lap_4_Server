from application import db, app

app.app_context().push()

class Ingredient(db.Model):
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(500), nullable=False)


    def __repr__(self):
        return f"Recipe(id: {self.id}, name: {self.name}, description: {self.description}, season: {self.season}, image: {self.image})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "season": self.season,
            "image": self.image
        }
