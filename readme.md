# IS601 Assignment 5 - Enhanced Calculator

A command-line calculator application built with Python, featuring a REPL interface, design patterns, and pandas-based history management.

---

## 📋 Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [CI/CD](#cicd)

---

## 📁 Project Structure

```
Assigment5/
├── app/
│   ├── __init__.py
│   ├── calculation.py
│   ├── calculator.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── calculator_repl.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   └── operations.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_calculation.py
│   ├── test_calculator.py
│   ├── test_config.py
│   ├── test_exceptions.py
│   ├── test_history.py
│   ├── test_operations.py
│   └── test_validators.py
├── .github/
│   └── workflows/
│       └── test.yml
├── .env
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

---

## ✨ Features

- **REPL Interface** — Continuous user interaction loop
- **Arithmetic Operations** — Addition, subtraction, multiplication, division, power, and root
- **Design Patterns:**
  - Observer Pattern — Logs and auto-saves calculation events
  - Memento Pattern — Undo and redo functionality
  - Strategy Pattern — Interchangeable operation strategies
  - Factory Pattern — Instantiates operations based on user input
  - Facade Pattern — Simplified interface to the calculator subsystem
- **History Management** — Stores calculation history using pandas DataFrames
- **Auto-Save & Load** — Saves history to CSV and loads on startup
- **Configuration** — Manages settings via `.env` file and `python-dotenv`
- **Commands:** `help`, `history`, `undo`, `redo`, `save`, `load`, `clear`, `exit`
- **Error Handling** — Handles invalid inputs, division by zero, and more using both LBYL and EAFP paradigms

---

## 🛠️ Setup Instructions

### 1. Install Homebrew (Mac Only)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew --version
```

### 2. Install Git

**Mac:**

```bash
brew install git
```

**Windows:** Download from [git-scm.com](https://git-scm.com/download/win)

Configure Git:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

### 3. Set Up SSH Key for GitHub

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub | pbcopy   # Mac
```

Then go to [GitHub SSH Settings](https://github.com/settings/keys) → **New SSH Key** → paste and save.

Test connection:

```bash
ssh -T git@github.com
```

### 4. Clone the Repository

```bash
git clone git@github.com:Thisaintkrupaa/IS601_Assignment5.git
cd IS601_Assignment5
```

### 5. Install Python 3.10+

**Mac:**

```bash
brew install python
python3 --version
```

**Windows:** Download from [python.org](https://www.python.org/downloads/) — check **Add Python to PATH**.

### 6. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate.bat       # Windows
```

### 7. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Application

```bash
python main.py
```

### Available Commands

| Command   | Description                      |
| --------- | -------------------------------- |
| `help`    | Show available commands          |
| `history` | Display calculation history      |
| `undo`    | Undo the last calculation        |
| `redo`    | Redo the last undone calculation |
| `save`    | Save history to CSV              |
| `load`    | Load history from CSV            |
| `clear`   | Clear calculation history        |
| `exit`    | Exit the application             |

---

## 🧪 Running Tests

```bash
pytest --cov=app tests/
```

To check coverage report:

```bash
coverage report --fail-under=100
```

---

## ⚙️ CI/CD

This project uses **GitHub Actions** to automatically run tests on every push or pull request to `main`.

The pipeline will:

- Install all dependencies
- Run all tests with `pytest`
- Enforce **100% test coverage** — build fails if coverage drops below 100%

Workflow file: `.github/workflows/test.yml`

---

## 📝 Submission

```bash
git add .
git commit -m "Complete Assignment 5"
git push origin main
```

Then submit your GitHub repository link as instructed.

---

## 🔥 Quick Commands Cheat Sheet

| Action                       | Command                                        |
| ---------------------------- | ---------------------------------------------- |
| Activate virtual environment | `source venv/bin/activate`                     |
| Install packages             | `pip install -r requirements.txt`              |
| Run application              | `python main.py`                               |
| Run tests                    | `pytest --cov=app tests/`                      |
| Push to GitHub               | `git add . && git commit -m "msg" && git push` |
