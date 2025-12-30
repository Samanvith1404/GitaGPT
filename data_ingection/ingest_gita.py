import os
import weaviate
from weaviate.connect import ConnectionParams
from weaviate.classes.config import Property, Configure, DataType

client_db = weaviate.WeaviateClient(
    connection_params=ConnectionParams.from_url(
        "http://localhost:8081/v1/meta",
        grpc_port=50051
    )
)

client_db.connect()

client_db.collections.create(
    name="Bhagavath_gita",
    vectorizer_config=Configure.Vectorizer.text2vec_transformers(),
    properties=[
        Property(name="text", data_type=DataType.TEXT),
        Property(name="content", data_type=DataType.TEXT),
    ]
)

docs = client_db.collections.get("Bhagavath_gita")

def insert_data(data: dict):
    docs.data.insert(data)

for folder in os.listdir():
    if os.path.isdir(folder):
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                with open(file_path, encoding="utf-8") as f:
                    text = f.read()

                data = {
                    "content": os.path.splitext(file)[0],
                    "text": text
                }

                insert_data(data)
