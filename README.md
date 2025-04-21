<h1 align="center">🚖 TaxiTime – NYC Taxi Trip Duration Predictor 🚖</h1>

<p align="center"><strong>An End-to-End MLOps Pipeline Built with DVC, MLflow, and FastAPI</strong></p>

---

## Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Architecture & Technologies](#architecture--technologies)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Data Pipeline](#data-pipeline)
  - [Training & Experiments](#training--experiments)
  - [Serving Predictions](#serving-predictions)
- [Project Structure](#project-structure)
- [Evaluation & Results](#evaluation--results)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

Predicting the duration of taxi rides in New York City is a classic regression problem with real-world business applications. This repository provides:

- A reproducible data pipeline with DVC for versioning raw, interim, and processed datasets.
- Feature engineering driven by modular Python code.
- Model training and hyperparameter tuning with MLflow for experiment tracking.
- Serialization and versioning of models using DVC and MLflow Model Registry.
- A lightweight FastAPI service to serve predictions in real-time.
- Containerization with Docker for consistent deployments.
- CI/CD-ready structure with Makefile and tox for testing.

## Key Features

- End-to-end ML pipeline: from raw data ingestion to production-ready API.
- Data versioning and pipeline orchestration with DVC.
- Experiment tracking, logging, and model registry with MLflow.
- Feature engineering encapsulated in reusable modules.
- High-performance XGBoost models (or scikit-learn RandomForest).
- Automated testing and linting (pytest, flake8, mypy).
- Dockerized application for easy deployment.
- Clear project structure for collaborative development.

## Architecture & Technologies

- **Language**: Python 3.8+
- **Data Versioning**: DVC
- **Experiment Tracking**: MLflow
- **Web Framework**: FastAPI & Uvicorn
- **Modeling**: XGBoost or scikit-learn RandomForest
- **Data Processing**: Pandas, NumPy
- **Deployment**: Docker, Makefile
- **Testing & CI**: pytest, tox, flake8, mypy

## Getting Started

### Prerequisites

- Git
- Python 3.8+
- pip
- DVC
- MLflow
- Docker (optional, for container builds)

### Installation

```bash
git clone https://github.com/tanny1412/nyc-taxi-duration-mlops.git
cd nyc-taxi-duration-mlops
pip install -r requirements.txt
pip install -e .
dvc pull           # fetch data and model artifacts
```

### Data Pipeline

Generate and process datasets:

```bash
make data
# or
dvc repro
```

- Raw data → cleaned and split into `data/processed/train.csv` and `data/processed/test.csv`.

### Training & Experiments

Train models and log experiments:

```bash
make train
# or
python -m src.models.train_model
```

- Hyperparameters and metrics are recorded to the MLflow server (`mlruns/`).
- Model artifacts are versioned with DVC.

Launch the MLflow UI to compare runs:

```bash
mlflow ui
```

### Serving Predictions

Start the FastAPI service:

```bash
uvicorn service:app --host 0.0.0.0 --port 8080
```

Example request:

```bash
curl -X POST "http://localhost:8080/predict" \
     -H "Content-Type: application/json" \
     -d '{
          "vendor_id": 2,
          "pickup_datetime": 1700000000,
          "passenger_count": 1,
          "pickup_longitude": -73.985,
          "pickup_latitude": 40.748,
          "dropoff_longitude": -73.975,
          "dropoff_latitude": 40.752,
          "store_and_fwd_flag": 0
        }'
```

## Project Structure

```text
.
├── data/               # Data versioned by DVC
├── docs/               # Sphinx docs
├── mlruns/             # MLflow experiment tracking
├── notebooks/          # Jupyter notebooks for exploration
├── reports/            # Generated reports and figures
├── service.py          # FastAPI application for inference
├── src/                # Source code package
│   ├── data/           # Data ingestion and processing
│   ├── features/       # Feature engineering
│   ├── models/         # Training, prediction, and model deployment
│   └── visualization/  # Plotting utilities
├── Dockerfile
├── Makefile
├── requirements.txt
├── dvc.yaml            # DVC pipeline
├── models.dvc          # DVC tracking of model artifacts
└── README.md
```

## Evaluation & Results

- Competitive RMSE on test set (see MLflow runs for details).
- Feature importance insights and visual diagnostics available under `reports/figures`.

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Make your changes and add tests.
4. Ensure linting and tests pass: `make lint && make test`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact

Created by **Tanish Kandivlikar** ([@tanny1412](https://github.com/tanny1412)).  
Feel free to reach out at [tkandivlikar@wpi.edu](mailto:tkandivlikar@wpi.edu).