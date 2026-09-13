from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="Business Listings Dashboard API")

# Frontend ko backend API access karne dena
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# MySQL connection
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "business_listings")
    )


@app.get("/")
def home():
    return {
        "message": "Business Listings Dashboard API is running"
    }


@app.get("/api/dashboard/city")
def city_wise_count():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT city, COUNT(*) AS count
        FROM listing_master
        GROUP BY city
        ORDER BY count DESC
    """)

    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data


@app.get("/api/dashboard/category")
def category_wise_count():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT category, COUNT(*) AS count
        FROM listing_master
        GROUP BY category
        ORDER BY count DESC
    """)

    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data


@app.get("/api/dashboard/source")
def source_wise_count():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT source, COUNT(*) AS count
        FROM listing_master
        GROUP BY source
        ORDER BY count DESC
    """)

    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data


@app.post("/api/listings/bulk")
def insert_listings(listings: list[dict]):
    db = get_db_connection()
    cursor = db.cursor()

    query = """
        INSERT INTO listing_master
        (business_name, category, city, address, phone, source)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = []

    for item in listings:
        values.append((
            item.get("business_name"),
            item.get("category"),
            item.get("city"),
            item.get("address"),
            item.get("phone"),
            item.get("source")
        ))

    cursor.executemany(query, values)
    db.commit()

    inserted = cursor.rowcount

    cursor.close()
    db.close()

    return {
        "message": "Listings inserted successfully",
        "inserted": inserted
    }