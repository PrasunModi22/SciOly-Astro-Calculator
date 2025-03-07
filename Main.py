import os
import math
import re
from collections import Counter
from typing import List, Dict, Tuple, Optional
import pickle


class BM25Retriever:
    
    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.corpus = []
        self.doc_lengths = []
        self.avgdl = 0
        self.term_frequencies = []
        self.doc_freqs = Counter()
        self.N = 0
        self.idf = {}
        self.doc_paths = []
        
    def _tokenize(self, text: str) -> List[str]:
        text = text.lower()
        return re.findall(r'\w+', text)
    
    def index_directory(self, directory_path: str, file_extensions: List[str] = ['.txt', '.md', '.pdf', '.docx']) -> None:
        self.doc_paths = []
        documents = []
        
        for root, _, files in os.walk(directory_path):
            for file in files:
                if any(file.endswith(ext) for ext in file_extensions):
                    file_path = os.path.join(root, file)
                    try:
                        if file.endswith('.txt') or file.endswith('.md'):
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read()
                        else:
                            print(f"Skipping {file_path} - Need additional libraries for this file type")
                            continue
                            
                        documents.append(content)
                        self.doc_paths.append(file_path)
                    except Exception as e:
                        print(f"Error processing {file_path}: {e}")
        
        self.index_documents(documents)
                
    def index_documents(self, documents: List[str]) -> None:
        self.corpus = []
        self.term_frequencies = []
        self.doc_freqs = Counter()
        self.doc_lengths = []
        
        # Process and tokenize each document
        for doc in documents:
            tokenized_doc = self._tokenize(doc)
            self.corpus.append(tokenized_doc)
            
            # Calculate term frequencies for the document
            term_freq = Counter(tokenized_doc)
            self.term_frequencies.append(term_freq)
            
            # Update document frequencies
            self.doc_freqs.update(set(tokenized_doc))
            
            # Store document length
            self.doc_lengths.append(len(tokenized_doc))
        
        self.N = len(self.corpus)
        self.avgdl = sum(self.doc_lengths) / self.N if self.N > 0 else 0
        
        # Calculate IDF for all terms
        self._calculate_idf()
    
    def _calculate_idf(self) -> None:
        self.idf = {}
        for term, doc_freq in self.doc_freqs.items():
            # BM25 IDF formula
            self.idf[term] = math.log((self.N - doc_freq + 0.5) / (doc_freq + 0.5) + 1.0)
    
    def search(self, query: str, top_k: int = 5) -> List[Tuple[int, float, str]]:
        if self.N == 0:
            return []
            
        query_tokens = self._tokenize(query)
        scores = [0.0] * self.N
        
        for token in query_tokens:
            if token not in self.idf:
                continue
                
            q_idf = self.idf[token]
            
            for doc_id, term_freqs in enumerate(self.term_frequencies):
                if token not in term_freqs:
                    continue
                    
                # BM25 scoring formula
                freq = term_freqs[token]
                doc_len = self.doc_lengths[doc_id]
                numerator = q_idf * freq * (self.k1 + 1)
                denominator = freq + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
                scores[doc_id] += numerator / denominator
        
        # Sort results by score
        results = [(i, score, self.doc_paths[i]) for i, score in enumerate(scores) if score > 0]
        results.sort(key=lambda x: x[1], reverse=True)
        
        return results[:top_k]
    
    def get_document_snippet(self, doc_id: int, query: str, window_size: int = 200) -> str:
        if doc_id >= self.N:
            return ""
            
        try:
            with open(self.doc_paths[doc_id], 'r', encoding='utf-8', errors='ignore') as f:
                doc_text = f.read()
                
            # Find the first location of query terms
            query_tokens = set(self._tokenize(query))
            doc_tokens = self._tokenize(doc_text)
            
            # Find the position with highest concentration of query terms
            best_position = 0
            max_matches = 0
            
            for i in range(len(doc_tokens)):
                if i + window_size // 10 > len(doc_tokens):
                    break
                    
                matches = sum(1 for j in range(window_size // 10) 
                           if i + j < len(doc_tokens) and doc_tokens[i + j] in query_tokens)
                           
                if matches > max_matches:
                    max_matches = matches
                    best_position = i
            
            # Try to find the actual text position corresponding to the token position
            char_position = 0
            tokens_found = 0
            for i, char in enumerate(doc_text.lower()):
                if re.match(r'\w', char):
                    if tokens_found == best_position:
                        char_position = i
                        break
                    continue
                else:
                    if i > 0 and re.match(r'\w', doc_text.lower()[i-1]):
                        tokens_found += 1
                    if tokens_found == best_position:
                        char_position = i
                        break
            
            # Extract the snippet
            start = max(0, char_position - window_size // 2)
            end = min(len(doc_text), char_position + window_size // 2)
            
            snippet = doc_text[start:end]
            
            # Add ellipsis if needed
            if start > 0:
                snippet = "..." + snippet
            if end < len(doc_text):
                snippet = snippet + "..."
                
            return snippet
            
        except Exception as e:
            return f"Error retrieving snippet: {e}"
    
    def save_index(self, file_path: str) -> None:
        index_data = {
            'k1': self.k1,
            'b': self.b,
            'corpus': self.corpus,
            'doc_lengths': self.doc_lengths,
            'avgdl': self.avgdl,
            'term_frequencies': self.term_frequencies,
            'doc_freqs': self.doc_freqs,
            'N': self.N,
            'idf': self.idf,
            'doc_paths': self.doc_paths
        }
        
        with open(file_path, 'wb') as f:
            pickle.dump(index_data, f)
            
    def load_index(self, file_path: str) -> None:
        with open(file_path, 'rb') as f:
            index_data = pickle.load(f)
            
        self.k1 = index_data['k1']
        self.b = index_data['b']
        self.corpus = index_data['corpus']
        self.doc_lengths = index_data['doc_lengths']
        self.avgdl = index_data['avgdl']
        self.term_frequencies = index_data['term_frequencies']
        self.doc_freqs = index_data['doc_freqs']
        self.N = index_data['N']
        self.idf = index_data['idf']
        self.doc_paths = index_data['doc_paths']


# Example usage
if __name__ == "__main__":
    # Create and initialize the retriever
    retriever = BM25Retriever(k1=1.5, b=0.75)
    
    # Index documents in a directory
    documents_dir = "./documents"
    retriever.index_directory(documents_dir)
    
    # Save the index
    retriever.save_index("bm25_index.pkl")
    
    # Load the index (for later use)
    # retriever.load_index("bm25_index.pkl")
    
    # Search for documents
    query = input("Query: ")
    results = retriever.search(query, top_k=3)
    
    # Print results
    for doc_id, score, doc_path in results:
        print(f"Document: {doc_path}")
        print(f"Score: {score:.4f}")
        snippet = retriever.get_document_snippet(doc_id, query)
        print(f"Snippet: {snippet[:200]}...\n")