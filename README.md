# SaaS Data Quality and Cleansing Platform

A comprehensive platform for managing data quality and cleansing during enterprise migrations from legacy systems to modern SaaS applications. Built to reduce the cost, risk, and time associated with poor data quality, incompatibility, and manual transformation during critical digital transformation initiatives.

## Overview

The SaaS Data Quality Platform provides essential data quality management capabilities for enterprises migrating from complex, customized legacy business applications to modern, standardized SaaS-based enterprise applications (e.g., ERP, CRM, HRIS cloud solutions). It ensures data integrity, compliance, and accelerates time-to-value for new SaaS investments.

## Key Features

- **Intelligent Data Profiling**: Automatically discover data structures, relationships, and quality issues in legacy sources
- **AI-Powered Data Cleansing**: De-duplication, format standardization, and correction of erroneous data
- **Visual Data Mapping**: AI-suggested transformations from legacy to target SaaS schemas
- **Automated Validation**: Configurable validation rules engine for pre- and post-migration checks
- **Quality Monitoring**: Dashboards and alerts for continuous data quality monitoring
- **Complete Audit Trail**: Comprehensive data lineage and audit logs for all transformations
- **Collaboration Support**: Role-Based Access Control (RBAC) and workflow management
- **Analytics & Reporting**: Data quality improvements, compliance, and migration progress reports

## Architecture

The platform follows a **microservices architecture** designed for serverless deployment:

```mermaid
graph TB
    subgraph "Client Layer"
        UI[Frontend<br/>Next.js 15 + React + TypeScript<br/>Tailwind CSS<br/>Port 3000]
    end

    subgraph "API Layer"
        API[Backend API<br/>FastAPI + Python<br/>RESTful API<br/>Port 8000]
    end

    subgraph "Authentication"
        AUTH[Clerk Auth<br/>User Management<br/>RBAC]
    end

    subgraph "Data Layer"
        DB[(PostgreSQL<br/>Primary Database<br/>Application Data)]
        ANALYTICS[(DuckDB<br/>In-Memory Analytics<br/>Data Profiling)]
    end

    UI -->|HTTPS/REST| API
    API -->|Validate Token| AUTH
    API -->|CRUD Operations| DB
    API -->|Analytics Queries| ANALYTICS
    UI -.->|Authentication| AUTH

    style UI fill:#4f46e5,stroke:#312e81,stroke-width:2px,color:#fff
    style API fill:#059669,stroke:#065f46,stroke-width:2px,color:#fff
    style AUTH fill:#dc2626,stroke:#991b1b,stroke-width:2px,color:#fff
    style DB fill:#2563eb,stroke:#1e40af,stroke-width:2px,color:#fff
    style ANALYTICS fill:#7c3aed,stroke:#5b21b6,stroke-width:2px,color:#fff
```

### Data Flow

```mermaid
sequenceDiagram
    actor User
    participant Frontend
    participant Clerk
    participant Backend
    participant PostgreSQL
    participant DuckDB

    User->>Frontend: Access Application
    Frontend->>Clerk: Authenticate User
    Clerk-->>Frontend: Auth Token

    User->>Frontend: Create Project
    Frontend->>Backend: POST /projects (with token)
    Backend->>Clerk: Validate Token
    Clerk-->>Backend: Token Valid
    Backend->>PostgreSQL: Insert Project
    PostgreSQL-->>Backend: Project Created
    Backend-->>Frontend: 201 Created
    Frontend-->>User: Show Success

    User->>Frontend: Profile Data Source
    Frontend->>Backend: POST /datasources/profile
    Backend->>DuckDB: Run Analytics Query
    DuckDB-->>Backend: Profile Results
    Backend->>PostgreSQL: Store Profile
    Backend-->>Frontend: Profile Data
    Frontend-->>User: Display Results
```

### Tech Stack

**Frontend:**
- Next.js 15 (App Router)
- React 18
- TypeScript
- Tailwind CSS 4
- Clerk React SDK (Authentication)

**Backend:**
- FastAPI (Python web framework)
- Pydantic (Data validation)
- SQLAlchemy (ORM)
- PostgreSQL (Primary database)
- DuckDB (In-memory analytics)
- Clerk Python SDK (Authentication)

**Testing:**
- pytest (Backend)
- Jest + React Testing Library (Frontend)

## Prerequisites

- **Git**: For version control
- **Python 3.11+**: For the backend
- **Node.js 20+** and **npm**: For the frontend
- **PostgreSQL**: A running instance for the backend database

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Pvision71/Saas-Data-Quality.git
cd Saas-Data-Quality
```

### 2. Backend Setup

```bash
cd backend

# Install dependencies
pip install -e .

# Configure PostgreSQL connection
# Edit backend/src/database.py and update SQLALCHEMY_DATABASE_URL
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@host:port/dbname"

# Start the development server
uvicorn src.main:app --reload
```

The backend API will be available at `http://localhost:8000`

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend application will be available at `http://localhost:3000`

## Project Structure

```
Saas-Data-Quality/
├── backend/                    # FastAPI backend
│   ├── src/
│   │   ├── main.py            # App entry point
│   │   ├── database.py        # SQLAlchemy configuration
│   │   ├── api/               # API route handlers
│   │   │   ├── projects.py
│   │   │   └── datasources.py
│   │   ├── models/            # Pydantic models
│   │   │   └── models.py
│   │   └── services/          # Business logic layer
│   │       ├── project_service.py
│   │       └── datasource_service.py
│   ├── tests/                 # Backend tests
│   │   ├── unit/
│   │   ├── integration/
│   │   └── contract/
│   ├── pyproject.toml         # Python dependencies
│   └── ruff.toml             # Linting configuration
│
├── frontend/                  # Next.js frontend
│   ├── src/
│   │   ├── app/              # Next.js App Router
│   │   │   ├── layout.tsx
│   │   │   └── page.tsx
│   │   ├── pages/            # Additional pages
│   │   ├── components/       # React components
│   │   ├── services/         # API client layer
│   │   │   └── api.ts
│   │   └── tests/            # Frontend tests
│   ├── package.json          # Node dependencies
│   └── jest.config.js        # Jest configuration
│
├── docs/                      # Documentation
│   ├── architecture.md
│   ├── developer_setup.md
│   ├── api.md
│   └── user_guide.md
│
├── specs/                     # Feature specifications
│   └── 001-saas-data-quality/
│       ├── spec.md
│       ├── plan.md
│       └── data-model.md
│
├── CLAUDE.md                  # Claude Code guidance
└── README.md                  # This file
```

## Data Models

The platform manages the following core entities:

- **Project**: Migration initiative container
- **DataSource**: Connection to legacy or SaaS system
- **DataProfile**: Results from data profiling process
- **CleansingRule**: Data cleansing transformation rules
- **Mapping**: Source-to-target schema mappings
- **User**: Clerk-authenticated users with RBAC roles

### Entity Relationship Diagram

```mermaid
erDiagram
    USER ||--o{ PROJECT : creates
    PROJECT ||--o{ DATASOURCE : contains
    PROJECT ||--o{ CLEANSINGRULE : defines
    PROJECT ||--o{ MAPPING : has
    DATASOURCE ||--o{ DATAPROFILE : profiled_by
    DATASOURCE ||--o{ MAPPING : "source/target"

    USER {
        string id PK "From Clerk"
        uuid organization_id
        string role "admin, editor, viewer"
    }

    PROJECT {
        uuid id PK
        string name
        timestamp created_at
        timestamp updated_at
    }

    DATASOURCE {
        uuid id PK
        uuid project_id FK
        string name
        string type "legacy_db, saas_app"
        jsonb connection_details
    }

    DATAPROFILE {
        uuid id PK
        uuid datasource_id FK
        string status "running, completed, failed"
        jsonb results
        timestamp created_at
    }

    CLEANSINGRULE {
        uuid id PK
        uuid project_id FK
        string name
        text description
        jsonb implementation
    }

    MAPPING {
        uuid id PK
        uuid project_id FK
        uuid source_datasource_id FK
        uuid target_datasource_id FK
        jsonb mapping_details
    }
```

See `specs/001-saas-data-quality/data-model.md` for detailed entity definitions.

## Development

### Running Tests

**Backend Tests:**
```bash
# From project root
pytest                     # Run all tests
pytest tests/unit          # Run unit tests only
pytest tests/integration   # Run integration tests only
pytest tests/contract      # Run contract tests only
```

**Frontend Tests:**
```bash
cd frontend
npm test                   # Run Jest tests
```

### Linting

**Backend:**
```bash
cd backend
ruff check .               # Run Ruff linter
```

**Frontend:**
```bash
cd frontend
npm run lint               # Run ESLint
```

### Building for Production

**Backend:**
```bash
# Backend runs directly with uvicorn
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
npm run build              # Build production bundle
npm start                  # Start production server
```

## API Documentation

The backend API provides RESTful endpoints for all data quality operations. Key endpoints:

- `GET /projects` - List all projects
- `POST /projects/{projectId}/datasources` - Create a new data source

For complete API documentation, see `docs/api.md` or visit `http://localhost:8000/docs` (Swagger UI) when the backend is running.

## Authentication

The platform uses [Clerk](https://clerk.com) for user authentication and authorization:

- **Frontend**: `@clerk/clerk-react` SDK
- **Backend**: `clerk-sdk-python` for token validation
- **RBAC Roles**: admin, editor, viewer

Note: Clerk API keys need to be configured as environment variables (setup in progress).

## Deployment

The platform is designed for serverless deployment on cloud platforms:

- **Frontend**: Vercel, AWS Amplify, or similar
- **Backend**: AWS Lambda, Google Cloud Run, or similar
- **Database**: Managed PostgreSQL (AWS RDS, Google Cloud SQL, etc.)

### Deployment Architecture

```mermaid
graph TB
    subgraph "CDN/Edge"
        CDN[Vercel Edge Network<br/>Static Assets + SSR]
    end

    subgraph "Frontend Hosting"
        VERCEL[Vercel<br/>Next.js Application<br/>Auto-scaling]
    end

    subgraph "Backend Services"
        LAMBDA[AWS Lambda / Cloud Run<br/>FastAPI Application<br/>Auto-scaling]
        API_GW[API Gateway<br/>Rate Limiting & Caching]
    end

    subgraph "Authentication Service"
        CLERK_CLOUD[Clerk Cloud<br/>Managed Auth Service]
    end

    subgraph "Data Services"
        RDS[(AWS RDS / Cloud SQL<br/>PostgreSQL<br/>Managed Database)]
        DUCKDB_LAMBDA[DuckDB<br/>In Lambda Runtime<br/>Ephemeral Analytics]
    end

    subgraph "Monitoring & Logging"
        LOGS[CloudWatch / Cloud Logging]
        METRICS[Application Metrics]
    end

    CDN -->|Serves| VERCEL
    VERCEL -->|API Calls| API_GW
    API_GW -->|Routes| LAMBDA
    LAMBDA -->|Validate| CLERK_CLOUD
    LAMBDA -->|Queries| RDS
    LAMBDA -->|Analytics| DUCKDB_LAMBDA
    LAMBDA -.->|Logs| LOGS
    LAMBDA -.->|Metrics| METRICS

    style CDN fill:#0ea5e9,stroke:#0369a1,stroke-width:2px,color:#fff
    style VERCEL fill:#4f46e5,stroke:#312e81,stroke-width:2px,color:#fff
    style LAMBDA fill:#059669,stroke:#065f46,stroke-width:2px,color:#fff
    style CLERK_CLOUD fill:#dc2626,stroke:#991b1b,stroke-width:2px,color:#fff
    style RDS fill:#2563eb,stroke:#1e40af,stroke-width:2px,color:#fff
```

## Contributing

1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Make your changes and test thoroughly
3. Commit with descriptive messages
4. Push to your branch: `git push origin feature/your-feature-name`
5. Create a Pull Request

## Documentation

Additional documentation is available in the `docs/` directory:

- `architecture.md` - Detailed architecture and data flow
- `developer_setup.md` - Full setup instructions
- `api.md` - API endpoint documentation
- `user_guide.md` - End-user documentation

## Current Status

This project is in active development. Current implementation status:

- ✅ Project structure and architecture defined
- ✅ Backend API skeleton with FastAPI
- ✅ Frontend skeleton with Next.js 15
- ✅ Data models defined
- ✅ Test structure established
- 🚧 Database migrations (planned - Alembic)
- 🚧 Clerk authentication integration
- 🚧 Data profiling engine
- 🚧 Data cleansing algorithms
- 🚧 Visual mapping tools

## License

[License information to be added]

## Support

For issues, questions, or contributions, please open an issue on GitHub or contact the development team.

---

**Built with ❤️ for enterprise data migration success**
