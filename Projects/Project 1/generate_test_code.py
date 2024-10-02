from random import randint
from gamify import (
    offer_star, 
    perform_activity, star_can_be_taken, most_fun_activity_minute, 
    initialize
)

def main():
    ALL_ACTIVITIES = ["running", "textbooks", "resting"]
    all_func = [offer_star, offer_star, star_can_be_taken, star_can_be_taken, most_fun_activity_minute, perform_activity, perform_activity, perform_activity]
    call_stack = [all_func[randint(0, len(all_func) - 1)] for i in range(40)]
    initialize()
    with open("test_code.txt", "w") as f:
        f.write("initialize()\n")
        for func in call_stack:
            activity = ALL_ACTIVITIES[randint(0, 2)]
            params = "()"
            if func == offer_star or func == star_can_be_taken:
                params = f"(\"{activity}\")"
            elif func == perform_activity:
                duration = randint(1, 1000)
                params = f"(\"{activity}\", {duration})"

            if func == star_can_be_taken or func == most_fun_activity_minute:
                f.write(f"print({func.__name__}{params})\n")
            else:
                f.write(f"{func.__name__}{params}\n")
            f.write("print(\"HEDONS: \" + str(get_cur_hedons()))\n")
            f.write("print(\"HEALTH: \" + str(get_cur_health()))\n")

if __name__ == "__main__":
    main()