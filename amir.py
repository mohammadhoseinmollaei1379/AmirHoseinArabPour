from weaviate import WeaviateClient
from weaviate.connect import ConnectionParams

client = WeaviateClient(
    connection_params=ConnectionParams.from_url(
        url="http://127.0.0.1:8080",
        grpc_port=50051  # اگر gRPC فعال است
    )
)

client.connect()
print("Connected:", client.is_ready())