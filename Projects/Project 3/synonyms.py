import math, re

def norm(vec) -> float:
    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)

def cosine_similarity(vec1, vec2) -> float:
    dot_product = 0
    for word, count in vec1.items():
        if word in vec2:
            dot_product += count * vec2[word]
    return dot_product / (norm(vec1) * norm(vec2))

def build_semantic_descriptors(sentences) -> dict:
    semantic_descriptors = {}
    for sentence in sentences:
        sentence = list(set(sentence))
        for word_key in sentence:
            if not word_key:
                continue
            if word_key not in semantic_descriptors:
                semantic_descriptors[word_key] = {}
            for neighbour_word in sentence:
                if neighbour_word != word_key and neighbour_word:
                    if neighbour_word not in semantic_descriptors[word_key]:
                        semantic_descriptors[word_key][neighbour_word] = 1
                    else:
                        semantic_descriptors[word_key][neighbour_word] += 1
    return semantic_descriptors

def build_semantic_descriptors_from_files(filenames) -> dict:
    all_text = ""
    for file in filenames:
        with open(file, "r", encoding="latin1") as f:
            all_text += f.read()
    for punc in [",", "-", "--", ":", ";"]:
        all_text = all_text.replace(punc, "")
    all_text = re.sub(r"\n+", " ", all_text)
    all_text = all_text.replace("?", ".").replace("!", ".").split(".")
    all_text = [[w.lower() for w in sentence.split(" ")] for sentence in all_text]
    return build_semantic_descriptors(all_text)

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    pass

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass

if __name__ == "__main__":
    # vec2 = {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1, "unattractive": 1}
    # vec1 = {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1}
    # print(cosine_similarity(vec1, vec2))
    # sentences = [["i", "am", "a", "sick", "man"],
    # ["i", "am", "a", "spiteful", "man"],
    # ["i", "am", "an", "unattractive", "man"],
    # ["i", "believe", "my", "liver", "is", "diseased"],
    # ["however", "i", "know", "nothing", "at", "all", "about", "my",
    # "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]
    # print(build_semantic_descriptors(sentences)['man'])
    print(build_semantic_descriptors_from_files(["test.txt", "test2.txt"]))
