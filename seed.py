from application import db
from application.recipes.models import Recipe
from application.comments.models import Comment
from application.users.models import User
from application.likes.models import Like

db.drop_all()
print("Dropping database")
db.create_all()
print("Creating database")

print("Seeding database")


predefined_user = User(
    username="predefined_user",
    email="predifined@example.com",
    password="unhashed_password"
)

db.session.add_all([predefined_user])
db.session.commit() 

entry1 = Recipe(
    name="Spaghetti Carbonara",
    description="A creamy pasta infused with salt, pepper and pancetta",
    ingredients="4 eggs, 500g spaghetti, 250g pancetta, 125g parmesan, 1tb salt, 1tb pepper",
    user_id=predefined_user.id
)

entry2 = Recipe(
    name="Spaghetti Bolognese",
    description="Beef Mince Cooked in assorted chopped vegetables",
    ingredients="500g beef mince, tomatos, onion, garlic, mushroom, pepper, spaghetti",
    user_id=predefined_user.id
)


db.session.add_all([entry1, entry2])
db.session.commit() 


comment1 = Comment(
    comment="This recipe is amazing!",
    recipe_id=entry1.id,
    user_id=predefined_user.id
)


like1 = Like(
    recipe_id=entry1.id,
    user_id=predefined_user.id
)




db.session.add_all([comment1, like1])
db.session.commit()
