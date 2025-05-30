# Financial Data EDA with News Sentiment Analysis

## Project Overview
This repository is a part of the challenge given by 10Academy for the training goven by 
This project performs Exploratory Data Analysis (EDA) on a a given dataset by combining financial stock data and associated news articles. The goal is to analyze stock price movements, extract sentiment from news, and explore potential correlations between news sentiment and stock performance.

## Folder Structure

* `.vscode/`: VS Code specific settings.
* `.github/workflows/`: GitHub Actions for CI/CD (e.g., running unit tests).
* `.gitignore`: Specifies files/folders to be ignored by Git.
* `requirements.txt`: Python package dependencies.
* `README.md`: This project overview.
* `src/`: Contains reusable Python modules for data loading, processing, and analysis.
* `notebooks/`: Jupyter notebooks for interactive EDA, visualizations, and analysis.
* `tests/`: Unit tests for the modules in `src/`.
* `scripts/`: Standalone scripts for data generation or automation tasks.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/abdumehammed/Kaim5-Week1-challenge.git
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **EDA:**


5.  **Run Tests:**
    ```bash
    pytest tests/
    ```

6.  **Launch Jupyter Lab/Notebook:**
    ```bash
    jupyter lab
    ```
    Navigate to the `notebooks/` directory and open `01_eda_financial_and_news.ipynb` to start the analysis.


## Author

Abdulhamid M.