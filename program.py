import datetime

def print_header():
    print('----------------------')
    print('    Test Bday')
    print('----------------------')
    print()

def get_birthday_from_user():
    print('When were you born? ')
    year = int(input('What year were you born [YYYY]: '))
    month = int(input('What month were you born [MM]: '))
    day = int(input('What day were you born [DD]: '))

    birthday = datetime.date(year, month, day)
    return birthday

def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date

    return dt.days

def print_birthday_information(days):
    if days < 0:
        print("Your birthday was {} days ago!".format(-days))
    elif days > 0:
        print("Your birthday is in {} days!".format(days))
    else:
        print("HAPPY BIRTHDAY!!!!")










def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)

if __name__ == '__main__':
    main()
