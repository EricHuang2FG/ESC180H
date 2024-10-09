import random

def problem_1(L):
    def count_evens(L):
        count = 0
        for num in L:
            if num % 2 == 0:
                count += 1
        return count
    print(count_evens(L))

def problem_2(lis):
    def list_to_str(lis):
        string = "["
        for c in lis:
            if isinstance(c, str):
                string += f"\'{c}\', "
            else:
                string += f"{c}, "
        return f"{string[:-2]}]"
    print(list_to_str(lis))

def problem_3(list1, list2):
    def lists_are_the_same(list1, list2):
        if len(list1) != len(list2):
            return False
        for index, value in enumerate(list1):
            if value != list2[index]:
                return False
        return True
    print(lists_are_the_same(list1, list2))

def problem_4(list1, list2):
    def list1_start_with_list2(list1, list2):
        if len(list1) < len(list2):
            return False
        for index, value in enumerate(list2):
            if value != list1[index]:
                return False
        return True
    print(list1_start_with_list2(list1, list2))

def problem_5(list1, list2):
    def match_pattern(list1, list2):
        if len(list1) < len(list2): 
            return False
        start = 0
        try:
            while start < len(list1):
                i = list1.index(list2[0], start)
                start = i + 1
                for j in range(i, i + len(list2)):
                    if j >= len(list1):
                        return False
                    if list1[j] != list2[j - i]:
                        break
                    if j - i == len(list2) - 1 and list1[j] == list2[j - i]:
                        return True
            return False
        except ValueError:
            return False
    print(match_pattern(list1, list2))

def problem_6(list0):
    def duplicates(list0):
        if len(set(list0)) == len(list0):
            return False
        for i in range(len(list0) - 1):
            if list0[i] == list0[i + 1]:
                return True
        return False
    print(duplicates(list0))

def problem_7(x, i):
    x = [i + 0.1 * random.random() for i in x]
    def method_1(x, i):
        # assume lenth of x must be greater than or equal to 4
        if i == 0:
            a = (x[i + 1] - x[i]) / 0.1
            b = (x[i + 2] - x[i]) / 0.2
            return (2 * a + b) / 3
            # return ((2 * x[i + 1] + 1 * x[i + 2]) / 3) / 0.1
        if i == 1:
            a1 = (x[i + 1] - x[i]) / 0.1
            a2 = (x[i] - x[i - 1]) / 0.1
            b = (x[i + 2] - x[i]) / 0.2
            return (2 * a1 + 2 * a2 + b) / 5
            # return ((2 * x[i + 1] + 2 * x[i - 1] + 1 * x[i + 2]) / 5) / 0.1
        if i == len(x) - 1:
            a = (x[i] - x[i - 1]) / 0.1
            b = (x[i] - x[i - 2]) / 0.2
            return (2 * a + b) / 3
            # return ((2 * x[i - 1] + 1 * x[i - 2]) / 3) / 0.1
        if i == len(x) - 2:
            a1 = (x[i] - x[i - 1]) / 0.1
            a2 = (x[x + 1] - x[i]) / 0.1
            b = (x[i] - x[i - 2]) / 0.2
            return (2 * a1 + 2 * a2 + b) / 5
            # return ((2 * x[i - 1] + 2 * x[i + 1] + 1 * x[i - 2]) / 5) / 0.1
        a1 = (x[i] - x[i - 1]) / 0.1
        a2 = (x[i + 1] - x[i]) / 0.1
        b1 = (x[i] - x[i - 2]) / 0.2
        b2 = (x[i + 2] - x[i]) / 0.2
        return (2 * a1 + 2 * a2 + b1 + b2) / 6
        # return ((2 * x[i - 1] + 2 * x[i + 1] + 1 * x[i - 2] + 1 * x[i + 2]) / 6) / 0.1
    def method_2(x, i):
        if i == len(x) - 1:
            return (x[i] - x[i - 1]) / 0.1
        return (x[i + 1] - x[i]) / 0.1
    print(method_1(x, i))
    print(method_2(x, i))

if __name__ == "__main__":
    problem_1([1, 2, 3, 2, 4, 6, 2])
    problem_2([1, 2, 3, 4, 5, "hello", 'hi', 'j'])
    problem_3([1, 2, 2, 4], [1, 2, 3, 4])
    problem_4([1, 2, 3, 4, 5], [1, 2])
    problem_5([4, 10, 2, 2, 3, 2, 3, 50, 7], [2, 3, 50])
    problem_6([1, 2, 5, 3, 4, 5])
    problem_7([0.5, 0.6, 0.89, 0.92], 1)
    