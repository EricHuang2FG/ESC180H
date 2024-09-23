import time, random

def ring_bell() -> None:
    for i in range(10000):
        print("\a")
        t = random.randint(1, 30)
        time.sleep(t / 100)

if __name__ == "__main__":
    ring_bell()
