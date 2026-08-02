import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
import psycopg2

DB_HOST = os.getenv("DB_HOST", "my-service-db")
DB_NAME = os.getenv("POSTGRES_DB", "myservice")
DB_USER = os.getenv("POSTGRES_USER", "myuser")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "mypassword")


def check_database():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]

        print("PostgreSQL bağlantısı başarılı.")
        print(f"Database: {DB_NAME}")
        print(f"PostgreSQL: {version}")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"PostgreSQL bağlantı hatası: {e}")


check_database()

server = HTTPServer(("0.0.0.0", 9090), SimpleHTTPRequestHandler)

print("Server started on port 9090")

server.serve_forever()
// webhook test
