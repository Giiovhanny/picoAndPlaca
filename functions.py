def conditions(i):
    switcher={
        1:'Monday' ,
        2:'Monday',
        3:'Tuesday',
        4:'Tuesday',
        5:'Wednesday',
        6:'Wednesday' ,
        7:'Thursday',
        8:'Thursday',
        9:'Friday',
        0:'Friday',
        }

    return switcher.get(i,"Invalid day of week")

def verifyTime(hour, minute):
     morning = hour in range (6 ,10) and minute in range (-1,31)
     afternoon = hour in range (15 ,18) and minute in range (-1,31)
     return morning, afternoon 

def printMessage(allowed):
    if allowed:
        print("You are allowed to drive your car")
    else:
        print("You are NOT allowed to drive your car")








