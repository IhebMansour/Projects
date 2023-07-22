import datetime


def check(User_list):
    Goal = User_list[0].strip() # Remove leading and trailing spaces
    Deadline = User_list[1].strip() # Remove leading and trailing spaces

    deadline_date = datetime.datetime.strptime(Deadline, "%d.%m.%Y")
    today_date = datetime.datetime.today()
    time = deadline_date - today_date

    if time.days == -1 :
        print(f"the deadline is today")
    elif 0<=time.days<1:
        print(f"You will achieve {Goal} tomorrow .")
    elif time.days >= 1:
        print(f"Dear user! You will achieve {Goal} in {time.days+1} days .")
    else:
        print("Error, Please enter a new deadline.")
        user_input = input("Enter your goal with a past deadline separated by:\n")
        User_list = user_input.split(":")
        check(User_list)

user_input = input("Enter your goal with a deadline separated by:\n")
User_list = user_input.split(":")
check(User_list)
