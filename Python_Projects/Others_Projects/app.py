from weaviate import WeaviateClient
from weaviate.connect import ConnectionParams
from weaviate.classes.config import Property, DataType

# --- Step 1: اتصال به Weaviate لوکال ---
# توجه: باید Weaviate روی پورت 8080 (REST) و 50051 (gRPC) در حال اجرا باشه
client = WeaviateClient(
    connection_params=ConnectionParams.from_url(
        url="http://127.0.0.1:8080",
        grpc_port=50051
    )
)

print("Connected:", client.is_ready())  # باید True باشه

# --- Step 2: پاک کردن کالکشن‌های قبلی و ساخت کالکشن جدید ---
client.collections.delete_all()

faq_collection = client.collections.create(
    name="FAQ",
    properties=[
        Property(name="question", data_type=DataType.TEXT),
        Property(name="answer", data_type=DataType.TEXT),
    ]
)

# --- Step 3: اضافه کردن داده‌ها ---
faq_data = [
    {"question": "Chetor az database backup begiram?", 
     "answer": "Ba estefade az dastoor BACKUP ya tool haye backup."},

    {"question": "Raveshhaye afzayeshe amniyate database", 
     "answer": "Estefade az ramzgozari, dastresi mahdood, va firewall."},

    {"question": "Chetor database ro be Excel vasl konam?", 
     "answer": "Ba estefade az ODBC driver ya export CSV."},

    {"question": "Chegoone database ra ramzgozari konim?", 
     "answer": "Ba estefade az Transparent Data Encryption (TDE)."},

    {"question": "Fargh beyn SQL va NoSQL chist?", 
     "answer": "SQL relational ast, NoSQL flexible va schema-less."}
]

for item in faq_data:
    faq_collection.data.insert(properties=item)

# --- Step 4: جستجوی معنایی ---
query = "Chetor amniyate database ro bala bebaram?"

result = faq_collection.query.near_text(
    query=query,
    limit=1,
    return_properties=["question", "answer"]
)

# --- Step 5: نمایش نتیجه ---
print("Soale voroodi:", query)
print("Nazdiktarin soal:", result.objects[0].properties["question"])
print("Pasokh:", result.objects[0].properties["answer"])
