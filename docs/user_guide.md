# User Guide: SaaS Data Quality and Cleansing Platform

This guide provides step-by-step instructions on how to use the SaaS Data Quality and Cleansing Platform.

## 1. Overview

This platform helps enterprises manage data quality and cleanse data during migrations from legacy systems to modern SaaS applications.

## 2. Getting Started

### 2.1. Accessing the Platform

Access the platform through your web browser at the provided URL.

### 2.2. Logging In

Use your credentials to log in to the platform.

## 3. Core Workflows

### 3.1. Creating a New Project

Projects are used to organize your data migration and cleansing efforts.

1.  Navigate to the 'Projects' dashboard.
2.  Click the 'New Project' button.
3.  Enter a descriptive name for your project (e.g., "Legacy CRM Migration").
4.  Click 'Create'.

### 3.2. Adding a Data Source

Data sources represent the systems from which you will extract data (legacy) or to which you will load data (SaaS).

1.  Within your selected project, navigate to the 'Data Sources' tab.
2.  Click the 'Add Data Source' button.
3.  Select the type of data source (e.g., 'Legacy Database', 'SaaS Application').
4.  Enter the required connection details (e.g., host, port, credentials, database name).
5.  Click 'Connect'. The platform will attempt to establish a connection and validate the details.

### 3.3. Running Data Profiling

Data profiling helps you understand the structure, content, and quality of your source data.

1.  From the 'Data Sources' tab, select a connected legacy data source.
2.  Click the 'Profile' button next to the data source name.
3.  The platform will initiate a data profiling job. You can monitor its progress in the 'Jobs' or 'Profiling' section.

### 3.4. Viewing Data Profiles

Once a data profiling job is complete, you can review the results to identify data quality issues.

1.  Navigate to the 'Profiles' tab within your project.
2.  Select the data profile you wish to view.
3.  Review the detailed report, which includes information on data types, completeness, uniqueness, patterns, and potential anomalies.

## 4. Next Steps (Beyond this Guide)

After profiling, you would typically proceed with:

-   **Data Cleansing & Standardization**: Applying rules to fix identified data quality issues.
-   **Data Mapping & Transformation**: Defining how data from your legacy system maps to the target SaaS application's schema.
-   **Data Validation**: Setting up rules to ensure data integrity throughout the migration process.
-   **Migration Execution**: Running the actual data migration.
