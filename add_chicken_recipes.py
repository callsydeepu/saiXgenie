# add_chicken_recipes.py
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "recipes.db"

recipes = [
    ("Simple Chicken Curry", "Sear chicken|Cook onion & garlic|Add tomatoes & spices|Simmer until cooked"),
    ("Grilled Chicken", "Marinate chicken|Grill until done|Rest and serve"),
    ("Chicken Fried Rice", "Cook rice|Stir fry chicken and veggies|Combine with rice and soy sauce"),
    ("Chicken Soup", "Sauté onion & garlic|Add chicken and water|Simmer until tender|Season"),
    ("Butter Chicken", "Marinate chicken|Cook in tomato-butter gravy|Finish with cream"),
]

ingredients = {
    0: ["chicken","onion","garlic","tomato","spices"],
    1: ["chicken","salt","pepper","olive oil","lemon"],
    2: ["chicken","rice","carrot","peas","soy sauce","egg"],
    3: ["chicken","onion","garlic","salt","pepper"],
    4: ["chicken","butter","tomato","cream","garam masala"]
}

def insert():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Insert recipes
    for idx, (name, steps) in enumerate(recipes):
        c.execute("INSERT INTO recipes (name, steps) VALUES (?, ?)", (name, steps))
        rid = c.lastrowid
        for ing in ingredients[idx]:
            c.execute("INSERT INTO ingredients (recipe_id, name) VALUES (?, ?)", (rid, ing.strip().lower()))
    conn.commit()
    # report counts
    r = c.execute("SELECT COUNT(*) FROM recipes").fetchone()[0]
    it = c.execute("SELECT COUNT(*) FROM ingredients").fetchone()[0]
    conn.close()
    print("Inserted sample chicken recipes. Total recipes:", r, "Total ingredients rows:", it)

if __name__ == "__main__":
    insert()
