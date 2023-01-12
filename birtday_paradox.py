import os

os.system('cls')

def probOfSameBirthday(n):
    q = 1
    for i in range(1, n):
        probability = i / 365
        q *= (1 - probability)
    p = 1 - q
    result = round((p * 100),3)
    print(str(result)+'%')

num = input('How many people in the room: ')

probOfSameBirthday(int(num))