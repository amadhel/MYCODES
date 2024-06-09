def my_fucntion():
    user = input("what is your password?: ")
    if user == "endy":
        print("correct")
    else:
        print(
            "incorrect\n"
            "try again"
        )
        my_fucntion()

my_fucntion()