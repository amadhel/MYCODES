def my_robot():
    Title="WELCOME TO PAGES ROBOTICS INC."
    print(Title)
    que1 = 'HOW MAY I HELP YOU?'
    que2 = 'PLEASE SELECT THE FOLLOWING OPTIONS'
    print(que1)
    print(que2)
    Request=input(
             "A. MENU\n"
             "B. INFORMATION\n"
             "C. ORDER\n"
             "D. PROGRAMMES\n"
             "E. EXIT\n"
             "Enter Option: "
    )   
    if Request.upper() == "A":
       print("PLEASE SELECT THE FF MENU")
    else:
        print(
            "invalid entry\n"
            "Please try again"
        )
        option = input("Do you wisht to continue?..press Y to continue N to exit: ")
        if option.lower() == "y" :
         my_robot()
        else:
            print("BYEE SEE YOU SOON")
            quit()
    menu = input(
        "1.FOOD SERVICES\n"
        "2.CLEANING SERVICES\n"
        "3.GHANA EMERGENCY CODES\n"
        "4.Cities information\n"
        "Enter Option: "
    )
    if menu == "1":
       print("FOOD MENU, AUTOMATICALLY OPENS WEBSITE, KINDLY CHOOSED THE FOOD TOY WANT") 
    option = input("do you want to open the website? press Y to open N to exit:  ") 
    if option == "y":
      import webbrowser
      chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
      url = "https://www.zubzz.com/menus"
      webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
      webbrowser.get('chrome').open_new_tab(url)
    else:
       my_robot() 

                                  
my_robot()