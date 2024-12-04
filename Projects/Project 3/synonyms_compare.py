import math

def norm(vec):
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)

def cosine_similarity(vec1, vec2):
    pass

def build_semantic_descriptors(sentences):
    pass

def build_semantic_descriptors_from_files(filenames):
    pass

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    pass

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass
