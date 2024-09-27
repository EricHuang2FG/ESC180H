def drink_coffee():
    global last_coffee_time, last_coffee_time2, too_much_coffee
    if last_coffee_time2 > 0 and (current_time - last_coffee_time2 < 120):
        too_much_coffee = True
        return
    last_coffee_time2 = last_coffee_time
    last_coffee_time = current_time

def study(minutes):
    global knols, current_time
    if too_much_coffee:
        current_time += minutes
        return
    knols += minutes * (5 if last_coffee_time != current_time else 10)
    current_time += minutes

def initialize():
    global too_much_coffee
    global current_time
    global last_coffee_time
    global last_coffee_time2
    global knols
    too_much_coffee = False
    current_time = 0
    knols = 0
    last_coffee_time = -100
    last_coffee_time2 = -100

if __name__ == "__main__":
    initialize() # start the simulation
    print(knols)
    study(60) # knols = 300
    print(knols)
    study(20) # knols = 400
    print(knols)
    drink_coffee() # knols = 400
    print(knols)
    study(10) # knols = 500
    print(knols)
    drink_coffee() # knols = 500
    print(knols)
    study(120) # knols = 600
    print(knols)
    drink_coffee() # knols = 600, 3rd coffee in 20 minutes
    print(knols)
    study(10) # knols = 600