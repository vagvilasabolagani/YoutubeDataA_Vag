## Project Overview
This project aims to securely manage, streamline, and perform analysis on the structured and semi-structured YouTube videos data based on the video categories and the trending metrics.

## Project Goals
1. **Data Ingestion**: Build a mechanism to ingest data from different sources.
2. **ETL System**: Transform raw data into the proper format.
3. **Data Lake**: Establish a centralized repository to store data from multiple sources.
4. **Scalability**: Ensure the system scales effectively with increasing data size.
5. **Cloud**: Utilize AWS cloud services for processing vast amounts of data.
6. **Reporting**: Develop a dashboard for insights and analysis.

## Services Used
- **Amazon S3**: Object storage service for manufacturing scalability, data availability, security, and performance.
- **AWS IAM**: Identity and Access Management for secure access to AWS services and resources.
- **Amazon QuickSight**: Scalable, serverless, machine learning-powered business intelligence (BI) service.
- **AWS Glue**: Serverless data integration service for discovering, preparing, and combining data.
- **AWS Lambda**: Computing service for running code without managing servers.
- **AWS Athena**: Interactive query service for S3 data without loading it into a database.

## Dataset
This project utilizes a Kaggle dataset containing statistics (CSV files) on daily popular YouTube videos over several months. Each region has its own file with data on up to 200 trending videos published daily. Data includes video title, channel title, publication time, tags, views, likes, dislikes, description, comment count, and category_id field specific to each region.
                    https://www.kaggle.com/datasets/datasnaek/youtube-new

## File Descriptions
- `data_ingestion_etl.py`: Python script for data ingestion and ETL process using AWS Glue.
- `analysis_and_reporting.py`: Python script for analyzing data and generating reports.
- `README.md`: Project documentation and instructions.
- `requirements.txt`: List of required Python packages for the project.
- `aws_glue_job_script.py`: AWS Glue job script for data processing.
- `dashboard_creation.ipynb`: Jupyter notebook for creating interactive dashboards using Amazon QuickSight.

## Usage
1. **Data Ingestion and ETL**:
   - Run `data_ingestion_etl.py` to ingest and transform raw data into the proper format.
   - Utilize AWS Glue to execute the ETL process at scale.

2. **Analysis and Reporting**:
   - Execute `analysis_and_reporting.py` for analyzing data and generating insights.
   - Create interactive dashboards using `dashboard_creation.ipynb` and Amazon QuickSight.

## Setup Instructions
1. Clone the repository to your local machine.
2. Install required Python packages using `pip install -r requirements.txt`.
3. Configure AWS IAM roles and permissions for accessing AWS services.
4. Update AWS Glue job script (`aws_glue_job_script.py`) with appropriate configurations.
5. Execute the scripts as per project requirements.

