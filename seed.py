from application import db
from application.recipes.models import Recipe
from application.comments.models import Comment
from application.users.models import User
from application.tokens.models import Token

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


first_user = User(
    username="test_username",
    password="test_password"
)

db.session.add_all([entry1, entry2, first_user])
db.session.commit() 


comment1 = Comment(
    comment="This recipe is amazing!",
    recipe_id=entry1.id,
    user_id=first_user.id
)

first_token = Token(
    token="xxxxxxxx",
    user_id=first_user.id
)

db.session.add_all([comment1, first_token])
db.session.commit()
