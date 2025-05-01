# Rubik's Cube Solver 🧩

An interactive 2D Rubik’s Cube visualizer built in **Python** using **Pygame**.  
You can rotate faces in real-time using clickable buttons — and watch the cube react instantly!

This project models the cube using object-oriented programming and is built from scratch with clean modular code.  
Eventually, this will grow into a full solver with scrambling and automated solving algorithms.

This project is being built from scratch, hence might have limited features
I am trying my best to reduce the number of bugs

🤗
---

## 📂 Project Structure

```plaintext
rubix-cube-solver/
├── core/
│   ├── __init__.py
│   ├── cube.py
│   ├── pieces.py
│   └── scramble.py
├── solver/
├── ├── __init__.py
│   └── LBL_solver.py
├── tests/
│   ├── test_cube.py
│   ├── test_pieces.py
│   ├── test_scramble.py
│   └── test_utils.py
├── uml/
│   └── rubix_cube.puml
├── utils/
│   ├── __init__.py
│   ├── colors.py
│   └── faces.py
├── visualizer/
│   ├── __init__.py
│   ├── button.py
│   └── UI.py
├── .coveragerc
├── .gitignore
├── LICENSE
├── main.py
├── pytest.ini
└── README.md
```

---

## 🚀 How to Run

### Prerequisites

 - Make sure Python 3.11+ is installed
 - Install Pygame and dependencies

```bash
pip install pygame pytest
```
(or activate your conda environment if you're using one.)

### Run the Visualizer

```bash
python main.py
```

### Run Unit Tests

```bash
pytest
```

## 🧰 Tech Stack

- **Python** 3.11+
- **Pygame** - for 2D visualization
- **OOP Design** - clean modular structure
- **Data Structures** – Multi-dimensional arrays (2D and 3D), HashMaps, enums, and custom classes
- **PlantUML** - for UML diagrams
- **Pytest** - for testing

---

## 😎 Features

- Fully interactive 2D Layout of a 3D Rubik's Cube
- Real-time visual rotation with button clicks
- Reset and Scramble buttons
- Move History Display
- Intuitive UI using Pygame
- Color-accurate representation of all six faces
- Clean and scalable object-oriented codebase

## 🛠️ Upcoming Features

- Ability to input custom cube states
- Solving algorithms (beginner -> advanced)
- Optimized move generation

## ✨ Notes

- Each face color follows the standard convention:
    - **U (Up)**: Yellow
    - **D (Down)**: White
    - **F (Front)**: Blue
    - **B (Back)**: Green
    - **R (Right)**: Red
    - **L (Left)**: Orange
- UML diagrams are created using **PlantUML** for visualizing the cube's structure and logic.
- UML diagrams are available in ```/uml/``` for internal logic representation

## 👤 Author

Created by [FuriousFire](https://github.com/FuriousFire05)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Copyright (c) 2025 [FuriousFire](https://github.com/FuriousFire05)