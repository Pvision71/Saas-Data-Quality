# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SaaS Data Quality and Cleansing Platform - A platform for managing data quality and cleansing during enterprise migrations from legacy systems to modern SaaS applications. The platform handles data profiling, cleansing, mapping, validation, and audit trails.

## Architecture

**Microservices Architecture**:
- **Frontend**: Next.js/React with TypeScript, Tailwind CSS - User interface for data quality management
- **Backend**: FastAPI (Python) - RESTful API providing business logic
- **Database**: PostgreSQL - Primary data store for application metadata
- **Analytics**: DuckDB - In-memory analytical queries for data profiling
- **Auth**: Clerk - User authentication and RBAC

**Data Flow**: Frontend (authenticated via Clerk) → Backend API → PostgreSQL/DuckDB → Response to Frontend

**Deployment**: Designed for serverless platforms (AWS Lambda, Vercel, Google Cloud Run)

## Development Commands

### Backend (FastAPI/Python)
```bash
cd backend
pip install -e .                      # Install dependencies
uvicorn src.main:app --reload         # Start dev server (http://localhost:8000)
pytest                                # Run all tests from project root
pytest tests/unit                     # Run unit tests only
pytest tests/integration              # Run integration tests only
pytest tests/contract                 # Run contract tests only
```

### Frontend (Next.js/React)
```bash
cd frontend
npm install                           # Install dependencies
npm run dev                           # Start dev server (http://localhost:3000)
npm run build                         # Build for production
npm start                             # Start production server
npm run lint                          # Run ESLint
npm test                              # Run Jest tests (non-watch mode)
```

## Backend Structure

```
backend/src/
├── main.py                   # FastAPI app entry point, router registration
├── database.py               # SQLAlchemy setup (engine, session, Base)
├── api/                      # API route handlers (FastAPI routers)
│   ├── projects.py
│   └── datasources.py
├── models/                   # Pydantic models for request/response validation
│   └── models.py            # Project, DataSource, DataProfile, CleansingRule, etc.
└── services/                # Business logic layer
    ├── project_service.py
    └── datasource_service.py
```

**Key Patterns**:
- **Layered Architecture**: API routes → Services → Database
- **Dependency Injection**: Services instantiated in route handlers
- **Pydantic Models**: Used for validation and serialization (not ORM models)
- **SQLAlchemy**: Database ORM with `Base` from `database.py`

**Database Configuration**: Update `SQLALCHEMY_DATABASE_URL` in `backend/src/database.py` with your PostgreSQL connection string before running.

**Testing Strategy**:
- **Unit Tests**: Test services in isolation
- **Integration Tests**: Test API endpoints with database
- **Contract Tests**: Validate OpenAPI spec compliance

## Frontend Structure

```
frontend/src/
├── app/                      # Next.js App Router
│   ├── layout.tsx           # Root layout with providers
│   └── page.tsx             # Home page
├── pages/                    # Additional pages (dashboard, etc.)
│   └── dashboard.tsx
├── components/               # React components
│   └── ProjectList.tsx
├── services/                 # API client layer
│   └── api.ts               # Backend API calls
└── tests/                    # Jest tests
    ├── components/
    └── pages/
```

**Key Patterns**:
- **API Service Layer**: `services/api.ts` centralizes backend communication
- **TypeScript Interfaces**: Defined in service files for type safety
- **Clerk Integration**: Authentication handled via Clerk React SDK
- **App Router**: Using Next.js 15 App Router pattern

**API Configuration**: Update `API_BASE_URL` in `frontend/src/services/api.ts` if backend is not on `http://localhost:8000`.

## Core Data Models

Defined in `backend/src/models/models.py`:
- **Project**: Migration initiative container
- **DataSource**: Connection to legacy or SaaS system
- **DataProfile**: Results from data profiling process
- **CleansingRule**: Data cleansing transformation rules
- **Mapping**: Source-to-target schema mappings
- **User**: Clerk-authenticated users with RBAC

All models use UUID4 for IDs except User (Clerk-provided string ID).

## Authentication

**Clerk Integration**:
- Frontend: `@clerk/clerk-react` SDK
- Backend: `clerk-sdk-python` for token validation
- RBAC roles: admin, editor, viewer

Authentication flows through Clerk, with backend validating tokens on each API request.

## Development Workflow

1. **Feature Development**: Work on `claude/initial-project-setup-*` branches
2. **Database Changes**: Currently no migration system - update `database.py` and models directly
3. **API Changes**: Update route handlers in `api/`, service logic in `services/`, and models in `models/`
4. **Frontend Changes**: Update components, pages, or API service as needed
5. **Testing**: Run both backend (`pytest`) and frontend (`npm test`) tests

## Important Notes

- **Database Migrations**: Not yet implemented - planned future task for Alembic
- **SQLAlchemy Models**: Currently using Pydantic models; ORM models need to be created for database operations
- **Running Tests**: Backend tests must be run from project root (not backend directory) due to import paths
- **PYTHONPATH**: If encountering import errors, ensure running from project root or configure PYTHONPATH
- **Clerk Setup**: Requires Clerk API keys configured as environment variables (not yet implemented)
- **Linting**: Backend uses Ruff (see `backend/ruff.toml`), Frontend uses ESLint

## Documentation

Additional documentation available in `docs/`:
- `architecture.md` - Detailed architecture and data flow
- `developer_setup.md` - Full setup instructions
- `api.md` - API endpoint documentation
- `user_guide.md` - End-user documentation

Specifications in `specs/001-saas-data-quality/`:
- `spec.md` - Feature specification and requirements
- `plan.md` - Implementation plan
- `data-model.md` - Detailed data model design
