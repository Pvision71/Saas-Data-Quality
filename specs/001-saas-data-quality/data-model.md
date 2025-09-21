# Data Model

This document defines the key data entities for the platform, based on the feature specification.

## Project
Represents a single migration initiative.
- `id`: UUID (Primary Key)
- `name`: String
- `created_at`: Timestamp
- `updated_at`: Timestamp

## DataSource
Connection details for a source or target system.
- `id`: UUID (Primary Key)
- `project_id`: UUID (Foreign Key to Project)
- `name`: String
- `type`: Enum (e.g., 'legacy_db', 'saas_app')
- `connection_details`: JSONB (encrypted)

## DataProfile
The output of the profiling process.
- `id`: UUID (Primary Key)
- `datasource_id`: UUID (Foreign Key to DataSource)
- `status`: Enum (e.g., 'running', 'completed', 'failed')
- `results`: JSONB
- `created_at`: Timestamp

## CleansingRule
A configurable rule for data cleansing.
- `id`: UUID (Primary Key)
- `project_id`: UUID (Foreign Key to Project)
- `name`: String
- `description`: Text
- `implementation`: JSONB (e.g., details of the cleansing algorithm)

## Mapping
The visual mapping between source and target schemas.
- `id`: UUID (Primary Key)
- `project_id`: UUID (Foreign Key to Project)
- `source_datasource_id`: UUID (Foreign Key to DataSource)
- `target_datasource_id`: UUID (Foreign Key to DataSource)
- `mapping_details`: JSONB

## User
A user of the platform.
- `id`: String (from Clerk)
- `organization_id`: UUID
- `role`: Enum (e.g., 'admin', 'editor', 'viewer')
