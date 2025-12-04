import random
import time

hit_ac = 10
run_ac = 10

while True:
    time.sleep(1)
    hit_roll = random.randint(1,20)
    run_roll = random.randint(1,20)

    if hit_roll > hit_ac:
        print("Hit! Will there be a home run?")
        if run_roll > run_ac:
            print("Nice home run!")
        else:
            print("Ooof! Out!")
            continue
    else:
        print("Ooof! No hit! Out!")
        


    # print(hit_ac, hit_roll)
    # print(run_ac, run_roll)
