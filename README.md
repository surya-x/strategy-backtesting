# Strategy Backtesting

This project is designed to backtest trading strategies on historical market data, with a specific focus on equity markets. It provides a tiny-framework for analyzing and refining strategies before deploying them in live environments.

I have personally used this repository to backtest my own trading strategies on equities, to evaluate their performance and optimize them.

## Features

- **Data Integration**: Supports integration of historical market data for realistic backtesting scenarios.
- **Interactive Jupyter Notebook**: The `main.ipynb` notebook offers a user-friendly interface to run backtests and visualize results.
- **Dependency Management**: Utilizes `pyproject.toml` and `poetry.lock` for a consistent and reproducible development environment.

## Getting Started

To get started with this project, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/surya-x/strategy-backtesting.git
   cd strategy-backtesting
   ```

2. **Install Dependencies**:

   Ensure you have [Poetry](https://python-poetry.org/) installed. Then, run:

   ```bash
   poetry install
   ```

3. **Access the Jupyter Notebook**:

   Start the Jupyter Notebook server:

   ```bash
   poetry run jupyter notebook
   ```

   Open `main.ipynb` to explore and execute the backtesting framework.

## Repository Structure

- `.github/workflows/`: GitHub Actions workflows for CI/CD.
- `algorithmic_trading/`: Scripts and modules related to trading algorithms.
- `data/`: Directory designated for historical market data files.
- `main.ipynb`: Jupyter Notebook for interactive backtesting.
- `poetry.lock` & `pyproject.toml`: Files for dependency management using Poetry.

## Use Case: Backtesting Equity Strategies

This repository has been specifically utilized to backtest trading strategies on equities. By using historical equity data, I have been able to assess the viability and optimize the performance of my strategies.

## Contributing

Contributions are welcome! Please fork this repository, create a new branch for your feature or bug fix, and submit a pull request for review.

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy backtesting!
