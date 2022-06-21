from randomOut import *

def getPhi(i):
    previousNumber = 1
    number = 1
    for i in range(i):
        number += previousNumber
        previousNumber = number - previousNumber
    return(number/previousNumber)

print("Phi: " + str(getPhi(int(input("Accuracy: ")))))
print(int(input("sass: ")))