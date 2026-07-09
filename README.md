# 🤖 Basic Rule-Based Chatbot

A simple command-line chatbot built with **Python** that responds to predefined user inputs using `if-elif-else` conditional logic. A beginner-friendly project demonstrating the fundamentals of Python programming — no external libraries or APIs required.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Beginner--Friendly-brightgreen)

---

## 📌 Features

- Interactive command-line chatbot
- Exact-match responses to predefined phrases
- Continuous conversation via a `while` loop
- Friendly startup banner listing valid commands
- Graceful exit on **bye**

---

## 🛠️ Built With

- **Python 3** — no external dependencies

---

## 📚 Concepts Demonstrated

| Concept | Usage |
|---|---|
| Functions | `chatbot()` wraps the entire program |
| Conditionals | `if-elif-else` decision making |
| Loops | `while True` loop for continuous chat |
| String Methods | `.strip()`, `.lower()` for input normalization |
| I/O | Reading user input, printing bot output |

---

## 📂 Project Structure

```
Basic-Rule-Based-Chatbot/
│
├── chatbot.py       # Main chatbot script
├── README.md        # Project documentation
└── .gitignore        # Files/folders excluded from Git
```

---

## ▶️ Getting Started

### Prerequisites
- Python 3.6 or higher installed ([download here](https://www.python.org/downloads/))

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/Basic-Rule-Based-Chatbot.git

# 2. Navigate into the project folder
cd Basic-Rule-Based-Chatbot

# 3. Run the chatbot
python chatbot.py
```

---

## 💬 Example Conversation

```
========================================
      🤖 BASIC RULE-BASED CHATBOT
========================================
Type one of the following:
  • hello
  • how are you
  • what is your name
  • who created you
  • bye
----------------------------------------

You: hello
Bot: Hi! Nice to meet you. 😊

You: how are you
Bot: I'm fine, thanks for asking!

You: what is your name
Bot: My name is AlphaBot.

You: who created you
Bot: I was created using Python.

You: bye
Bot: Goodbye! Have a great day. 👋
```

---

## 🧩 Supported Commands

| You type | Bot responds |
|---|---|
| `hello` | Hi! Nice to meet you. 😊 |
| `how are you` | I'm fine, thanks for asking! |
| `what is your name` | My name is AlphaBot. |
| `who created you` | I was created using Python. |
| `bye` | Goodbye! Have a great day. 👋 *(ends the chat)* |
| anything else | Sorry, I don't understand that. |

> **Note:** Input must match a command exactly (extra words won't be recognized) — e.g. `hello` works, but `hello there` doesn't.

---

## 🎯 Learning Outcomes

Building this project covers:
- Writing and organizing Python functions
- Using loops for continuous, stateful interaction
- Handling and normalizing user input
- Implementing decision-making with `if-elif-else`
- Structuring a simple command-line application

---

## 🚀 Roadmap

- [ ] Use substring/keyword matching instead of exact matches
- [ ] Move responses to a dictionary for easier expansion
- [ ] Add more predefined responses
- [ ] Build a graphical interface with Tkinter
- [ ] Add voice input and speech output
- [ ] Integrate NLP for smarter matching
- [ ] Connect to an AI API for dynamic conversations

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/saran-2101/Basic-Rule-Based-Chatbot/issues) or submit a pull request.

---

## 👨‍💻 Author

**SARAN S**
GitHub: [@saran-2101](https://github.com/saran-2101)

