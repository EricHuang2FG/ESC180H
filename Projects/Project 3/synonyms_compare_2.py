import math
import time

def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    #print(f"v1 = {vec1}")
    #print(f"v2 = {vec2}")
    '''Returns the cosine similarity score of two vectors
    '''
    dot_sum = 0
    square_sum1 = 0
    square_sum2 = 0

    if len(vec1) != len(vec2): #if the vectors are not equal in length
        #find shortest and longest vec
        shortest_vec = vec1 if len(vec1)<len(vec2) else vec2
        longest_vec = vec2 if len(vec2)>len(vec1) else vec1
    else: #if the vectors are equal in length
        shortest_vec = vec1
        longest_vec = vec2

    #cimpute the dot product
    for key, value in shortest_vec.items(): #go through the shortest vector
        if key in longest_vec: # if the current key is in longest_vec
            dot_sum = dot_sum + shortest_vec[key]*longest_vec[key]

    #to find square_sum1
    for key, value in vec1.items():
        square_sum1 = square_sum1+ value**2

    #to find square_sum2
    for key, value in vec2.items():
        square_sum2 = square_sum2 + value**2

    return dot_sum/((square_sum1*square_sum2)**0.5)

#print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))


def build_semantic_descriptors(sentences):
    '''Returns a semantic descriptors dictionary
    '''
    dict = {}

    #sentences is a list of lists

    #iterate through each sentence in sentences
    for sentence in sentences:

        for i in range(len(sentence)): # loop through each word in sentence
            sentence[i] = sentence[i].lower() # lower case every word

    #iterate through each sentence in sentences
    for sentence in sentences:
        for word in range(len(sentence)): # loop through each word in each sentence
            if sentence[word] not in dict: # if the current word is not in the big dictionary
                dict[sentence[word]] = {} # make an empty dictionary in dict
            for word2 in range(len(sentence)): # for each pair of words in sentence
                if sentence[word2] not in dict[sentence[word]]:
                    if sentence[word] != sentence[word2]:
                        dict[sentence[word]][sentence[word2]] = 1
                elif sentence[word] != sentence[word2] and sentence.index(sentence[word]) == word and sentence.index(sentence[word2]) == word2:
                    #track index of first occurence, if current index is not it, then dont do this again
                    dict[sentence[word]][sentence[word2]] += 1
                #print(dict)
    return dict


test = [['file', 'two', 'has', 'two', 'sentences'],['this', 'is', 'file', 'three'],['file', 'three', 'has', 'three', 'sentences'],['this', 'is', 'the', 'third', 'sentence']]

#test = [["i", "am", "a", "sick", "man"],["i", "am", "a", "spiteful", "man"],["i", "am", "an", "unattractive", "man"],]
#print(build_semantic_descriptors(test))


def build_semantic_descriptors_from_files(filenames):
    '''Takes in a list a files and returns a dictionary of the semantic descriptors
    '''
    sentences = []
    words = []
    letters = []
    punc = [".", "!","?"]
    texts = ""
    for file in range(len(filenames)):

        #storing the text file in text
        text = open(filenames[file], "r", encoding = "latin1")

        #replacing punctuation and newlines
        text = text.read().lower()
        text = text.replace("\n", " ")
        text = text.replace(",", "")
        text = text.replace("-", "")
        text = text.replace("--", "")
        text = text.replace(":", "")
        text = text.replace(";", "")

        #getting rid of extra spaces
        while "  " in text:
            text = text.replace("  ", " ")
        texts += text+ " "


    texts = texts.replace(".","|").replace("!","|").replace("?","|").split("|")
    for iter in range(len(texts)):
        texts[iter] = texts[iter].split()
    return build_semantic_descriptors(texts)

#print(build_semantic_descriptors_from_files(files))


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    #print(word)
    #print(choices)
    #print(semantic_descriptors)

    high_sim = -10000
    best_choice = None
    for choice in choices:
        if choice in semantic_descriptors and word in semantic_descriptors:
            sim = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])
        else:
            sim = -1
        if sim > high_sim: #smaller index is returned
            high_sim = sim
            best_choice = choice
    #print(best_choice)
    return best_choice


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    text = open(filename, "r", encoding = "latin1")
    text = text.readlines() # list of lines in text file
    num = len(text) # number of elements in list text

    count = 0

    L = []
    for line in text:
        line = line.replace("\n", "")
        L.append(line.split(" "))

    for line in range(num):

        word = L[line][0]
        ans = L[line][1]
        choices = L[line][2:]
        actual = most_similar_word(word, choices, semantic_descriptors, similarity_fn)
        if actual == ans:
            count += 1

    perc = (count / num) * 100
    return perc

# def run_similarity_test(filename, semantic_descriptors, similarity_fn):
#
#     text = open(filename, "r", encoding = "latin1")
#     text = text.readlines()
#     num = len(text)
#     #text[num-1] = text[num-1] + "\n"
#     #print(text)
#     #first_space = None
#     #second_space = None
#     count = 0
#
#     for i in range(len(text)):
#         choices = []
#         #str = ""
#         line = text[i].split(" ")
#        line = line.replace("\n","")
#         word = line[0]
#         answer = line[1]
#         choices = line[2:len(line)+1]
#         best_word = most_similar_word(word, choices, semantic_descriptors, similarity_fn)
#         if best_word == answer:
#             count += 1
#     perc = (count / num) * 100
#     return perc
#
#     #text[num-1] = text[num-1] + "\n"
#     #print(text)


# start = time.time()
# sem = build_semantic_descriptors_from_files([r"C:\Users\selin\Downloads\syn_tests\syn_tests\warandpeacetest.txt",r"C:\Users\selin\Downloads\syn_tests\syn_tests\swann.txt"])

# print(f"time taken: {time.time()-start}")
# text = r"C:\Users\selin\Downloads\syn_tests\syn_tests\text.txt"

# score = run_similarity_test(text, sem, cosine_similarity)
# print(score)