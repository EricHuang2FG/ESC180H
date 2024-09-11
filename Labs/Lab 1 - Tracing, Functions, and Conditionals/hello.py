class Question5:

    @staticmethod
    def main():
        print("Hello!")

class Question6And7:

    @staticmethod
    def greetings(name1, name2):
        print(f"Hello, {name1}")
        if name1 != name2:
            print(f"Hello, {name2}")
        else:
            print(f"Hello, your name is still {name1}")
        print(f"Hello, {name1} and {name2}. Your names are {name1} and {name2}")
        print(f"Hi there, your names are still {name1} and {name2}")

        name1 = "Prof. Carrick"
        name2 = "Prof. Bentz"

class Question8:

    @staticmethod
    def more_greetings(greetee):
        if greetee == "Lord Voldemort":
            print("I'm not talking to you.")
        else:
            print(f"Hello, my name is {greetee}")

def main():
    Question5.main()
    Question6And7.greetings("Eric", "Justin")
    Question8.more_greetings("Eric")

if __name__ == "__main__":
    main()