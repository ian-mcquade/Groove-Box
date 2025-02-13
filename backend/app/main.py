
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .database import Base, engine

# Routers we'll create soon
# from .routers import auth, parties, songs, analytics, websocket

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Configure CORS
origins = [
    "http://localhost:8080",  # Vue app default port
    # Add others if needed (e.g., 'https://myapp.com')
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the DJ Web App Backend"}

# Include routers (once created)
# app.include_router(auth.router)
# app.include_router(parties.router)
# app.include_router(songs.router)
# app.include_router(analytics.router)
# app.include_router(websocket.router)

