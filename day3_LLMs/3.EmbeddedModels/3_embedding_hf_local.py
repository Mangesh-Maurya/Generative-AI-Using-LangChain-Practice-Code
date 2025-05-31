from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = ["Delhi is the capital of India",
             "Kolkata is the capital of west bengal"
             "Paris is the capital od the france"]

vector = embedding.embed_documents(documents)

print(str(vector))