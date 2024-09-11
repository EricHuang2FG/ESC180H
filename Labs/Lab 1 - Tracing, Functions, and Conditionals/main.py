class Question2:

    @staticmethod
    def main(course):
        if course == "Praxis":
            print("Carrick")
        elif course == "CIV":
            print("Bentz")

class Question3:

    @staticmethod
    def greet_instructor(course, greeting):
        c = "Carrick" if course == "Praxis" else "Bentz"
        return f"{greeting} {c}"

def main():
    Question2.main("Praxis")
    print(Question3.greet_instructor("Praxis", "Hello professor"))

if __name__ == "__main__":
    main()