from functions import conditions, verifyTime, printMessage

#Verify that the condition function (switch case) works
def test_conditions():
    plateNumber ="PBM2690"
    day=conditions(int(plateNumber[-1]))
    assert day == "Friday"


#Verify that the time is correctly detected in the pico y placa range (morning)
def test_verifyTime():
    hour=9
    minute=15
    morning = hour in range (6 ,10) and minute in range (-1,31)
    assert morning == True



#Verify that the time is correctly detected in the pico y placa range (afternoon)
def test_verifyTime():
    hour=16
    minute=00
    afternoon = hour in range (15 ,18) and minute in range (-1,31)
    assert afternoon == True

#Verify that the message is correctly printed
def test_printMessage():
    assert print("You are allowed to drive your car") == printMessage(True)




   