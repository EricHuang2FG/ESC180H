import time

def problem_2():
    def binary_search(L, e):
        low = 0
        high = len(L) - 1
        iter = 0
        while high - low >= 2:
            iter += 1
            mid = (low + high) // 2
            if L[mid] > e:
                high = mid - 1
            elif L[mid] < e:
                low = mid + 1
            else:
                return mid, iter
        if L[low] == e:
            return low, iter
        if L[high] == e:
            return high, iter
        return None, iter
    
    L = [i for i in range(5, 15)]
    print(binary_search(L, 7))

    # part c)
    # [1, 3, 5, 6, 7, 8, 9, 10, 11], binary_search(L, 1)

    base_size = 10
    for i in range(1, 11):
        list_size = base_size ** i
        L = [i for i in range(5, list_size + 5)]
        L_copy = L.copy()
        start = time.time()
        L_copy.sort()
        end = time.time()
        print(f"Time for linear search: {end - start}")
        start = time.time()
        _, iter = binary_search(L, 5)
        end = time.time()
        print(f"Time for binary search: {end - start}")
        print(iter)

if __name__ == "__main__":
    problem_2()
