import urllib.request, urllib.parse

def problem_3():
    with open("data2.txt") as f:
        for line in f:
            if "lol" in line.lower():
                print(line.strip())

def problem_4():
    def dict_to_str(d):
        out = ""
        for key, value in d.items():
            out += f"{key}, {value}\n"
        return out[:-1]
    print(dict_to_str({1: 2, 5: 6}))

def problem_5():
    def dict_to_str_sorted(d):
        keys = list(d.keys())
        keys.sort()
        out = ""
        for key in keys:
            out += f"{key}, {d[key]}\n"
        return out[:-1]
    print(dict_to_str_sorted({1: 2, 0: 3, 10: 5}))

def problem_6():
    def top10(L):
        L = L.copy()
        L.sort()
        return L[len(L) - 10:] if len(L) >= 10 else L
    
    all_words, word_counts = [], {}
    with open("text.txt", encoding="latin-1") as f:
        all_words = f.read().split()
    all_words = [string.lower() for string in all_words]
    for word in all_words:
        if word not in word_counts.keys():
            word_counts[word] = all_words.count(word)

    word_counts = sorted(word_counts.items(), key=lambda i: i[1], reverse=True)
    out = []
    for pair in word_counts:
        out.append(pair[0])
        if len(out) == 10:
            break
    print(out)

def problem_8():
    def choose_variant(variants):
        tally = {}
        for search_term in variants:
            orig_search_term = search_term
            url = "https://ca.search.yahoo.com/search;_ylt=AwrEo7g66DRn8wEAyq_rFAx.;_ylc=X1MDMjExNDcyMTAwMwRfcgMyBGZyA3lmcC10LTcxNQRmcjIDc2ItdG9wBGdwcmlkA0RQZE1HX0VFU2RDWVFtVEVQLnlJVUEEbl9yc2x0AzAEbl9zdWdnAzEwBG9yaWdpbgNjYS5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAMxOQRxdWVyeQNlbmdpbmVlcmluZyUyMHNjaWVuY2UEdF9zdG1wAzE3MzE1MjA1Mzk-?p=engineering+science&fp=1&fr=yfp-t-715&fr2=sb-top"
            url = url.split("?p=")
            search_term = search_term.split(" ")
            search_term = "+".join(search_term)
            url[1] = search_term
            url = "?p=".join(url)
            f = urllib.request.urlopen(url)
            page = f.read().decode("utf-8")
            f.close()

            page_split = page.split('<span style="color:inherit;" class="fz-14 lh-22">About ')
            num = int(page_split[1].split(" ")[0].replace(",", ""))
            if orig_search_term not in tally.keys():
                tally[orig_search_term] = num
        tally = sorted(tally.items(), key=lambda i: i[1])
        print(tally)
        return f"Variant that appears the most frequent: {tally[-1][0]}"
    print(choose_variant(["ANDREW", "ERIC", "eng sci"]))

def problem_9():
    # parsing CCC results haha
    tally = {}
    with open("2024CCCResults.txt") as f:
        for line in f:
            line = line.strip()
            i = 0
            for index, word in enumerate(line.split(" ")):
                if word.upper() != word:
                    i = index
                    break
            school = line.split(" ")[i:]
            school = " ".join(school)
            if school in tally.keys():
                tally[school] += 1
            else:
                tally[school] = 1
    tally = sorted(tally.items(), key=lambda i: i[1], reverse=True)
    for pair in tally:
        print(f"{pair[0]}: {pair[1]}")

if __name__ == "__main__":
    problem_3()
    problem_4()
    problem_5()
    problem_6()
    problem_8()
    problem_9()
