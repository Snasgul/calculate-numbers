import time

def isPrimary(number, primaryNumbers):
    for j in primaryNumbers:
        if(j != 0):
            if (number%j == 0):
                return False
    return True


try:
    primaryNumbers = [2, 3]
    primary = False
    numberRange = int(input("Number range: "))
    timeElapsed = None

    startTime = time.time()
    for i in range(2, numberRange):
        if isPrimary(i, primaryNumbers) == True:
            primaryNumbers.append(i)

    timeElapsed = time.time() - startTime

finally:
    if timeElapsed == None:
        timeElapsed = time.time() - startTime
    print(primaryNumbers)
    
    file = open("primeNumbers_0_to_" + str(numberRange) + ".txt", "wt")
    file.write("\n".join(str(i) for i in primaryNumbers))
    file.close()

    print("Time elapsed: " + str(timeElapsed * 1000) + " ms")
    print(str(len(primaryNumbers)) + " primary numbers from 0 to " + str(numberRange))