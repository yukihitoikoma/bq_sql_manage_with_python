from google.cloud import bigquery

client = bigquery.Client()

# rollback - 10 minutes
QUERY = ('SELECT * FROM `dataset.table` FOR SYSTEM TIME AS OF TIMESTAMP_ADD(CURRENT_TIMESTAMP(), INTERVAL -10 MINUTE)')

query_job = client.query(QUERY)
rows = query_job.result()

for row in rows:
    print(row.name)