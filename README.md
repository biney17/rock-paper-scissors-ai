 🪨✂️📄 Rock Paper Scissors – AI Bot

 🧠 Description

This project is an intelligent **Rock, Paper, Scissors** bot built using Python.
Unlike random bots, this AI learns from the opponent’s previous moves to **predict and counter their next choice**.

It was developed as part of the **FreeCodeCamp Machine Learning curriculum**, and it successfully defeats all four built-in bots (Quincy, Abbey, Kris, Mrugesh) with over **60% win rate** in each match.

 🚀 Features

* Learns opponent patterns dynamically
* Adapts strategy to maximize win rate
* Beats multiple types of opponents (predictive, repetitive, random)
* Tested using FreeCodeCamp’s official test suite

 ⚙️ Installation

 1. Clone this repository

```bash
git clone https://github.com/<your-username>/rock-paper-scissors-ai.git
cd rock-paper-scissors-ai
```

 2. Run the project

```bash
python main.py
```

 3. Run unit tests

```bash
python test_module.py
```

 📊 Example Results

| Opponent | Win Rate (%) |
| -------- | ------------ |
| Quincy   | 99.8%        |
| Abbey    | 60.3%        |
| Kris     | 87.4%        |
| Mrugesh  | 81.7%        |

✅ **All tests passed!**
This confirms the AI meets the 60% minimum win rate required by FreeCodeCamp.

 🧩 How It Works

The bot uses **pattern recognition**:

1. Stores the opponent’s past moves.
2. Searches for repeating sequences.
3. Predicts the next move based on frequency.
4. Plays the **winning counter-move**.

This method is similar to a **Markov chain model** used in AI decision systems.

 🛠️ Project Structure

```
boilerplate-rock-paper-scissors-main/
│
├── RPS.py               # Your AI logic (edit this file)
├── RPS_game.py          # Game engine (do not modify)
├── test_module.py       # FreeCodeCamp test suite
├── main.py              # Main script to run and test
└── README.md            # Project documentation
```

 💡 Future Improvements

* Add a simple **machine learning model** (e.g. logistic regression) for better predictions
* Create a **web interface** to play interactively
* Implement **reinforcement learning** for adaptive strategies

 👤 Author

**Isra Nour El Yakine Brahimi**
🎓 Master’s in Embedded Systems

🔗 [LinkedIn Profile](https://www.linkedin.com/in/isra-nour-el-yakine-b-713a38208)

