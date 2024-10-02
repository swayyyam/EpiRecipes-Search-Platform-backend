from opensearchpy import OpenSearch
import pandas as pd

def ingest_data():

    data = pd.read_csv('/home/swayam/Downloads/archive/epi_r.csv')

    client = OpenSearch(
        hosts=[{'host': 'localhost', 'port': 9200}],
        http_auth=('admin', 'admin')
    )

    index_name = 'epirecipes'

    index_mapping = {
        "mappings": {
            "properties": {
                "title": {"type": "text"},
                "rating": {"type": "float"},
                "calories": {"type": "float"},
                "protein": {"type": "float"},
                "fat": {"type": "float"},
                "sodium": {"type": "float"},
                "tags": {"type": "keyword"}
            }
        }
    }

    if not client.indices.exists(index=index_name):
        client.indices.create(index=index_name, body=index_mapping)
        print(f"Index '{index_name}' created successfully.")
    else:
        print(f"Index '{index_name}' already exists.")

    for idx, row in data.iterrows():
        document = {
            "title": row['title'],
            "rating": float(row['rating']), 
            "calories": float(row['calories']),
            "protein": float(row['protein']),
            "fat": float(row['fat']),
            "sodium": float(row['sodium']),
            "tags": [col for col in data.columns if row[col] == 1.0] or ['no_tags']  # Ensure not empty
        }

        print(f"Indexing document: {document}")

        try:
            client.index(index=index_name, id=idx, body=document)
        except Exception as e:
            print(f"Failed to index document ID {idx}: {e}")

    print("Data indexing completed.")

if __name__ == "__main__":
    ingest_data()
