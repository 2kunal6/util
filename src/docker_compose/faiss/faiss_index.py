from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

class FAISSindex:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.db = FAISS.load_local('faiss_index', HuggingFaceEmbeddings(),
                                      allow_dangerous_deserialization=True)

        return cls._instance

    def search_similar_docs(self, query, n_results):
        return self.db.similarity_search(query, n_results)
