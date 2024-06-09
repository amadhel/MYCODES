from datetime import date
today_date =date.today().strftime("%Y")
birth_year = int(input("ENTER YOUR BIRTH YEAR"))
print("your current age is ", int(today_date)-birth_year)
