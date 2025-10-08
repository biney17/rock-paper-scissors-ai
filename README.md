# 🪨✂️📄 Rock Paper Scissors – AI Bot

 🧠 Description

Ce projet est un bot intelligent de **Pierre-Papier-Ciseaux** développé en Python.
Contrairement aux bots aléatoires, ce bot **apprend des coups précédents de l’adversaire** pour prédire et contrer son prochain choix.

Il a été développé dans le cadre du programme **FreeCodeCamp Machine Learning**, et réussit à battre les quatre bots intégrés (Quincy, Abbey, Kris, Mrugesh) avec un taux de victoire supérieur à **60%** dans chaque match.

Grâce à la **nouvelle interface web améliorée**, tu peux désormais **jouer directement contre l’IA** depuis ton navigateur.


🚀 Fonctionnalités

* Apprentissage dynamique des motifs de l’adversaire
* Adaptation de la stratégie pour maximiser le taux de victoire
* Bat plusieurs types d’adversaires (prédictifs, répétitifs, aléatoires)
* **Interface web interactive** pour jouer en direct
* Testé avec la suite de tests officielle de FreeCodeCamp


 🖥️ Interface Web

* Choix de **Pierre, Papier ou Ciseaux** via boutons
* Affichage du score et des résultats en temps réel
* Design réactif pour mobile et desktop
* Basé sur HTML/CSS/Flask dans `static/index.html` et `app.py`


 📦 Installation

1. **Cloner le dépôt**

```bash
git clone https://github.com/biney17/rock-paper-scissors-ai.git
cd rock-paper-scissors-ai
```

2. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

3. **Lancer l’application web**

```bash
python app.py
```

4. **Ouvrir le navigateur** sur (http://127.0.0.1:8000/play-game)

5. **Exécuter les tests unitaires** (facultatif)

```bash
python test_module.py
```


 📊 Résultats Exemple

| Adversaire | Taux de Victoire (%) |
| ---------- | -------------------- |
| Quincy     | 99.8%                |
| Abbey      | 60.3%                |
| Kris       | 87.4%                |
| Mrugesh    | 81.7%                |

✅ **Tous les tests ont été réussis !**


 🧩 Comment ça marche

Le bot utilise la **reconnaissance de motifs** :

1. Stocke les coups précédents de l’adversaire
2. Recherche des séquences répétitives
3. Prédit le prochain coup basé sur la fréquence
4. Joue le **contre-coup gagnant**

Cette méthode est similaire à un **modèle de chaîne de Markov** utilisé dans les systèmes de décision IA.


 🛠️ Structure du Projet

```
boilerplate-rock-paper-scissors-main/
│
├── RPS.py               # Logique de l'IA
├── RPS_game.py          # Moteur de jeu
├── test_module.py       # Suite de tests FreeCodeCamp
├── main.py              # Script principal pour exécuter et tester
├── app.py               # Application Flask pour l'interface web
├── static/
│   └── index.html       # Page d'accueil de l'interface web
└── README.md            # Documentation du projet
```

 💡 Améliorations Futures

* Ajouter un **modèle ML plus avancé** pour des prédictions encore plus fiables
* Ajouter des **animations et graphiques de score** dans l’interface web
* Implémenter **l’apprentissage par renforcement** pour des stratégies adaptatives


 👤 Auteur

**Isra Nour El Yakine Brahimi**
🎓 Master en Systèmes Embarqués

🔗 [LinkedIn](https://www.linkedin.com/in/isra-nour-el-yakine-b-713a38208)


Veux‑tu que je fasse ça ?
