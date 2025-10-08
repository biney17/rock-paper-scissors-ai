import random
from collections import defaultdict

N = 5
DECAY = 0.9

moves = ["R", "P", "S"]
beats = {"R": "P", "P": "S", "S": "R"}

patterns = defaultdict(lambda: {"R": 0, "P": 0, "S": 0})
opponent_history = []

def player(prev_play, opponent_history=[]):
    import random

    # Enregistrer l'historique de l'adversaire
    if prev_play:
        opponent_history.append(prev_play)

    # Si on n'a pas encore assez de données, jouer aléatoirement
    if len(opponent_history) < 3:
        return random.choice(["R", "P", "S"])

    # Construire un dictionnaire des séquences de 3 coups
    last_three = "".join(opponent_history[-3:])
    patterns = {}

    for i in range(len(opponent_history) - 3):
        seq = "".join(opponent_history[i:i+3])
        next_move = opponent_history[i + 3]
        if seq not in patterns:
            patterns[seq] = {"R": 0, "P": 0, "S": 0}
        patterns[seq][next_move] += 1

    # Prédire le prochain coup d'après les 3 derniers
    prediction = random.choice(["R", "P", "S"])
    if last_three in patterns:
        prediction = max(patterns[last_three], key=patterns[last_three].get)

    # Jouer pour battre ce coup
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[prediction]
