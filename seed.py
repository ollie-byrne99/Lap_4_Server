from application import db
# from application.users.models import User
# from application.tokens.models import Token
from application.recipes.models import Recipe

db.drop_all()
print("Dropping database")
db.create_all()
print("Creating database")

print("Seeding database")


entry1= Recipe(
    name="Spaghetti Carbonara",
    description="A creamy pasta infused with salt, pepper and pancetta"
)

entry2= Recipe(
    name="Spaghetti Bolognese",
    description="Beef Mince Cooked in assorted chopes vehe"
)


db.session.add_all([entry1, entry2])



db.session.commit()
