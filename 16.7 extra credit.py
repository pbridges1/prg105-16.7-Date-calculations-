from datetime import datetime

today = datetime.today()


class Birthday:
    def __init__(self):
        self.month = None
        self.day = None
        self.year = None
bday = Birthday()
bday.month = int(input('Enter birth month; mm format: \n'))
bday.day = int(input('Enter birth day; dd format: \n'))
bday.year = int(input('Enter birth year; yyyy format: \n'))
age = today.year - bday.year
if bday.month > today.month:
    age -= 1
if bday.month == today.month and bday.day > today.day:
    age -= 1
print "You are", age, "years old"


def until():

    m = bday.month
    d = bday.day
    birthday = datetime(today.year, m, d)
    hours = today.hour
    if birthday < today:
        print "Your birthday went past %d days ago." % (today-birthday).days
        birthday = birthday.replace(year=today.year + 1)
        hours = birthday.replace(hour=today.hour + 0)

    hours_until_birthday = (hours - today)
    print "There are", hours_until_birthday, "until your next Birthday"

until()
