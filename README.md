# Tic-Tac-Toe Coding Challenge

This is your first coding challenge: write a simple command-line Tic-Tac-Toe
game in Python that two players can play against each other. Along the way you
will practice planning a program before you write it, using program-design tools
and splitting your code into small, focused functions. The repository gives you
the assignment, a few supporting lessons, and a starter script to build on.

## Learning Objectives

By the end of this repository, you should be able to:

- Break a programming problem into small, well-named functions before writing
  code.
- Apply program-design tools (flowcharts, requirements, skeleton code) to plan a
  solution.
- Write pseudocode to outline an algorithm before you implement it.
- Build a working command-line Tic-Tac-Toe game in Python (board display, player
  turns, win and draw detection).
- Explain what `if __name__ == "__main__"` does and use it as a script entry
  point.
- Read Python error messages and stack traces to debug your own code.

## Learning Path

| File / Folder                                                | Description                                                                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| [**01 - Assignment**](01_assignment.md)                   | The coding challenge: build a command-line Tic-Tac-Toe game, with step-by-step suggestions.                  |
| [**02 - Program Design**](02_program_design.md)           | Design tools (flowcharts, requirements, pseudocode, skeleton code) for planning a program before you code.   |
| [**03 - Intro to Pseudocode**](03_intro_to_pseudocode.md) | A short primer on writing pseudocode to outline an algorithm.                                                |
| [**Tic Tac Toe**](tic_tac_toe.py)                         | Starter script where you write your game; it already includes the `if __name__ == "__main__"` entry point. |

### Additional Folders and Files

| File / Folder                           | Description                                                                                                      |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [**Examples**](examples/)            | Two small scripts showing how `if __name__ == "__main__"` behaves when a file is run directly versus imported. |
| [**Solutions**](solutions/)          | Reference solution.|
| [**Assets**](assets/)               | Images used in the lessons.|
| [**pyproject.toml**](pyproject.toml) | Project configuration and dependencies.|
| [**uv.lock**](uv.lock)               | Pinned dependency lock file.                                                                                     |

## Setup

> [!NOTE]
> Throughout these steps, text in angle brackets like `<repo-name>` is a
> **placeholder**. Replace it, including the `< >` brackets, with your own
> value. For example, `cd <repo-name>` becomes `cd tic-tac-toe`.

### 1. Create the Repository from the Template

Click **Use this template** on GitHub.

When creating the repository:

- Set yourself as the **Owner**
- Choose a repository name
- Enable **Include all branches**
- Click **Create repository**

> [!IMPORTANT]
> If you are working in pairs or groups, only **one person** should complete
> this step.

---

### 2. Add Collaborators (Pairs/Groups Only)

If working with teammates:

1. Open the repository on GitHub
2. Go to **Settings → Collaborators**
3. Add your teammates as collaborators
4. Share the repository link with your team

Teammates should accept the invitation before continuing.

---

### 3. Clone the Repository

Copy the SSH URL from the **Code** button on GitHub, then run:

```bash
git clone <copied-ssh-url>
```

The copied SSH URL will look like
`git@github.com:<your-username>/<repo-name>.git`.

---

### 4. Move into the Project Folder and Install Dependencies

This installs all dependencies and creates a virtual environment in `.venv/`,
including the Jupyter kernel (`ipykernel`).

```bash
cd <repo-name>
uv sync
```

---

### 5. Open the Project in VS Code

> [!NOTE]
> Make sure you open VS Code from the project root so it automatically detects
> the environment created by `uv sync`.

Launch VS Code from the terminal:

```bash
code .
```

If you want to work interactively, create a notebook (for example `scratch.ipynb`) and
select the Python environment created by `uv sync` as the kernel.

> [!TIP]
> Prototype and test small pieces of your game in notebook cells, then move the working code into [**tic_tac_toe.py**](tic_tac_toe.py).

## Usage

Work through the material in order, and plan before you code.

1. Read [**01 - Assignment**](01_assignment.md) to understand what the game
   should do.
2. Review [**02 - Program Design**](02_program_design.md) and
   [**03 - Intro to Pseudocode**](03_intro_to_pseudocode.md) for planning techniques.
3. Sketch your solution using a flowchart or pseudocode.
4. Implement and test small functions, then move working code into
   [**tic_tac_toe.py**](tic_tac_toe.py).
5. Connect your functions inside the `if __name__ == "__main__"` block.
6. Run the finished game:

   ```bash
   uv run python tic_tac_toe.py
   ```

### Coding practices to keep in mind

- Give your functions explicit, descriptive names.
- Write a docstring for each function explaining how to call it.
- Keep functions short, roughly 4 to 10 lines each.

## References & Further Reading

- [**Tic-Tac-Toe**](https://en.wikipedia.org/wiki/Tic-tac-toe):
  Rules and background of the game you are building.
- [**Python control flow and functions**](https://docs.python.org/3/tutorial/controlflow.html):
  Official tutorial on loops, conditionals, and defining functions.
- [**Python `__main__` documentation**](https://docs.python.org/3/library/__main__.html):
  Official reference for the `if __name__ == "__main__"` entry point.
- [**Real Python: What does `if __name__ == "__main__"` do?**](https://realpython.com/if-name-main-python/):
  A beginner-friendly walkthrough of the script entry-point idiom.
- [**What is Pseudocode**](https://www.geeksforgeeks.org/dsa/what-is-pseudocode-a-complete-tutorial/):
  A complete tutorial on writing pseudocode.
- [**Real Python: Build a Tic-Tac-Toe game**](https://realpython.com/tic-tac-toe-python/):
  A more advanced, GUI-based take on the same game for when you want to go
  further.
- [**Real Python: Docstring**](https://realpython.com/how-to-write-docstrings-in-python/):
  A guide to writing and using docstrings in Python.
