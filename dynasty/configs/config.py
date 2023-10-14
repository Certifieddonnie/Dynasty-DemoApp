"""
Configuration File
"""
import os
from datetime import timedelta

from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())


SECRET_KEY = os.getenv("SECRET_KEY")

JWT_SECRET_KEY = SECRET_KEY
JWT_ACCESS_TOKEN_EXPIRES = os.getenv("ACCESS_TOKEN_EXPIRES")
JWT_TOKEN_LOCATION = ["headers", "cookies"]
JWT_COOKIE_SECURE = False
JWT_COOKIE_CSRF_PROTECT = False


sql_lite = "sqlite:///development.db"
DATABASE_URI = os.getenv("DATABASE_URL", default=sql_lite)

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Frame-Options": "deny",
    "X-Content-Type-Options": "nosniff",
    "X-RateLimit-Limit": "1000",
    "Content-Security-Policy": "default-src 'self'",
    "Access-Control-Allow-Origin": "*",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "Allow": "GET, POST, HEAD, OPTIONS",
    "Cache-Control": "no-cache",
    "Content-Encoding": "gzip",
    "Accept-Encoding": "gzip, deflate",
}
