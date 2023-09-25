from application import db
from application.recipes.models import Recipe
from application.comments.models import Comment

db.drop_all()
print("Dropping database")
db.create_all()
print("Creating database")

print("Seeding database")


entry1 = Recipe(
    name="Spaghetti Carbonara",
    description="A creamy pasta infused with salt, pepper and pancetta"
)

entry2 = Recipe(
    name="Spaghetti Bolognese",
    description="Beef Mince Cooked in assorted chopped vegetables"
)

db.session.add_all([entry1, entry2])
db.session.commit() 


comment1 = Comment(
    comment="This recipe is amazing!",
    recipe_id=entry1.id 
)

db.session.add(comment1)
db.session.commit()
