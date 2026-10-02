import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

# DATABASE_URL must come from the environment (.env locally, real env vars in prod).
# Never hardcode credentials here - this file is committed to version control.
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL is not set. Copy .env.example to .env and set DATABASE_URL."
    )

# Create the database engine
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our database models
Base = declarative_base()

# Dependency injected into FastAPI routes to manage DB sessions automatically
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()