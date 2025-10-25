from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
# Step 1: Load model baraye tabdil matn be vector
model = SentenceTransformer('all-MiniLM-L6-v2')
# Step 2: Soalhaye portekraar (FAQ)
faq = [
    "Chetor az database backup begiram?",
    "Raveshhaye afzayeshe amniyate database",
    "Chetor database ro be Excel vasl konam?",
    "Chegoone database ra ramzgozari konim?",
    "Fargh beyn SQL va NoSQL chist?",
    "Chetor az hack shodane database jelogiri konam?",
    "Chegoone dastrasiye karbaran ra mahdood konim?",
    "Chetor loggiri az database anjam bedim?",
    "Chegoone database ra be soorate amn be internet vasl konim?",
    "Chetor ramze oboor database ra ghavi-tar konim?"]
# Step 3: Tabdile soalha be vector
faq_vectors = model.encode(faq)
faq_vectors = np.array(faq_vectors)
# Step 4: Sakhte database bardari ba FAISS
dimension = faq_vectors.shape[1]  # tedade ab'ad
index = faiss.IndexFlatL2(dimension)
index.add(faq_vectors)  # type: ignore
# Step 5: Soale jadid baraye search
query = "Chetor az hack shodane database jelogiri konam?"
query_vector = model.encode([query])
query_vector = np.array(query_vector)
# Step 6: Peyda kardane nazdiktarin soal
D, I = index.search(query_vector, k=1)  # type: ignore
print("Soale voroodi:", query)
print("Nazdiktarin soal:", faq[I[0][0]])
print("Fasele:", D[0][0])