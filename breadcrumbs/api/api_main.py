from fastapi import FastAPI as api
from mongoengine import connect
from os import environ

# IMPORT ROUTERS HERE
# from routers import home_router

# Connect to MongoDB
host: str = f"mongodb://{environ.get('MONGODB_HOST')}/{environ.get('MONGODB_NAME')}"
try:
    connect(host=host, password=environ.get('MONGODB_PASSWORD'), username=environ.get('MONGODB_USERNAME'))
    print(f"Connected to MongoDB at {host}")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
