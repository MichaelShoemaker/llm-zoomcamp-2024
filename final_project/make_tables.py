#may need to run pip install --upgrade pipenv
#and pipenv install --quiet  langchain langchain-community langchain-openai 
#first
import duckdb
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase

# Connect to a new DuckDB database file
conn = duckdb.connect('chicago_crime_data.duckdb')

# Read the Parquet file into a DuckDB table
conn.execute("CREATE TABLE chicago_crime AS SELECT * FROM read_parquet('ChicagoCrimeData20240627.parquet')")
# conn.execute("CREATE TABLE chicago_crime AS SELECT * FROM read_parquet('SunRiseSunSet2024.parquet')")

# Optionally, check if the data has been loaded correctly
print(conn.execute("SELECT * FROM chicago_crime LIMIT 5").fetchdf())

# Close the connection
conn.close()

# https://github.com/langchain-ai/langchain/discussions/20033