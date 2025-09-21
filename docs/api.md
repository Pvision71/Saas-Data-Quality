# API Documentation

This document provides an overview of the SaaS Data Quality API.

## Info
- **Title**: SaaS Data Quality API
- **Version**: 1.0.0

## Paths

### GET /projects
- **Summary**: List all projects
- **Responses**:
  - **200**: A list of projects
    - **Schema**: Array of `Project` objects

### POST /projects/{projectId}/datasources
- **Summary**: Create a new data source
- **Parameters**:
  - `projectId` (path): Required, string
- **Request Body**:
  - **Content**: `DataSource` object
- **Responses**:
  - **201**: Data source created

## Schemas

### Project
- **Type**: object
- **Properties**:
  - `id`: string (uuid format)
  - `name`: string

### DataSource
- **Type**: object
- **Properties**:
  - `name`: string
  - `type`: string
