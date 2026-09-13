import mysql.connector
import os
import random

# Read database settings from .env
env = {}

with open(".env", "r") as file:
    for line in file:
        line = line.strip()
        if "=" in line:
            key, value = line.split("=", 1)
            env[key] = value

db = mysql.connector.connect(
    host=env.get("DB_HOST", "localhost"),
    user=env.get("DB_USER", "root"),
    password=env.get("DB_PASSWORD", ""),
    database=env.get("DB_NAME", "business_listings")
)

cursor = db.cursor()

categories = [
    "Restaurant",
    "Cafe",
    "Hospital",
    "School",
    "IT Services",
    "Hotel",
    "Gym",
    "Salon",
    "Retail Store",
    "Coaching Centre"
]

cities = [
    "Delhi",
    "Noida",
    "Meerut",
    "Ghaziabad",
    "Muzaffarnagar",
    "Agra",
    "Mathura",
    "Bulandshahr",
    "Lucknow",
    "Jaipur"
]

sources = [
    "Google",
    "Justdial",
    "Sulekha",
    "Website"
]

query = """
INSERT INTO listing_master
(business_name, category, city, address, phone, source)
VALUES (%s, %s, %s, %s, %s, %s)
"""

data = []

for i in range(1, 501):
    category = random.choice(categories)
    city = random.choice(cities)
    source = random.choice(sources)

    data.append((
        f"{category} Business {i}",
        category,
        city,
        f"Main Road, {city}",
        f"98{random.randint(10000000, 99999999)}",
        source
    ))

cursor.executemany(query, data)
db.commit()

print(f"{len(data)} listings inserted successfully!")

cursor.close()
db.close()