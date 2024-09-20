import math

def compute_idf(corpus, term):
    total_docs = len(corpus)
    docs_with_term = sum([1 for doc in corpus if term in doc])
    idf = math.log(total_docs / (docs_with_term + 1))  # Add 1 to avoid division by zero
    return idf


corpus = [
    "the quick brown fox",
    "the lazy dog",
    "the fox jumps over the dog",
    "the fox is clever"
]

term = "fox"

idf_value = compute_idf(corpus, term)
print(f"IDF of term '{term}': {idf_value}")
