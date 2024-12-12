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
        sentence = [i for i in sentence if i]
        # print(sentence)
        for word_key in sentence:
            word_key = word_key.lower()
            if not word_key: 
                continue
            if word_key not in semantic_descriptors:
                semantic_descriptors[word_key] = {}
            for neighbour_word in sentence:
                neighbour_word = neighbour_word.lower()
                if neighbour_word != word_key and neighbour_word:
                    if neighbour_word not in semantic_descriptors[word_key]:
                        semantic_descriptors[word_key][neighbour_word] = 1
                    else:
                        semantic_descriptors[word_key][neighbour_word] += 1
    semantic_descriptors = {key: value for key, value in semantic_descriptors.items() if value}
    return semantic_descriptors

def build_semantic_descriptors_from_files(filenames) -> dict:
    all_text = ""
    for file in filenames:
        with open(file, "r", encoding="utf-8") as f:
            all_text += f.read() + ". "
    for punc in [",", "-", "--", ":", ";"]:
        all_text = all_text.replace(punc, " ")
    all_text = re.sub(r"\n+", " ", all_text)
    all_text = all_text.replace("?", ".").replace("!", ".").replace("(", "").replace(")", "").split(".")
    all_text = [[w.lower().strip() for w in sentence.split(" ")] for sentence in all_text]
    return build_semantic_descriptors(all_text)

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    most_similar_word, most_similar_similarity = "", -2
    for choice in choices:
        if choice in semantic_descriptors and word in semantic_descriptors:
            similarity = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])
        else:
            similarity = -1
        if similarity > most_similar_similarity:
            most_similar_word = choice
            most_similar_similarity = similarity
    return most_similar_word

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    total, correct = 0, 0
    with open(filename, "r", encoding="latin1") as f:
        for line in f:
            line = line.replace("\n", "").split(" ")
            most_similar = most_similar_word(line[0], line[2:], semantic_descriptors, similarity_fn)
            if most_similar == line[1]:
                correct += 1
            total += 1
    return (correct / total) * 100

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
    # vecs = {'a1':{'a2':1,'a3':2},'a4':{'a2':2,'a3':1},'a5':{'a2':4,'a3':4}}
    # choices = ['blah','a4','a5']
    # word = 'a1'
    # print(most_similar_word(word, choices, vecs, cheb_sim))
    filename = "test.txt"
    semantic_descriptors = build_semantic_descriptors_from_files(["war_and_peace.txt", "swanns_way.txt"])
    print(run_similarity_test(filename, semantic_descriptors, cosine_similarity))
