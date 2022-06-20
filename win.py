while True:
    print("Choose an option [1]Main  and [2] User : ")
    choice =str(input("Your Choice: "))
    if choice == '1':
        import main
        break
        
    elif choice == '2':
        import winwin.py
        break
    else:
        print ("Invalid input......!")
