# FastAPI Learning

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-499848)
![uv](https://img.shields.io/badge/package%20manager-uv-DE5FE9)
![Status](https://img.shields.io/badge/status-learning%20project-blue)

A hands-on learning repository for exploring the core concepts of **[FastAPI](https://fastapi.tiangolo.com/)**. It uses a small patient-records dataset (with BMI and health verdicts) to demonstrate how to build REST endpoints, read data from a JSON file, and work with **path** and **query** parameters.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Running the Application](#running-the-application)
- [API Reference](#api-reference)
- [Sample Data](#sample-data)
- [Interactive API Docs](#interactive-api-docs)
- [Learning Roadmap](#learning-roadmap)
- [Contributing](#contributing)
- [Author](#author)

---

## Features

- Basic FastAPI app with multiple GET endpoints
- JSON file used as a lightweight data source
- **Path parameters** with validation and documentation via `Path(...)`
- **Query parameters** examples
- Automatic interactive documentation (Swagger UI and ReDoc)
- Reproducible dependency management with [`uv`](https://docs.astral.sh/uv/)

## Tech Stack

| Component | Details |
| --- | --- |
| Language | Python 3.12+ |
| Framework | FastAPI |
| Server | Uvicorn (ASGI) |
| Package manager | uv (`pyproject.toml` + `uv.lock`) |
| Data store | `data.json` (flat file) |

## Project Structure

```
FastAPI-Learning/
├── main.py            # Basic app: home, about, and view-all-data endpoints
├── path_params.py     # Path parameter example: fetch a patient by ID
├── query_params.py    # Query parameter examples
├── data.json          # Sample patient dataset
├── pyproject.toml     # Project metadata and dependencies
├── uv.lock            # Locked dependency versions
├── .python-version    # Pinned Python version
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- **Python 3.12** or newer
- **[uv](https://docs.astral.sh/uv/getting-started/installation/)** (recommended) or `pip`

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/mjamshaid786/FastAPI-Learning.git
   cd FastAPI-Learning
   ```

2. **Install dependencies**

   Using `uv` (recommended):

   ```bash
   uv sync
   ```

   Or using `pip`:

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   pip install fastapi uvicorn
   ```

## Running the Application

Each file is a standalone FastAPI app. Start whichever one you want to explore with Uvicorn:

```bash
# Basic endpoints
uv run uvicorn main:app --reload

# Path parameters example
uv run uvicorn path_params:app --reload

# Query parameters example
uv run uvicorn query_params:app --reload
```

> If you are not using `uv`, drop the `uv run` prefix and run `uvicorn main:app --reload` inside your activated virtual environment.

The server starts at **http://127.0.0.1:8000** by default.

## API Reference

### `main.py`

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Health-check style welcome message |
| `GET` | `/about` | Returns information about the author |
| `GET` | `/view` | Returns every record from `data.json` |

**Example**

```bash
curl http://127.0.0.1:8000/
```

```json
{ "message": "My First API is working" }
```

### `path_params.py`

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/patient/{patient_id}` | Returns a single patient record by ID |

`patient_id` is a required path parameter (for example `P001`). If the ID does not exist, the API returns `{"error": "patient not found"}`.

**Example**

```bash
curl http://127.0.0.1:8000/patient/P001
```

```json
{
  "name": "Ananya Sharma",
  "city": "Guwahati",
  "age": 28,
  "gender": "female",
  "height": 1.65,
  "weight": 90.0,
  "bmi": 33.06,
  "verdict": "Obese"
}
```

### `query_params.py`

Demonstrates how to accept optional and required query parameters (for example `?sort_by=...&order=...`) on top of the same dataset. See the source file for the exact endpoints and parameters.

## Sample Data

`data.json` contains five sample patients keyed by ID (`P001` to `P005`). Each record includes:

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Patient name |
| `city` | string | City of residence |
| `age` | integer | Age in years |
| `gender` | string | Gender |
| `height` | float | Height in metres |
| `weight` | float | Weight in kilograms |
| `bmi` | float | Body Mass Index |
| `verdict` | string | Category: Underweight, Normal, Overweight, or Obese |

> The dataset is fictional and used for demonstration only.

## Interactive API Docs

FastAPI generates documentation automatically. With the server running, open:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Learning Roadmap

- [x] Create a first FastAPI application and endpoints
- [x] Read and serve data from a JSON file
- [x] Path parameters with `Path()` validation
- [x] Query parameters
- [ ] Request bodies and Pydantic models (`POST`)
- [ ] Update and delete operations (`PUT`, `DELETE`)
- [ ] Proper error handling with `HTTPException` and status codes
- [ ] Computed fields and validation with Pydantic
- [ ] Database integration (SQLite / PostgreSQL)
- [ ] Testing with `pytest` and `TestClient`
- [ ] Containerisation with Docker

## Contributing

This is a personal learning project, but suggestions are welcome. To propose a change:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## Author

**Muhammad Jamshaid**
GitHub: [@mjamshaid786](https://github.com/mjamshaid786)

---

If you find this repository helpful, consider giving it a star.
