from application import db
from application.recipes.models import Recipe
from application.comments.models import Comment
from application.users.models import User
from application.likes.models import Like
from application.ingredients.models import Ingredient

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
    name="Vegetable Pasta",
    description="A light pasta dish with fresh spring vegetables.",
    ingredients="200g pasta, 100g asparagus, 100g peas, 1 lemon, 50g parmesan",
    season="Spring",
    image="https://images.immediate.co.uk/production/volatile/sites/2/2021/06/OnePotPasta-47b5b0a-a302cf0.jpg?quality=90&resize=556,505",
    user_id=predefined_user.id
)

entry2 = Recipe(
    name="Grilled Chicken Salad",
    description="A refreshing salad with grilled chicken and summer fruits.",
    ingredients="200g chicken breast, mixed salad greens, strawberries, blueberries, vinaigrette",
    season="Summer",
    image="https://assets.epicurious.com/photos/64a845e67799ee8651e4fb8f/16:9/w_6815,h_3833,c_limit/AshaGrilledChickenSalad_RECIPE_070523_56498.jpg",
    user_id=predefined_user.id
)

entry3 = Recipe(
    name="Pumpkin Soup",
    description="A warm and creamy pumpkin soup perfect for fall.",
    ingredients="1 pumpkin, 1 onion, 2 cloves of garlic, 500ml vegetable broth, salt, pepper",
    season="Autumn",
    image="https://thebigmansworld.com/wp-content/uploads/2022/10/pumpkin-curry-soup-recipe.jpg",
    user_id=predefined_user.id
)

entry4 = Recipe(
    name="Beef Stew",
    description="A hearty and warming beef stew for cold winter days.",
    ingredients="500g beef, 2 carrots, 2 potatoes, 1 onion, 500ml beef broth, salt, pepper",
    season="Winter",
    image="https://hips.hearstapps.com/hmg-prod/images/beef-stew-horizontal-1539197161.jpg?crop=1xw:0.9997999709048588xh;center,top&resize=1200:*",
    user_id=predefined_user.id
)


db.session.add_all([entry1, entry2, entry3, entry4])
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


ingredient1 = Ingredient(
    name="Fresh Strawberries",
    description="Sweet and juicy strawberries, perfect for spring desserts.",
    season="Spring",
    image="https://nearlynakedveg.co.uk/cdn/shop/files/Depositphotos_164262558_S.jpg?v=1683043057"
)

ingredient2 = Ingredient(
    name="Summer Squash",
    description="Light and versatile summer squash, great for grilling.",
    season="Summer",
    image="https://www.southernliving.com/thmb/AdniXnJJDFcao4wpXC0s2UPCy3k=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Squash_001-9c50ae26dff14572aa7cd3f8002f9e78.jpg"
)

ingredient3 = Ingredient(
    name="Pumpkin",
    description="Ripe and flavorful pumpkin, a staple for autumn recipes.",
    season="Autumn",
    image="https://images.immediate.co.uk/production/volatile/sites/30/2020/02/pumpkin-3f3d894.jpg?quality=90&resize=556,505"
)

ingredient4 = Ingredient(
    name="Winter Cabbage",
    description="Crunchy and hearty winter cabbage, ideal for soups and stews.",
    season="Winter",
    image="https://www.bejo.com/sites/bejo-drupal/files/styles/variety_teaser/public/variety/33009/GZ_004722_Winter_Cabbage_Renton.jpg?itok=ET0nMpLU"
)

ingredient5 = Ingredient(
    name="Rice",
    description="Staple grain, can be used in a variety of dishes across all seasons.",
    season="Any",
    image="https://hips.hearstapps.com/vidthumb/images/delish-u-rice-2-1529079587.jpg?crop=0.565xw:1.00xh;0.218xw,0&resize=1200:*"
)

db.session.add_all([ingredient1, ingredient2, ingredient3, ingredient4, ingredient5])
db.session.commit()
