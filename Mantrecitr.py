import time

mantra = "No Mantra Entered"
reps = 0
timedelay = 0
count = 1

print('Enter desired Mantra')
mantra = input()
print('Enter Number of Repetitions')
reps = int(input())
print("Enter Time Delay (1 = 1 second)")
timedelay = float(input())

while reps > 0:
    print(count,":", mantra)
    reps -= 1
    count += 1
    time.sleep(timedelay)
    
print("00((0)0)(0)")
input("Press ENTER to Exit")