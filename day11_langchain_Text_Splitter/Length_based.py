from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('day11_langchain_Text_Splitter/dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap= 0,
    separator=''
)

result = splitter.split_documents(docs)

print(len(result))
print(result[1].page_content)