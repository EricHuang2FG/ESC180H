from synonyms import (
    norm,
    cosine_similarity,
    build_semantic_descriptors,
    build_semantic_descriptors_from_files,
    most_similar_word,
    run_similarity_test
)
import synonyms_compare as test
import random

suceeded_test_count, failed_test_count = 0, 0

def assert_test_result(description: str, output_a: str, output_b: str, f) -> None:
    global suceeded_test_count, failed_test_count
    s = f"Description: {description}\nLocal output: {output_a}\nCompared output: {output_b}\nComparison "
    if output_a == output_b:
        suceeded_test_count += 1
        s += "SAME OUTPUT ✅✅✅✅✅✅\n\n\n"
    else:
        failed_test_count += 1
        s += "DIFFERENT OUTPUT ❌❌❌❌❌\n\n\n"
    f.write(s)

def test_semantic_descriptors(f):
    files = ["swanns_way.txt", "war_and_peace.txt"]
    local_sd = build_semantic_descriptors_from_files(files)
    compared_sd = test.build_semantic_descriptors_from_files(files)
    
    f.write(f"\n\n\n{'-' * 20}COMPARING SEMANTIC DESCRIPTORS DICTIONARY BUILDING{'-' * 20}\n\n")
    for key, value in local_sd.items():
        description = f"Comparing the semantic descriptors for the word {key}"
        if key in compared_sd.keys():
            assert_test_result(description, value, compared_sd[key], f)
        else:
            assert_test_result(description, value, "Word D.N.E", f)
    return local_sd, compared_sd # tests the rest with the same semantic descriptor

def test_most_similar_word(sd, f):
    words_arr = list(sd.keys())

    f.write(f"\n\n\n{'-' * 20}COMPARING DETERMINING THE MOST SIMILAR WORD{'-' * 20}\n\n")
    for _ in range(1000):
        target_word = words_arr[random.randint(0, len(words_arr) - 1)]
        start = random.randint(0, len(words_arr) - 2)
        choices = words_arr[start + 1: random.randint(start + 2, len(words_arr) - 1)]
        assert_test_result(
            "Testing most_similar_word()", 
            most_similar_word(target_word, choices, sd, cosine_similarity),
            test.most_similar_word(target_word, choices, sd, test.cosine_similarity),
            f
        )

def test_run_similarity_test(local_sd, compared_sd, f):
    # this test only run "once" since it's not randomized

    f.write(f"\n\n\n{'-' * 20}COMPARING RUNNING SIMILARITY TEST{'-' * 20}\n\n")
    for sd in [local_sd, compared_sd]:
        assert_test_result(
            "Testing run_similarity_test()",
            run_similarity_test("test.txt", sd, cosine_similarity),
            test.run_similarity_test("test.txt", sd, test.cosine_similarity),
            f
        )

if __name__ == "__main__":
    with open("results.txt", "w", encoding="utf-8") as f:
        local_sd, compared_sd = test_semantic_descriptors(f)
        test_most_similar_word(local_sd, f)
        test_run_similarity_test(local_sd, compared_sd, f)
