# Application Architecture and Data Flow

This document provides a high-level overview of the SaaS Data Quality and Cleansing Platform's architecture and how data flows through its components.

## 1. High-Level Architecture

The application follows a microservices-oriented architecture, with a clear separation between the frontend (user interface) and the backend (API and business logic). It is designed for a serverless deployment model, leveraging cloud services for scalability and cost-efficiency.

```
+------------------+
|    Frontend      |
| (Next.js/React)  |
+--------+---------+
         | HTTP/S
         v
+------------------+
|     Backend      |
|   (FastAPI)      |
+--------+---------+
         | API Calls
         v
+------------------+
|   Authentication |
|     (Clerk)      |
+--------+---------+
         |
         v
+------------------+
|    Database      |
|   (PostgreSQL)   |
+--------+---------+
         |
         v
+------------------+
|    Analytics     |
|     (DuckDB)     |
+------------------+
```

## 2. Component Breakdown

### 2.1. Frontend (Next.js/React)

-   **Purpose**: Provides the user interface for interacting with the platform.
-   **Technologies**: Next.js (React framework), React (UI library), TypeScript, Tailwind CSS.
-   **Key Responsibilities**:
    -   User authentication and session management (via Clerk).
    -   Displaying project dashboards, data source configurations, profiling results, and cleansing rules.
    -   Handling user input and interactions.
    -   Making API calls to the backend.

### 2.2. Backend (FastAPI)

-   **Purpose**: Exposes the core business logic and data management functionalities via a RESTful API.
-   **Technologies**: FastAPI (Python web framework), Python, Pydantic (data validation), PostgreSQL (main database), DuckDB (in-memory analytics).
-   **Key Responsibilities**:
    -   Managing projects, data sources, data profiles, cleansing rules, and mappings.
    -   Orchestrating data profiling, cleansing, and transformation processes.
    -   Interacting with the database.
    -   Handling authentication and authorization (via Clerk integration).
    -   Providing data for the frontend.

### 2.3. Authentication (Clerk)

-   **Purpose**: Manages user authentication, authorization, and user profiles.
-   **Technologies**: Clerk SDKs (React and Python).
-   **Key Responsibilities**:
    -   User registration and login.
    -   Role-Based Access Control (RBAC).
    -   Secure session management.

### 2.4. Database (PostgreSQL)

-   **Purpose**: Primary data store for application metadata, project configurations, user information, and potentially large datasets related to data profiling and cleansing.
-   **Technologies**: PostgreSQL.
-   **Key Responsibilities**:
    -   Persisting application state.
    -   Storing structured data.

### 2.5. Analytics (DuckDB)

-   **Purpose**: Used for fast, in-memory analytical queries, particularly for data profiling and quick data quality assessments.
-   **Technologies**: DuckDB (embedded analytical database).
-   **Key Responsibilities**:
    -   Performing complex analytical operations on data subsets.
    -   Generating real-time data quality reports.

## 3. Data Flow

1.  **User Interaction**: Users interact with the **Frontend** to initiate actions (e.g., create project, add data source).
2.  **API Calls**: The **Frontend** makes authenticated API calls to the **Backend**.
3.  **Authentication**: The **Backend** validates user requests using **Clerk** for authentication and authorization.
4.  **Business Logic**: The **Backend** processes the request, applying business logic related to data quality management.
5.  **Data Persistence**: The **Backend** interacts with **PostgreSQL** for persistent storage of metadata and configurations.
6.  **Data Processing/Analytics**: For data profiling or complex analysis, the **Backend** may leverage **DuckDB** for efficient in-memory processing.
7.  **Response**: The **Backend** returns data to the **Frontend**.
8.  **Display**: The **Frontend** renders the data for the user.

## 4. Serverless Deployment Considerations

-   Both Frontend and Backend are designed to be deployed on serverless platforms (e.g., AWS Lambda/Vercel for Frontend, AWS Lambda/Google Cloud Run for Backend).
-   Stateless backend components where possible.
-   Efficient cold start times.
-   Scalability based on demand.
