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
    name="Strawberry Spinach Salad",
    description="A refreshing salad featuring fresh strawberries and spinach with a balsamic vinaigrette.",
    ingredients="150g fresh spinach, 200g strawberries, 50g feta cheese, 50g pecans, balsamic vinaigrette",
    season="Spring",
    image="https://www.wellplated.com/wp-content/uploads/2019/04/Spinach-Strawberry-Salad.jpg",
    user_id=predefined_user.id
)

entry3 = Recipe(
    name="Spring Pea Risotto",
    description="A creamy risotto with fresh spring peas and Parmesan cheese.",
    ingredients="300g Arborio rice, 200g fresh peas, 1 onion, 750ml vegetable broth, 50g Parmesan cheese, salt, pepper",
    season="Spring",
    image="https://www.curiouscuisiniere.com/wp-content/uploads/2015/04/Italian-Spring-Pea-Risotto-7993-450-450x375.jpg",
    user_id=predefined_user.id
)

entry4 = Recipe(
    name="Lemon Herb Chicken",
    description="Grilled chicken marinated in lemon and herbs, perfect for a light spring meal.",
    ingredients="2 chicken breasts, 1 lemon, mixed herbs (thyme, rosemary), salt, pepper, olive oil",
    season="Spring",
    image="https://playswellwithbutter.com/wp-content/uploads/2021/03/Simple-Lemon-Herb-Marinade-11.jpg",
    user_id=predefined_user.id
)

entry5 = Recipe(
    name="Grilled Chicken Salad",
    description="A refreshing salad with grilled chicken and summer fruits.",
    ingredients="200g chicken breast, mixed salad greens, strawberries, blueberries, vinaigrette",
    season="Summer",
    image="https://assets.epicurious.com/photos/64a845e67799ee8651e4fb8f/16:9/w_6815,h_3833,c_limit/AshaGrilledChickenSalad_RECIPE_070523_56498.jpg",
    user_id=predefined_user.id
)

entry6 = Recipe(
    name="Summer Berry Parfait",
    description="A delightful parfait with layers of summer berries, yogurt, and granola.",
    ingredients="Mixed berries (strawberries, blueberries, raspberries), 200g yogurt, 100g granola, honey",
    season="Summer",
    image="https://domesticate-me.com/wp-content/uploads/2014/06/Summer-Berry-Parfaits-with-Vanilla-Bean-Ricotta-and-Toasted-Almonds-61.jpg",
    user_id=predefined_user.id
)

entry7 = Recipe(
    name="Shrimp Tacos",
    description="Tasty shrimp tacos with fresh salsa and creamy avocado, a perfect summer dish.",
    ingredients="200g shrimp, 4 small tortillas, 1 avocado, fresh salsa (tomatoes, onion, cilantro, lime), sour cream",
    season="Summer",
    image="https://therecipecritic.com/wp-content/uploads/2022/12/shrimp_tacos-1.jpg",
    user_id=predefined_user.id
)

entry8 = Recipe(
    name="Peach Caprese Salad",
    description="A twist on the classic Caprese, featuring fresh peaches, tomatoes, mozzarella, and basil.",
    ingredients="2 peaches, 200g cherry tomatoes, 150g fresh mozzarella, fresh basil leaves, balsamic glaze",
    season="Summer",
    image="https://reciperunner.com/wp-content/uploads/2020/07/Peach-Tomato-Caprese-Salad-Picture.jpg",
    user_id=predefined_user.id
)

entry9 = Recipe(
    name="Pumpkin Soup",
    description="A warm and creamy pumpkin soup perfect for fall.",
    ingredients="1 pumpkin, 1 onion, 2 cloves of garlic, 500ml vegetable broth, salt, pepper",
    season="Autumn",
    image="https://thebigmansworld.com/wp-content/uploads/2022/10/pumpkin-curry-soup-recipe.jpg",
    user_id=predefined_user.id
)

entry10 = Recipe(
    name="Apple Cider Chicken",
    description="A savory and aromatic dish featuring chicken cooked in apple cider.",
    ingredients="2 chicken breasts, 200ml apple cider, 1 apple, 1 onion, 2 sprigs rosemary, salt, pepper",
    season="Autumn",
    image="https://www.fromvalerieskitchen.com/wordpress/wp-content/uploads/2021/09/Apple-Cider-Chicken-0056.jpg",
    user_id=predefined_user.id
)

entry11 = Recipe(
    name="Butternut Squash Risotto",
    description="A creamy and hearty risotto made with butternut squash and Parmesan cheese.",
    ingredients="300g Arborio rice, 500g butternut squash, 1 onion, 750ml vegetable broth, 50g Parmesan cheese, salt, pepper",
    season="Autumn",
    image="https://www.feastingathome.com/wp-content/uploads/2020/10/Instant-Pot-Butternut-Risotto_-14.jpg",
    user_id=predefined_user.id
)

entry12 = Recipe(
    name="Caramelized Onion Tart",
    description="A flavorful tart with caramelized onions and goat cheese on a flaky crust.",
    ingredients="1 pie crust, 3 large onions, 100g goat cheese, 2 tbsp olive oil, salt, pepper, thyme",
    season="Autumn",
    image="https://sixhungryfeet.com/wp-content/uploads/2020/09/caramelised-onion-tart-with-figs-and-feta-3.jpg",
    user_id=predefined_user.id
)

entry13 = Recipe(
    name="Beef Stew",
    description="A hearty and warming beef stew for cold winter days.",
    ingredients="500g beef, 2 carrots, 2 potatoes, 1 onion, 500ml beef broth, salt, pepper",
    season="Winter",
    image="https://hips.hearstapps.com/hmg-prod/images/beef-stew-horizontal-1539197161.jpg?crop=1xw:0.9997999709048588xh;center,top&resize=1200:*",
    user_id=predefined_user.id
)

entry14 = Recipe(
    name="Chicken and Rice Soup",
    description="A classic, comforting soup combining the heartiness of chicken and rice.",
    ingredients="1 chicken breast, 1 cup rice, 2 carrots, 1 onion, 2 celery sticks, 1.5L chicken broth, salt, pepper",
    season="Winter",
    image="https://thecozycook.com/wp-content/uploads/2021/10/Chicken-and-Rice-Soup-f.jpg",
    user_id=predefined_user.id
)

entry15 = Recipe(
    name="Hearty Lentil Soup",
    description="A rich and flavorful soup that combines lentils with various vegetables for a nutritious meal.",
    ingredients="200g lentils, 2 carrots, 1 onion, 2 tomatoes, 1L vegetable broth, 2 garlic cloves, salt, pepper, 1 tsp cumin",
    season="Winter",
    image="https://www.noracooks.com/wp-content/uploads/2018/11/square-1.jpg",
    user_id=predefined_user.id
)

entry16 = Recipe(
    name="Baked Ziti",
    description="A delicious and filling pasta dish with layers of ziti, cheese, and marinara sauce.",
    ingredients="500g ziti pasta, 700ml marinara sauce, 250g ricotta cheese, 200g mozzarella cheese, 100g Parmesan cheese, salt, pepper",
    season="Winter",
    image="https://www.allrecipes.com/thmb/uJocCYfLL1gMCsbj79tY7hKilWw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/4557541-21604073f2774e89b532193821d6cd9c.jpg",
    user_id=predefined_user.id
)

db.session.add_all([entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, entry12, entry13, entry14, entry15, entry16])
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
