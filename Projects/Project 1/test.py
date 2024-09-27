# this file compares outputs of gamify.py and gamify_test.py

from random import randint
from gamify import (
    get_cur_hedons, get_cur_health, offer_star, 
    perform_activity, star_can_be_taken, most_fun_activity_minute, 
    initialize
)
import gamify_test as test

def main():
    ALL_ACTIVITIES = ["running", "textbooks", "resting"]
    all_func = [offer_star, star_can_be_taken, most_fun_activity_minute, perform_activity, perform_activity, perform_activity]
    call_stack = [all_func[randint(0, len(all_func) - 1)] for i in range(50)]
    initialize()
    test.initialize()
    with open("results.txt", "w") as f:
        try:
            for func in call_stack:
                activity = ALL_ACTIVITIES[randint(0, 2)]
                params = ()
                a, b = None, None
                if func == offer_star:
                    func(activity)
                    test.offer_star(activity)
                    params = (activity,)
                elif func == star_can_be_taken:
                    a, b = func(activity), test.star_can_be_taken(activity)
                    params = (activity,)
                    assert a == b, f"Star can be taken don't match, {a} != {b}"
                elif func == most_fun_activity_minute:
                    a, b = func(), test.most_fun_activity_minute()
                    assert a == b, f"Most fun activity don't match, {a} != {b}"
                elif func == perform_activity:
                    duration = randint(1, 1000)
                    func(activity, duration)
                    test.perform_activity(activity, duration)
                    params = (activity, duration)
                msg = f'Function call: {func.__name__}{params}'
                print(msg)
                f.write(msg + "\n")
                if a is not None and b is not None:
                    msg = f"Other outputs: {a}, {b}"
                    print(msg)
                    f.write(msg + "\n")
                msg = f"My health: {get_cur_health()}, test health: {test.get_cur_health()}"
                print(msg)
                f.write(msg + "\n")
                assert get_cur_health() == test.get_cur_health(), f"Health don't match, {get_cur_health()} != {test.get_cur_health()}"
                msg = f"My hedons: {get_cur_hedons()}, test hedons: {test.get_cur_hedons()}\n"
                print(msg)
                f.write(msg + "\n\n")
                assert get_cur_hedons() == test.get_cur_hedons(), f"Hedons don't match, {get_cur_hedons()} != {test.get_cur_hedons()}"
        except AssertionError as e:
            print("***AssertionError***")
            print(e)
            f.write(f"***AssertionError {str(e)}***")

if __name__ == "__main__":
    main()
