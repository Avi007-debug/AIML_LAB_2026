# AIML Lab - 5th Semester

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Supported-013243.svg?logo=numpy&logoColor=white)](https://numpy.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Supported-F7931E.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Supported-11557c.svg)](https://matplotlib.org/)

Repository containing practical lab implementations of fundamental **Artificial Intelligence** search algorithms and **Machine Learning** algorithms for Semester 5 AIML Lab.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Repository Structure](#-repository-structure)
- [Requirements & Dependencies](#-requirements--dependencies)
- [Setup & Installation](#-setup--installation)
- [Experiments & How to Run](#-experiments--how-to-run)
  - [1. Tic-Tac-Toe (Minimax with Backtracking)](#1-tic-tac-toe-minimax-with-backtracking)
  - [2. Alpha-Beta Pruning](#2-alpha-beta-pruning)
  - [3. 8-Puzzle Problem (A* Search)](#3-8-puzzle-problem-a-search)
  - [4. Hill Climbing Search](#4-hill-climbing-search)
  - [5. K-Nearest Neighbors (KNN)](#5-k-nearest-neighbors-knn)
  - [6. K-Means Clustering (OOP Custom)](#6-k-means-clustering-oop-custom)
  - [7. K-Means Clustering (Vectorized NumPy)](#7-k-means-clustering-vectorized-numpy)
- [Summary of Algorithms](#-summary-of-algorithms)

---

## 📌 Overview

This repository includes hands-on implementations covering core areas of AI and ML:
- **Game Playing & Adversarial Search**: Minimax with Backtracking, Alpha-Beta Pruning.
- **Informed & Local Search Strategies**: A* Search with heuristic evaluation, Hill Climbing optimization.
- **Supervised Learning**: K-Nearest Neighbors (KNN) from first principles on the Iris dataset.
- **Unsupervised Learning**: Custom K-Means clustering (both modular object-oriented and concise vectorized versions) with cluster visualizations.

---

## 📂 Repository Structure

| File | Algorithm / Topic | Paradigm | Description |
| :--- | :--- | :--- | :--- |
| `1. tic-tac-toe.py` | Minimax Search / DFS | AI Game Playing | Interactive Tic-Tac-Toe game where the AI plays optimal moves using minimax search and backtracking. |
| `2. Alpha-beta_pruning.py` | Alpha-Beta Pruning | Adversarial Search | Game tree search optimization that prunes unnecessary subtrees using $\alpha$ and $\beta$ bounds. |
| `3. 8-puzzle(A-star).py` | A* Search Algorithm | Informed Search | Solves the classic 8-puzzle sliding tile problem using misplaced tile heuristics and a priority queue. |
| `4. Hill_Climb_Search.py` | Hill Climbing | Local Search Optimization | Finds local/global maxima for mathematical functions using iterative ascent. |
| `7. knn.py` | K-Nearest Neighbors | Supervised ML | Multiclass classification on the Iris dataset using Euclidean distance, confusion matrix, and classification report. |
| `8. k-means.py` | K-Means Clustering (OOP) | Unsupervised ML | Full class-based implementation of K-Means clustering with Matplotlib 2D scatter visualization. |
| `8. kmeans_short.py` | K-Means Clustering (Vectorized) | Unsupervised ML | Compact, vectorized NumPy implementation of K-Means with visualization and Hungarian mapping evaluation. |
| `requirements.txt` | Dependencies | Environment | Python package dependencies for running all experiments. |
| `.gitignore` | Git Ignore | Configuration | Ignores virtual environments, caches, and system files. |

---

## 📦 Requirements & Dependencies

The experiments require **Python 3.10+** and the following scientific computing and machine learning packages:

- `numpy` (>= 1.24.0)
- `scikit-learn` (>= 1.2.0)
- `matplotlib` (>= 3.7.0)
- `scipy` (>= 1.10.0)

All dependencies are listed in [requirements.txt](requirements.txt).

---

## 🚀 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Avi007-debug/AIML_LAB_2026.git
cd AIML_LAB_2026
```

### 2. Create and Activate a Virtual Environment

It is recommended to use a virtual environment to manage dependencies:

#### Windows (PowerShell)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### Windows (Command Prompt)
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

#### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🧪 Experiments & How to Run

### 1. Tic-Tac-Toe (Minimax with Backtracking)

An unbeatable AI playing Tic-Tac-Toe using depth-first minimax search with backtracking.
- AI plays as `X` (maximizer).
- Human player plays as `O` (minimizer).

```bash
python "1. tic-tac-toe.py"
```

**Interaction**: Enter row (0-2) and column (0-2) when prompted during your turn.

---

### 2. Alpha-Beta Pruning

Computes the optimal minimax value on a binary game tree with alpha-beta pruning to skip redundant evaluation branches.

```bash
python "2. Alpha-beta_pruning.py"
```

**Sample Input**:
```text
Enter values separated by spaces: 3 5 6 9 1 2 0 -1
Enter depth: 3
```

**Sample Output**:
```text
The optimal value is: 5
```

---

### 3. 8-Puzzle Problem (A* Search)

Solves the 8-puzzle board configuration using the A* search algorithm with misplaced tiles as the heuristic function $h(n)$ and step cost $g(n)$.

```bash
python "3. 8-puzzle(A-star).py"
```

**Output**: Displays the step-by-step puzzle board transitions from the start configuration to the goal state along with the total move count.

---

### 4. Hill Climbing Search

Performs local search optimization on a user-provided continuous mathematical function of $x$ to find local/global maxima.

```bash
python "4. Hill_Climb_Search.py"
```

**Sample Input**:
```text
Enter a function of x (e.g., -(x-2)**2 + 4): -(x-2)**2 + 4
Enter the starting value (e.g., 0): 0
```

**Sample Output**:
```text
Maxima found at x = 2.0
Maximum value = 4.0
```

---

### 5. K-Nearest Neighbors (KNN)

Classifies samples from the Fisher's Iris dataset using custom $k$-NN ($k=3$) based on Euclidean distance metric. Evaluates accuracy, prints the confusion matrix, and generates a detailed classification report.

```bash
python "7. knn.py"
```

**Sample Output**:
```text
Accuracy: 0.9778
Predictions: ['setosa' 'versicolor' ...]

Confusion Matrix:
[[14  0  0]
 [ 0 18  0]
 [ 0  1 12]]

Classification Report:
              precision    recall  f1-score   support
      setosa       1.00      1.00      1.00        14
  versicolor       0.95      1.00      0.97        18
   virginica       1.00      0.92      0.96        13
```

---

### 6. K-Means Clustering (OOP Custom)

An object-oriented implementation of the $k$-Means clustering algorithm on the Iris dataset. It implements random centroid initialization, assignment step, update step, and convergence detection, followed by an interactive Matplotlib 2D scatter plot of clusters and centroids.

```bash
python "8. k-means.py"
```

---

### 7. K-Means Clustering (Vectorized NumPy)

A concise, vectorized implementation of $k$-Means leveraging NumPy array broadcasting for fast distance calculations and centroid updates, along with cluster visualization.

```bash
python "8. kmeans_short.py"
```

---

## 🧠 Summary of Algorithms

| Category | Algorithm | Key Concept | Time / Complexity |
| :--- | :--- | :--- | :--- |
| **Search** | Minimax | Game tree exploration, zero-sum game | $O(b^d)$ |
| **Search** | Alpha-Beta Pruning | Branch-and-bound pruning of minimax tree | Best: $O(b^{d/2})$, Worst: $O(b^d)$ |
| **Search** | A* Search | Best-first search with heuristic $f(n) = g(n) + h(n)$ | Guided by heuristic admissibility |
| **Search** | Hill Climbing | Greedy local search, gradient-free ascent | $O(\text{iterations})$ (vulnerable to local maxima) |
| **ML** | $k$-Nearest Neighbors | Instance-based / lazy learning with $L_2$ norm | $O(n \cdot d)$ per query |
| **ML** | $k$-Means Clustering | Partitioning clustering via Expectation-Maximization | $O(I \cdot k \cdot n \cdot d)$ |

---

## 👨‍💻 Author

- **Avishkar More**
- Repository: [Avi007-debug/AIML_LAB_2026](https://github.com/Avi007-debug/AIML_LAB_2026)
