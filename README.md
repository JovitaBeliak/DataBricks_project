# Complete Data Lakehouse project built using Databricks and the Medallion Architecture.
Raw data is ingested and progressively transformed into clean, reliable, and business-ready datasets across Bronze, Silver, and Gold layers.

The solution includes end-to-end data processing, from ingestion to analytics-ready outputs, with automated orchestration using Databricks Workflows (Jobs) to execute the pipeline on a daily schedule.

### Architecture

This project follows the Medallion Architecture:

🥉 Bronze Layer

- Raw data ingestion from source systems
- Schema inference and storage in Delta Lake tables

🥈 Silver Layer

- Data cleaning and standardization
- Type casting and validation
- Handling missing and inconsistent values

🥇 Gold Layer

- Business-level transformations
- Dimensional data modeling (fact and dimension tables)
- Data prepared for BI, reporting, and analytics

⚙️ Orchestration

- Developed orchestration notebooks for Silver and Gold layers
- Implemented automated pipeline execution using Databricks Jobs
- Scheduled daily runs for end-to-end Bronze → Silver → Gold processing