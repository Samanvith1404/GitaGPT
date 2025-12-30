import weaviate
from weaviate.connect import ConnectionParams

client_db=weaviate.WeaviateClient(
    connection_params=ConnectionParams.from_url(
        "http://localhost:8081/v1/meta",
        grpc_port=50051
    )
)

client_db.connect()
gita=client_db.collections.get('Bhagavath_gita')

def retriever(output):
    relevant_docs=[]

    for i in output:
        a=gita.query.near_text(
            query=i['retrieval_query'],
            certainty=0.6,
            limit=3
        )
        relevant_docs.append(a)
    return relevant_docs