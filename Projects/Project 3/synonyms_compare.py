import math
import re
import time

def cosine_similarity(vec1, vec2):
    dot = sum(vec1[key] * vec2[key] for key in vec1 if key in vec2)
    return dot / math.sqrt(sum(value ** 2 for value in vec1.values()) * sum(value ** 2 for value in vec2.values()))

def build_semantic_descriptors(sentences):
    d = {}
    for sentence in sentences:
        unique_words = {}
        for word in sentence:
            word_lower = word.lower()
            unique_words[word_lower] = 1
        for word in unique_words:
            if word not in d:
                d[word] = {}
            for other_word in unique_words:
                if word != other_word:
                    if other_word in d[word]:
                        d[word][other_word] += 1
                    else:
                        d[word][other_word] = 1
    return d

def build_semantic_descriptors_from_files(filenames):
    s = ""
    for file in filenames:
        with open(file, "r", encoding="utf-8") as f:
            s += f.read() + "."
    s = re.sub(r'[.!?]', '|', s.replace('\n',' ')).split('|')
    for sentence in range(len(s)):
        s[sentence] = re.sub(r'[^a-zA-Z\s]', '', s[sentence]).split()
    # return build_semantic_descriptors(s)
    hi = build_semantic_descriptors(s)
    return hi
# IF WORD IS NOT IN SEMANTIC DESCRIPTORS, WHAT DO I DO???? RETURN NONE OR FIRST CHOICE?
def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    max_score, max_word = -2, ""
    a = semantic_descriptors.get(word, None)
    for choice in choices:
        b = semantic_descriptors.get(choice, None)
        score = similarity_fn(a, b) if a and b else -1
        if score > max_score:
            max_score = score
            max_word = choice
    return max_word

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    questions = open(filename, "r", encoding="utf-8").readlines()
    for i in range(len(questions)):
        questions[i] = questions[i].split()
    count = 0
    for question in questions:
        count += most_similar_word(question[0], question[2:], semantic_descriptors, similarity_fn) == question[1]
    return 100 * count / len(questions)

def norm(vec):
    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    return math.sqrt(sum_of_squares)

# start = time.time()
# sem = build_semantic_descriptors_from_files(["aayush_smart_train.txt"])
# print(f"sem = {sem}")
# print(f"time taken: {time.time() - start}")
#
# score = run_similarity_test("input.txt", sem, cosine_similarity)
# print(score)