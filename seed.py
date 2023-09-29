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
    instructions="",
    budget="£",
    image="https://images.immediate.co.uk/production/volatile/sites/2/2021/06/OnePotPasta-47b5b0a-a302cf0.jpg?quality=90&resize=556,505",
    user_id=predefined_user.id
)

entry2 = Recipe(
    name="Strawberry Spinach Salad",
    description="A refreshing salad featuring fresh strawberries and spinach with a balsamic vinaigrette.",
    ingredients="150g fresh spinach, 200g strawberries, 50g feta cheese, 50g pecans, balsamic vinaigrette",
    season="Spring",
    instructions="1. Wash spinach and strawberries.\n2. Slice strawberries and mix with spinach in a bowl.\n3. Crumble feta cheese and sprinkle over salad.\n4. Add pecans.\n5. Drizzle with balsamic vinaigrette and toss well.",
    budget="£",
    image="https://www.wellplated.com/wp-content/uploads/2019/04/Spinach-Strawberry-Salad.jpg",
    user_id=predefined_user.id
)

entry3 = Recipe(
    name="Spring Pea Risotto",
    description="A creamy risotto with fresh spring peas and Parmesan cheese.",
    ingredients="300g Arborio rice, 200g fresh peas, 1 onion, 750ml vegetable broth, 50g Parmesan cheese, salt, pepper",
    season="Spring",
    instructions="1. Sauté chopped onion until translucent.\n2. Add Arborio rice, cook for 2 mins.\n3. Gradually add warm broth, stirring, until absorbed.\n4. Add peas halfway through.\n5. Once rice is cooked, stir in Parmesan, salt, and pepper.",
    budget="££",
    image="https://www.curiouscuisiniere.com/wp-content/uploads/2015/04/Italian-Spring-Pea-Risotto-7993-450-450x375.jpg",
    user_id=predefined_user.id
)

entry4 = Recipe(
    name="Lemon Herb Chicken",
    description="Grilled chicken marinated in lemon and herbs, perfect for a light spring meal.",
    ingredients="2 chicken breasts, 1 lemon, mixed herbs (thyme, rosemary), salt, pepper, olive oil",
    season="Spring",
    instructions="1. Marinate chicken in lemon juice, herbs, salt, pepper, and olive oil for 30 mins.\n2. Preheat grill.\n3. Grill chicken until internal temperature reaches 165°F (74°C).\n4. Let rest for a few mins before serving.",
    budget="££",
    image="https://playswellwithbutter.com/wp-content/uploads/2021/03/Simple-Lemon-Herb-Marinade-11.jpg",
    user_id=predefined_user.id
)

entry5 = Recipe(
    name="Grilled Chicken Salad",
    description="A refreshing salad with grilled chicken and summer fruits.",
    ingredients="200g chicken breast, mixed salad greens, strawberries, blueberries, vinaigrette",
    season="Summer",
    instructions="1. Grill chicken until internal temperature is 165°F (74°C).\n2. Arrange salad greens, sliced strawberries, and blueberries on a plate.\n3. Slice grilled chicken and place on top.\n4. Drizzle with vinaigrette and serve.",
    budget="££",
    image="https://assets.epicurious.com/photos/64a845e67799ee8651e4fb8f/16:9/w_6815,h_3833,c_limit/AshaGrilledChickenSalad_RECIPE_070523_56498.jpg",
    user_id=predefined_user.id
)

entry6 = Recipe(
    name="Summer Berry Parfait",
    description="A delightful parfait with layers of summer berries, yogurt, and granola.",
    ingredients="Mixed berries (strawberries, blueberries, raspberries), 200g yogurt, 100g granola, honey",
    season="Summer",
    instructions="1. In a glass, layer yogurt, granola, and mixed berries.\n2. Drizzle honey between each layer.\n3. Repeat layers until the glass is filled.\n4. Serve chilled.",
    budget="£",
    image="https://domesticate-me.com/wp-content/uploads/2014/06/Summer-Berry-Parfaits-with-Vanilla-Bean-Ricotta-and-Toasted-Almonds-61.jpg",
    user_id=predefined_user.id
)

entry7 = Recipe(
    name="Shrimp Tacos",
    description="Tasty shrimp tacos with fresh salsa and creamy avocado, a perfect summer dish.",
    ingredients="200g shrimp, 4 small tortillas, 1 avocado, fresh salsa (tomatoes, onion, cilantro, lime), sour cream",
    season="Summer",
    instructions="1. Cook shrimp until pink and opaque.\n2. Assemble tacos with shrimp, sliced avocado, fresh salsa, and a dollop of sour cream.\n3. Serve immediately with lime wedges on the side.",
    budget="££",
    image="https://therecipecritic.com/wp-content/uploads/2022/12/shrimp_tacos-1.jpg",
    user_id=predefined_user.id
)

entry8 = Recipe(
    name="Peach Caprese Salad",
    description="A twist on the classic Caprese, featuring fresh peaches, tomatoes, mozzarella, and basil.",
    ingredients="2 peaches, 200g cherry tomatoes, 150g fresh mozzarella, fresh basil leaves, balsamic glaze",
    season="Summer",
    instructions="1. Slice peaches, tomatoes, and mozzarella.\n2. Arrange on a plate, alternating between peaches, tomatoes, and mozzarella.\n3. Drizzle with balsamic glaze and garnish with basil leaves.",
    budget="££",
    image="https://reciperunner.com/wp-content/uploads/2020/07/Peach-Tomato-Caprese-Salad-Picture.jpg",
    user_id=predefined_user.id
)

entry9 = Recipe(
    name="Pumpkin Soup",
    description="A warm and creamy pumpkin soup perfect for fall.",
    ingredients="1 pumpkin, 1 onion, 2 cloves of garlic, 500ml vegetable broth, salt, pepper",
    season="Autumn",
    instructions="1. Sauté chopped onion and garlic until soft.\n2. Add diced pumpkin and cook for 5 mins.\n3. Pour in broth, simmer until pumpkin is tender.\n4. Blend until smooth, season with salt and pepper.",
    budget="£",
    image="https://thebigmansworld.com/wp-content/uploads/2022/10/pumpkin-curry-soup-recipe.jpg",
    user_id=predefined_user.id
)

entry10 = Recipe(
    name="Apple Cider Chicken",
    description="A savory and aromatic dish featuring chicken cooked in apple cider.",
    ingredients="2 chicken breasts, 200ml apple cider, 1 apple, 1 onion, 2 sprigs rosemary, salt, pepper",
    season="Autumn",
    instructions="1. Sauté chopped onion, sliced apple, and rosemary.\n2. Add chicken breasts and brown each side.\n3. Pour in apple cider, simmer until chicken is cooked.\n4. Season with salt and pepper.",
    budget="££",
    image="https://www.fromvalerieskitchen.com/wordpress/wp-content/uploads/2021/09/Apple-Cider-Chicken-0056.jpg",
    user_id=predefined_user.id
)

entry11 = Recipe(
    name="Butternut Squash Risotto",
    description="A creamy and hearty risotto made with butternut squash and Parmesan cheese.",
    ingredients="300g Arborio rice, 500g butternut squash, 1 onion, 750ml vegetable broth, 50g Parmesan cheese, salt, pepper",
    season="Autumn",
    instructions="1. Sauté onion, add diced squash and Arborio rice.\n2. Gradually add warm broth, stirring, until absorbed.\n3. Once rice and squash are tender, stir in Parmesan, salt, and pepper.",
    budget="££",
    image="https://www.feastingathome.com/wp-content/uploads/2020/10/Instant-Pot-Butternut-Risotto_-14.jpg",
    user_id=predefined_user.id
)

entry12 = Recipe(
    name="Caramelized Onion Tart",
    description="A flavorful tart with caramelized onions and goat cheese on a flaky crust.",
    ingredients="1 pie crust, 3 large onions, 100g goat cheese, 2 tbsp olive oil, salt, pepper, thyme",
    season="Autumn",
    instructions="1. Caramelize onions in olive oil.\n2. Pre-bake pie crust until golden.\n3. Add caramelized onions, thyme, and crumbled goat cheese.\n4. Bake until cheese is melted and crust is crispy.",
    budget="££",
    image="https://sixhungryfeet.com/wp-content/uploads/2020/09/caramelised-onion-tart-with-figs-and-feta-3.jpg",
    user_id=predefined_user.id
)

entry13 = Recipe(
    name="Beef Stew",
    description="A hearty and warming beef stew for cold winter days.",
    ingredients="500g beef, 2 carrots, 2 potatoes, 1 onion, 500ml beef broth, salt, pepper",
    season="Winter",
    instructions="1. Brown beef chunks in a pot.\n2. Add chopped veggies and broth.\n3. Simmer until meat and veggies are tender.\n4. Season with salt and pepper to taste.",
    budget="££",
    image="https://hips.hearstapps.com/hmg-prod/images/beef-stew-horizontal-1539197161.jpg?crop=1xw:0.9997999709048588xh;center,top&resize=1200:*",
    user_id=predefined_user.id
)

entry14 = Recipe(
    name="Chicken and Rice Soup",
    description="A classic, comforting soup combining the heartiness of chicken and rice.",
    ingredients="1 chicken breast, 1 cup rice, 2 carrots, 1 onion, 2 celery sticks, 1.5L chicken broth, salt, pepper",
    season="Winter",
    instructions="1. Cook chicken in broth, then shred.\n2. Sauté veggies, add rice, broth, and chicken.\n3. Simmer until rice is tender.\n4. Season with salt and pepper.",
    budget="£",
    image="https://thecozycook.com/wp-content/uploads/2021/10/Chicken-and-Rice-Soup-f.jpg",
    user_id=predefined_user.id
)

entry15 = Recipe(
    name="Hearty Lentil Soup",
    description="A rich and flavorful soup that combines lentils with various vegetables for a nutritious meal.",
    ingredients="200g lentils, 2 carrots, 1 onion, 2 tomatoes, 1L vegetable broth, 2 garlic cloves, salt, pepper, 1 tsp cumin",
    season="Winter",
    instructions="1. Sauté onions, garlic, carrots, and tomatoes.\n2. Add lentils, broth, and cumin.\n3. Simmer until lentils are tender.\n4. Season with salt and pepper.",
    budget="£",
    image="https://www.noracooks.com/wp-content/uploads/2018/11/square-1.jpg",
    user_id=predefined_user.id
)

entry16 = Recipe(
    name="Baked Ziti",
    description="A delicious and filling pasta dish with layers of ziti, cheese, and marinara sauce.",
    ingredients="500g ziti pasta, 700ml marinara sauce, 250g ricotta cheese, 200g mozzarella cheese, 100g Parmesan cheese, salt, pepper",
    season="Winter",
    instructions="1. Cook ziti. Layer ziti, sauce, and cheeses in a baking dish.\n2. Repeat layers, ending with cheese.\n3. Bake until bubbly and golden.\n4. Season with salt and pepper.",
    budget="££",
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
    name="Asparagus",
    description="Tender and flavorful asparagus, a versatile vegetable for spring dishes.",
    season="Spring",
    image="https://hips.hearstapps.com/hmg-prod/images/delish-grilled-asparagus-1522951967.jpg?crop=0.668xw:1.00xh;0.167xw,0&resize=1200:*"
)

ingredient3 = Ingredient(
    name="Spring Peas",
    description="Sweet and fresh spring peas, a delightful addition to salads and pastas.",
    season="Spring",
    image="https://blog.myfitnesspal.com/wp-content/uploads/2019/04/Your-In-Season-Guide-to-Cooking-and-Eating-Spring-Peas-1200x900.jpg"
)

ingredient4 = Ingredient(
    name="Radishes",
    description="Crisp and peppery radishes, ideal for salads and garnishes.",
    season="Spring",
    image="https://www.alphafoodie.com/wp-content/uploads/2023/03/What-to-do-with-radishes-square.jpeg"
)

ingredient5 = Ingredient(
    name="Summer Squash",
    description="Light and versatile summer squash, great for grilling.",
    season="Summer",
    image="https://www.southernliving.com/thmb/AdniXnJJDFcao4wpXC0s2UPCy3k=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Squash_001-9c50ae26dff14572aa7cd3f8002f9e78.jpg"
)

ingredient6 = Ingredient(
    name="Watermelon",
    description="Juicy and refreshing watermelon, a summer staple for staying hydrated.",
    season="Summer",
    image="https://hips.hearstapps.com/hmg-prod/images/fresh-ripe-watermelon-slices-on-wooden-table-royalty-free-image-1684966820.jpg"
)

ingredient7 = Ingredient(
    name="Cherries",
    description="Sweet and tart cherries, perfect for snacking or adding to desserts.",
    season="Summer",
    image="https://images.immediate.co.uk/production/volatile/sites/30/2023/07/Cherries-02-d6ba13e.jpg?resize=768,574"
)

ingredient8 = Ingredient(
    name="Bell Peppers",
    description="Colorful and crunchy bell peppers, ideal for salads, grilling, or stuffing.",
    season="Summer",
    image="https://blog.lexmed.com/images/librariesprovider80/blog-post-featured-images/shutterstock_1901644783.jpg?sfvrsn=1986920b_0"
)

ingredient9 = Ingredient(
    name="Pumpkin",
    description="Ripe and flavorful pumpkin, a staple for autumn recipes.",
    season="Autumn",
    image="https://images.immediate.co.uk/production/volatile/sites/30/2020/02/pumpkin-3f3d894.jpg?quality=90&resize=556,505"
)

ingredient10 = Ingredient(
    name="Sweet Potatoes",
    description="Sweet and versatile sweet potatoes, great for both savory and sweet dishes.",
    season="Autumn",
    image="https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Ipomoea_batatas_006.JPG/800px-Ipomoea_batatas_006.JPG"
)

ingredient11 = Ingredient(
    name="Brussels Sprouts",
    description="Nutty and savory Brussels sprouts, a flavorful addition to autumn meals.",
    season="Autumn",
    image="https://tinandthyme.uk/wp-content/uploads/2023/01/Cooked-Brussels-Sprouts.jpg"
)

ingredient12 = Ingredient(
    name="Cranberries",
    description="Tart and vibrant cranberries, ideal for sauces, baked goods, and beverages.",
    season="Autumn",
    image="https://i0.wp.com/images-prod.healthline.com/hlcmsresource/images/AN_images/cranberries-101-1296x728-feature.jpg?w=1155&h=1528"
)

ingredient13 = Ingredient(
    name="Winter Cabbage",
    description="Crunchy and hearty winter cabbage, ideal for soups and stews.",
    season="Winter",
    image="https://www.bejo.com/sites/bejo-drupal/files/styles/variety_teaser/public/variety/33009/GZ_004722_Winter_Cabbage_Renton.jpg?itok=ET0nMpLU"
)

ingredient14 = Ingredient(
    name="Parsnips",
    description="Sweet and earthy parsnips, a versatile root vegetable for winter dishes.",
    season="Winter",
    image="https://images.immediate.co.uk/production/volatile/sites/30/2020/08/honey-roasted-parsnip-361bce8.jpg?resize=768,574"
)

ingredient15 = Ingredient(
    name="Chestnuts",
    description="Rich and nutty chestnuts, great for roasting and incorporating into sweet and savory recipes.",
    season="Winter",
    image="https://drivemehungry.com/wp-content/uploads/2022/09/roasted-chestnuts-5.jpg"
)

ingredient16 = Ingredient(
    name="Kale",
    description="Nutrient-dense and hearty kale, a healthy green for winter salads and sautés.",
    season="Winter",
    image="https://i0.wp.com/images-prod.healthline.com/hlcmsresource/images/AN_images/benefits-of-kale-1296x728-feature.jpg?w=1155&h=1528"
)

ingredient17 = Ingredient(
    name="Rice",
    description="Staple grain, can be used in a variety of dishes across all seasons.",
    season="Any",
    image="https://hips.hearstapps.com/vidthumb/images/delish-u-rice-2-1529079587.jpg?crop=0.565xw:1.00xh;0.218xw,0&resize=1200:*"
)

db.session.add_all([ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6, ingredient7, ingredient8, ingredient9, ingredient10, ingredient11, ingredient12, ingredient13, ingredient14, ingredient15, ingredient16, ingredient17])
db.session.commit()
