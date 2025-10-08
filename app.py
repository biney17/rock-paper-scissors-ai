from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import random
import os

from RPS_game import play, random_player

app = FastAPI()

# Autoriser les requêtes du frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Modèle de données ===
class Move(BaseModel):
    player_move: str

# Conversion entre lettres et mots
def letter_to_word(letter):
    return {"R": "Rock", "P": "Paper", "S": "Scissors"}[letter]

# Déterminer le gagnant
def winner(player_move, computer_move):
    if player_move == computer_move:
        return "tie"
    elif (
        (player_move == "R" and computer_move == "S")
        or (player_move == "P" and computer_move == "R")
        or (player_move == "S" and computer_move == "P")
    ):
        return "player"
    else:
        return "computer"

# === ROUTES ===

@app.get("/")
def home():
    return {"message": "Rock Paper Scissors API is running!"}

# 🧠 Nouvelle route pour afficher la page HTML
@app.get("/play-game")
def serve_frontend():
    file_path = os.path.join(os.getcwd(), "static", "index.html")
    return FileResponse(file_path)

@app.post("/play")
def play_game(data: Move):
    player_move = data.player_move
    computer_move = random.choice(["R", "P", "S"])
    result = winner(player_move, computer_move)

    return {
        "player": letter_to_word(player_move),
        "computer": letter_to_word(computer_move),
        "result": result,
    }

# 🚀 Lancement du serveur
if __name__ == "__main__":
    import uvicorn
    print("==========================================")
    print("✅ Serveur lancé avec succès !")
    print("🌍 Accède au jeu ici : http://127.0.0.1:8000/play-game")
    print("==========================================")
    uvicorn.run(app, host="0.0.0.0", port=8000)
