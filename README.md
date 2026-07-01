# AI-Powered Intelligent Resource Allocation Engine

An AI-powered platform that intelligently assigns field-service engineers to customer
service requests by combining **Operations Research**, **Machine Learning**,
**Explainable AI**, and **Interactive Visualization**.

> **Status: Runnable Scaffold.** Every API endpoint and UI page works end-to-end with
> **mock/stub data**. The allocation algorithms, ML/DL models, feature engineering, and
> SHAP explainability are **typed interface stubs** (signatures + docstrings + `TODO`s)
> ready for real implementation. See [What's Stubbed](#whats-stubbed).

---

## Architecture

```text
React Dashboard  ->  FastAPI Backend  ->  Data Generator  ->  Feature Engineering
      ^                                                              |
      |                                                              v
 Explainability  <-  Optimization Engine  <-  ML / DL Models  <-  Preprocessing
```

- **Frontend:** Vite + React + TypeScript + Tailwind CSS + Recharts + React-Leaflet
- **Backend:** FastAPI + Pydantic v2
- **Persistence:** In-memory store + serialized artifacts (pickle / parquet / joblib)
- **ML/DL:** scikit-learn (Random Forest), XGBoost, LightGBM, CatBoost, PyTorch FFNN,
  TabNet, SHAP
- **Env/tooling:** conda (`environment.yml`), pytest, Vitest

---

## Project Structure

```text
re_alc/
  backend/
    main.py              FastAPI app + CORS + routers
    config.py            Settings (paths, CORS origins)
    core/                constants, logging
    schemas/             Pydantic contracts (Technician, Request, Assignment, ...)
    api/routes/          data, models, allocation, metrics endpoints
    algorithms/          greedy, hungarian, ml, dl allocators (stubs)
    ml/                  data generation, features, preprocessing, training,
                         evaluation, explainability, registry (stubs)
    ml/models/           random_forest, xgboost, lightgbm, catboost, ffnn, tabnet (stubs)
    services/            store + orchestration services
    fixtures/            deterministic mock data for stub responses
    data/  models/       generated artifacts (gitignored)
  frontend/
    src/
      api/               typed API client
      types/             TS mirror of backend schemas
      components/        layout, map (Leaflet), kpi, explain, common
      charts/            Recharts visualizations
      pages/             Dashboard, Allocation, Models, Comparison, Explainability
      hooks/  store/  utils/
  tests/                 backend pytest suite
  environment.yml
```

---

## Getting Started

### 1. Backend

```powershell
# Create & activate the conda environment
conda env create -f environment.yml
conda activate re-alc

# Run the API (from the backend/ directory)
cd backend
uvicorn main:app --reload
```

- API root: <http://localhost:8000>
- Interactive docs (Swagger): <http://localhost:8000/docs>
- Health check: <http://localhost:8000/health>

### 2. Frontend

```powershell
cd frontend
npm install
npm run dev
```

- Dashboard: <http://localhost:5173>

The frontend calls the backend at `http://localhost:8000` (CORS pre-configured).

---

## API Endpoints

| Method | Path | Description |
| --- | --- | --- |
| POST | `/generate-data` | Generate synthetic technicians & requests |
| POST | `/train-model` | Train an ML/DL model on historical data |
| POST | `/predict` | Predict assignment success probability |
| POST | `/allocate` | Run an allocation algorithm |
| POST | `/compare` | Compare all allocation algorithms |
| GET | `/metrics` | ML metrics + executive KPIs |
| GET | `/technicians` | List technicians |
| GET | `/requests` | List service requests |
| GET | `/assignments` | List assignments |

---

## Testing

```powershell
# Backend (from repo root, with conda env active)
pytest

# Frontend
cd frontend
npm run test
```

---

## What's Stubbed

These modules expose finished **interfaces** but return mock data or raise
`NotImplementedError`. They are the intended targets for real implementation:

- `backend/algorithms/*` — Greedy, Hungarian, ML, and DL allocation logic
- `backend/ml/data_generator.py` — synthetic 1,000 technicians / 10,000 assignments
- `backend/ml/feature_engineering.py` — the 13 engineered features
- `backend/ml/preprocessing.py` — clean / encode / scale / split
- `backend/ml/models/*` — Random Forest, XGBoost, LightGBM, CatBoost, FFNN, TabNet
- `backend/ml/training.py`, `evaluation.py` — training loop + metrics
- `backend/ml/explainability.py` — SHAP / feature-importance explanations

---

## License

For demonstration / portfolio use.
