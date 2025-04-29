# Rubik's Cube Solver 🧩

This is a Rubik's Cube Solver project written in **Python**.

The cube uses object-oriented principles to represent pieces, faces, and rotations.  
The goal is to eventually solve a scrambled cube algorithmically!

This project is being built from scratch, hence might have limited features
I am trying my best to reduce the number of bugs

🤗
---

## 📂 Project Structure

```plaintext
rubix-cube-solver/
├── solver/
│   ├── __init__.py
│   ├── cube.py
│   └── pieces.py
├── tests/
│   └── test_cube.py
├── uml/
│   └── rubix_cube.puml
├── utils/
│   ├── __init__.py
│   ├── colors.py
│   └── faces.py
├── .coveragerc
├── .gitignore
├── main.py
├── pytest.ini
└── README.md
```

---

## 🚀 How to Run

Make sure you are inside the project's **conda environment**.

Then run:

```bash
python main.py
```

To run tests:

```bash
pytest
```

## 📋 Requirements

- Python 3.11+
- `pytest` (for running tests)
- Optional tools:
    - `black` (code formatting)
    - `ruff` (linting)

---

## 😎 Features

- Object Oriented Design of a 3D Rubix cube
- Visual Graphics for cube layout using Pygame
- Interactive Buttons for Cube Rotation
- Game Updates the cube layout after rotation button clicks in Real-Time

## 🛠️ Upcoming Updates

- Reset, Scramble Functions
- Take cube layout as input
- Implement solving algorithms
- Optimized Solution to solve the cube

## ✨ Notes

- Each face color follows the standard convention:
    - **U (Up)**: Yellow
    - **D (Down)**: White
    - **F (Front)**: Blue
    - **B (Back)**: Green
    - **R (Right)**: Red
    - **L (Left)**: Orange
- UML diagrams are created using **PlantUML** for visualizing the cube's structure and logic.


## 👤 Author

[FuriousFire](https://github.com/FuriousFire05)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Copyright (c) 2025 [FuriousFire](https://github.com/FuriousFire05)