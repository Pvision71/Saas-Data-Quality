# Developer Setup Guide: SaaS Data Quality and Cleansing Platform

This guide provides instructions for setting up the development environment for the SaaS Data Quality and Cleansing Platform.

## 1. Prerequisites

Ensure you have the following installed on your system:

-   **Git**: For version control.
-   **Python 3.11+**: For the backend.
-   **Node.js 20+ and npm**: For the frontend.
-   **PostgreSQL**: A running instance for the backend database.

## 2. Project Setup

1.  **Clone the repository**:

    ```bash
    git clone https://github.com/Pvision71/Saas-Data-Quality.git
    cd Saas-Data-Quality
    ```

2.  **Switch to the feature branch**:

    ```bash
    git checkout 001-saas-data-quality
    ```

## 3. Backend Setup

1.  **Navigate to the backend directory**:

    ```bash
    cd backend
    ```

2.  **Install Python dependencies**:

    ```bash
    pip install -e .
    ```

3.  **Configure PostgreSQL connection**:

    Edit `backend/src/database.py` and update `SQLALCHEMY_DATABASE_URL` with your PostgreSQL connection string.

    ```python
    SQLALCHEMY_DATABASE_URL = "postgresql://user:password@host:port/dbname"
    ```

4.  **Run database migrations** (if applicable, not yet implemented):

    *(Future task: Implement Alembic or similar for migrations)*

5.  **Start the backend server**:

    ```bash
    uvicorn src.main:app --reload
    ```

    The backend API will be available at `http://localhost:8000`.

## 4. Frontend Setup

1.  **Navigate to the frontend directory**:

    ```bash
    cd frontend
    ```

2.  **Install Node.js dependencies**:

    ```bash
    npm install
    ```

3.  **Start the frontend development server**:

    ```bash
    npm run dev
    ```

    The frontend application will be available at `http://localhost:3000`.

## 5. Running Tests

### Backend Tests

From the project root directory:

```bash
pytest
```

### Frontend Tests

From the `frontend` directory:

```bash
npm test
```

## 6. Common Issues & Troubleshooting

-   **Python `ModuleNotFoundError`**: Ensure you are running `pytest` from the project root or that your `PYTHONPATH` is correctly configured.
-   **Frontend Jest Errors**: If you encounter issues with Jest, ensure all `@testing-library` packages are correctly installed and `jest-environment-jsdom` is present.
