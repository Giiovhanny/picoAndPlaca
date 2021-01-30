import datetime 
from functions import conditions, verifyTime, printMessage

numberPlate= input('Enter your plate number: ')
dateEntry = input('Enter a date in YYYY-MM-DD format: ')
time=input('Enter a time in h:m format (24h): ')
year, month, day  = map(int, dateEntry.split('-'))
hour, minute  = map(int, time.split(':'))
finalDate = datetime.datetime(year, month, day, hour,minute)
allowedToDrive=True

day = conditions(int(numberPlate[-1]))
morning, afternoon = verifyTime (finalDate.hour, finalDate.minute)

print(finalDate.strftime("%A") , day, finalDate.hour, finalDate.minute,morning, afternoon)
if(finalDate.strftime("%A") == day):
    if morning or afternoon:
        allowedToDrive=False


printMessage(allowedToDrive)