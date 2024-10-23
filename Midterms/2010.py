def longest_sequence(search_str, ch):
    max_length = 0
    for i, value in enumerate(search_str):
        if value == ch:
            count = 0
            for j in range(i, len(search_str)):
                if search_str[j] == ch:
                    count += 1
                else:
                    break
            if count > max_length:
                max_length = count
    return max_length

if __name__ == "__main__":
    pass
