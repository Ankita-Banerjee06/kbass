from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chat import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://kbass.vercel.app",
        "https://kbassistant-sg45.vercel.app",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    # Also allow any Vercel preview/production URL for this project
    # (e.g. https://kbass-git-main-<user>.vercel.app), so a renamed or
    # preview deployment doesn't get silently blocked by CORS again.
    allow_origin_regex=r"https://kbass.*\.vercel\.app",
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)