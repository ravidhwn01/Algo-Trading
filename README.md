# Trading Algorithm Project

This project aims to develop a stock price prediction model and a trading signal generator using historical stock data and technical indicators.

## Project Structure

- `data/`: Contains the raw, processed, and external data.
  - `raw/`: Raw, immutable data.
  - `processed/`: Cleaned and preprocessed data.
  - `external/`: Data from third-party sources.
- `notebooks/`: Jupyter notebooks for exploration and experimentation.
- `src/`: Source code for the project.
  - `data/`: Scripts to download or generate data.
  - `features/`: Scripts to generate features from the data.
  - `models/`: Scripts to train and evaluate models.
  - `visualization/`: Scripts to create visualizations.
- `models/`: Trained and serialized models.
- `reports/`: Generated analysis as HTML, PDF, etc.
  - `figures/`: Generated figures and plots.
- `requirements.txt`: Project dependencies.
- `main.py`: Main script to run the project.
