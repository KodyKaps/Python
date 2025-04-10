USE appdb;

CREATE TABLE IF NOT EXISTS Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20),
    image_url VARCHAR(255)
);


INSERT INTO Recipes (name, ingredients, cooking_time, difficulty, image_url)
VALUES 
('Spaghetti Bolognese', 'spaghetti, minced beef, tomato sauce, onions, garlic', 45, 'Medium', 'https://example.com/spaghetti.jpg'),
('Grilled Cheese Sandwich', 'bread, cheddar cheese, butter', 10, 'Easy', 'https://example.com/grilledcheese.jpg'),
('Chicken Curry', 'chicken, curry powder, coconut milk, onions', 40, 'Intermediate', 'https://example.com/chickencurry.jpg'),
('Pancakes', 'flour, milk, eggs, baking powder, sugar', 20, 'Easy', 'https://example.com/pancakes.jpg'),
('Beef Wellington', 'beef tenderloin, puff pastry, mushrooms, prosciutto', 90, 'Hard', 'https://example.com/beefwellington.jpg');
