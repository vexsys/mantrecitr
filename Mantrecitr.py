import time

mantra = "No Mantra Entered"
reps = 0
count = 1

print('Enter desired Mantra')
mantra = input()
print('Enter Number of Repetitions')
reps = int(input())

while reps > 0:
    print(count,":", mantra)
    reps -= 1
    count += 1
    
print("00((0)0)(0)")