from time import sleep

def countdown(n):
    while n:
        print(f'{n} SECOND(S)!')
        n -= 1
    
    print('HAPPY NEW YEAR!')

def countdown_with_sleep(n):
    while n:
        print(f'{n} SECOND(S)!')
        n -= 1
        sleep(1)
    print('HAPPY NEW YEAR!')