import awswrangler as wr
import pandas as pd
import urllib.parse
import os

# Environment variables
s3_cleansed_layer = os.environ.get('s3_cleansed_layer')
glue_catalog_db_name = os.environ.get('glue_catalog_db_name')
glue_catalog_table_name = os.environ.get('glue_catalog_table_name')
write_data_operation = os.environ.get('write_data_operation')

def lambda_handler(event, context):
    # Get the object from the event and extract bucket name and key
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    try:
        # Read JSON content from S3 into a DataFrame
        df_raw = wr.s3.read_json(f's3://{bucket}/{key}')

        # Extract required columns
        df_step_1 = pd.json_normalize(df_raw['items'])

        # Write to S3 in Parquet format and update Glue catalog
        wr.s3.to_parquet(
            df=df_step_1,
            path=s3_cleansed_layer,
            dataset=True,
            database=glue_catalog_db_name,
            table=glue_catalog_table_name,
            mode=write_data_operation
        )

        return "Data processing completed successfully"
    except Exception as e:
        print(f"Error processing object {key} from bucket {bucket}: {e}")
        raise e
