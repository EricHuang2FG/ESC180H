def parrot_trouble(talking, hour):
    return (talking and hour < 7) or (talking and hour > 20)

def sum_double(a, b):
    if a != b:
        return a + b
    return 2 * (a + b)

def sleep_in(weekday, vacation):
    return vacation or not weekday

def set_square(x):
    global ret_square
    ret_square = x ** 2
