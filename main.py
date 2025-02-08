from fastapi import FastAPI
import models
from database import engine
from routes import auth,tasks    # Import the new router

# Run database migrations
models.Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI()

# Include authentication routes
app.include_router(auth.router)
app.include_router(tasks.router)
