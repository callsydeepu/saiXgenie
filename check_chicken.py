import sqlite3

conn = sqlite3.connect("recipes.db")
c = conn.cursor()

print("\nCount of recipes with 'chicken':")
count = c.execute("""
    SELECT COUNT(DISTINCT r.id)
    FROM recipes r
    JOIN ingredients i ON r.id = i.recipe_id
    WHERE i.name LIKE '%chicken%'
""").fetchone()[0]
print(count)

print("\nSome recipe names with 'chicken':")
rows = c.execute("""
    SELECT DISTINCT r.id, r.name
    FROM recipes r
    JOIN ingredients i ON r.id = i.recipe_id
    WHERE i.name LIKE '%chicken%'
    ORDER BY r.id DESC
    LIMIT 10
""").fetchall()

for r in rows:
    print(f"{r[0]}: {r[1]}")

conn.close()
