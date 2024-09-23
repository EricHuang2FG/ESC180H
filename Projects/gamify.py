def initialize() -> None:
    global ALL_ACTIVITIES
    global hedons, health
    global curr_time
    global curr_star, stars_offer_time
    global lost_interest
    global last_tiring_activities_time
    global time_running
    global running_hedons_now, textbooks_hedons_now
    ALL_ACTIVITIES = ["running", "textbooks", "resting"]
    hedons, health = 0, 0
    curr_star, stars_offer_time, lost_interest = None, [], False
    curr_time = 0
    last_tiring_activities_time = []
    time_running = 0
    running_hedons_now, textbooks_hedons_now = 2, 1

def get_cur_hedons():
    return hedons

def get_cur_health():
    return health

def offer_star(activity) -> None:
    global curr_star, stars_offer_time, lost_interest
    # filter star offers within 2 hours
    stars_offer_time = [t for t in stars_offer_time if curr_time - t < 120]
    if len(stars_offer_time) >= 2 and not lost_interest:
        # offering the third star within 2 hours, so they lose interest
        lost_interest = True
        curr_star = None
    elif activity in ALL_ACTIVITIES and not lost_interest:
        curr_star = activity
        stars_offer_time.append(curr_time)
    else:
        curr_star = None

def perform_activity(activity, duration) -> None:
    global health, hedons
    global curr_star
    global last_tiring_activities_time, time_running, curr_time
    # filter out time if more than 2 hours
    last_tiring_activities_time = [t for t in last_tiring_activities_time if curr_time - t < 120]

    curr_time += duration
    if activity in ALL_ACTIVITIES and duration and activity != "resting":
        if activity == "running":
            health += 3 * min(duration, max(180 - time_running, 0)) + max(time_running + duration - 180, 0)
            if len(last_tiring_activities_time) >= 1:
                # user is tired, deduct hedons
                hedons -= 2 * duration
            else:
                hedons += 2 * min(duration, 10) - 2 * max(duration - 10, 0)
            time_running += duration
        elif activity == "textbooks":
            time_running = 0 # reset clock
            health += 2 * duration
            if len(last_tiring_activities_time) >= 1:
                # user is tired, deduct hedons
                hedons -= 2 * duration
            else:
                hedons += min(duration, 20) - max(duration - 20, 0)
        last_tiring_activities_time.append(curr_time)

        if curr_star == activity and not lost_interest:
            hedons += 3 * min(duration, 10)

    else: #resting or performing some unknown activities
        time_running = 0 # reset clock
    curr_star = None

def star_can_be_taken(activity) -> bool:
    return curr_star == activity and not lost_interest

def most_fun_activity_minute():
    global running_hedons_now, textbooks_hedons_now
    global last_tiring_activities_time
    last_tiring_activities_time = [t for t in last_tiring_activities_time if curr_time - t < 120]
    if len(last_tiring_activities_time) >= 1: # tiring activity within 2 h!
        running_hedons_now, textbooks_hedons_now = -2, -2
    else:
        running_hedons_now, textbooks_hedons_now = 2, 1
    if curr_star == "running" and not lost_interest: 
        running_hedons_now += 3
    elif curr_star == "textbooks" and not lost_interest:
        textbooks_hedons_now += 3
    match = {"running": running_hedons_now, "textbooks": textbooks_hedons_now, "resting": 0}
    return max(match, key=match.get)

# UNITTEST FUNCTIONS BELOW
def print_unittest_variables():
    print(f"health: {health}")
    print(f"hedons: {hedons}")
    print(f"time_running: {time_running}")
    print()

def unittest():
    global curr_time
    perform_activity("running", 120)
    perform_activity("running", 30)
    perform_activity("running", 50)
    print_unittest_variables()

# UNITTEST FUNCTIONS ABOVE

if __name__ == "__main__":
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons()) # -20 = 10 * 2 + 20 * (-2)
    print(get_cur_health()) # 90 = 30 * 3
    print(most_fun_activity_minute()) # resting
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute()) # running
    perform_activity("textbooks", 30)
    print(get_cur_health()) # 150 = 90 + 30*2

    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons()) # -20 = 10 * 2 + 20 * (-2)
    print(get_cur_health()) # 90 = 30 * 3
    print(most_fun_activity_minute()) #resting
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute()) # running
    perform_activity("textbooks", 30)
    print(get_cur_health()) # 150 = 90 + 30*2
    print(get_cur_hedons()) # -80 = -20 + 30 * (-2)
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health()) # 210 = 150 + 20 * 3
    print(get_cur_hedons()) # -90 = -80 + 10 * (3-2) + 10 * (-2)
    perform_activity("running", 170)
    print(get_cur_health()) # 700 = 210 + 160 * 3 + 10 * 1
    print(get_cur_hedons()) # -430 = -90 + 170 * (-2)