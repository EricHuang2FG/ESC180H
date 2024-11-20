from copy import deepcopy

def to_lower(s):
    return s.lower()

s = "HELAOWDAWD"
s = to_lower(s)

L = [1, 2, 3]

def g(L):
    print(id(L))
    G = [1, 3, 2]
    return G

L = g(L)
print(id(L))

def g1(L):
    print(id(L))
    G = L
    return G

L = g1(L)
print(id(L))

d = {1: "HELLO", 2: "HI"}
d_c = d.copy()

def c(d):
    print(id(d))
    G = d.copy()
    return G

d = c(d)
print(id(d))

def c_1(d):
    print(id(d))
    G = d
    return G

d = c_1(d)
print(id(d))

orig_dict = {1: [1, 2, 3], 2: [3, 4, 5]}
dict_copy = orig_dict.copy()

dict_copy[1].append(5)

print(orig_dict)
print(dict_copy)

orig_dict = {1: [1, 2, 3], 2: [3, 4, 5]}
dict_copy = deepcopy(dict_copy)

print(orig_dict)
print(dict_copy)