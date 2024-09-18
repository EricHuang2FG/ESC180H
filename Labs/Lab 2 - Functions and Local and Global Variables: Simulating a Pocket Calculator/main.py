def my_sqrt(x):
    global sqr
    sqr = x ** 0.5
    return sqr

def my_print_square(x):
    print(x ** 0.5)

def display_current_value():
    print(f"Current value: {val}")

def add(to_add):
    global val, prev
    prev = val
    val += to_add

def mult(to_mult):
    global val, prev
    prev = val
    val *= to_mult

def div(to_div):
    if to_div == 0:
        return print("Can't divide by 0!")
    global val, prev
    prev = val
    val /= to_div

def save_in_memory():
    global mem
    mem = val

def recall():
    global val, prev
    prev = val
    val = mem

def undo():
    global val, prev
    temp = val
    val = prev
    prev = temp

if __name__ == "__main__":
    # res = my_sqrt(25) # stored in a variable but no print statement called
    # print(sqr) # prints global variable sqr
    # res = my_print_square(25) # res == None
    # print(res) # this prints None

    val, mem, prev = 0, 0, 0
    print("Welcome to the calculator program.")
    display_current_value()

    add(5)
    display_current_value()

    mult(5)
    display_current_value()

    div(5)
    display_current_value()

    save_in_memory()

    mult(5)
    mult(5)
    display_current_value()

    recall()
    display_current_value()

    mult(5)
    undo()
    display_current_value()

    undo()
    display_current_value()

    undo()
    display_current_value()
