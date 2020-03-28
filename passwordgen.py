import datetime

def GenerateRandomNumber(rint):
    currentTime = datetime.datetime.now()
    rf = currentTime.microsecond * .000001
    return int(float(rint) * rf)

randomInput = str(input("Enter an integer: "))

if randomInput.isdigit():
    print (GenerateRandomNumber(randomInput))
else:
    print ("Not a valid input.")
