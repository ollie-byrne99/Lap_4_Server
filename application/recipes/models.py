from application import db, app

app.app_context().push()


class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)



    def __repr__(self):
        return f"Recipe(id: {self.id}, name: {self.name}, description: {self.description})"
    

    @property
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
