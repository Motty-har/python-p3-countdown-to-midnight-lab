from time import sleep;

def countdown(int):
    while int > 0:
        print(f'{int} SECOND(S)!')
        int -= 1
    print("HAPPY NEW YEAR!")
    pass

def countdown_with_sleep(int):
    while int > 0:
        print(f'{int} SECOND(S)!')
        int -=1
        sleep(1)
    print("HAPPY NEW YEAR!")
    pass