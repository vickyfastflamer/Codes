USER = ['124005126', '124005016', '124005161']
password = 'bank'

def auth():
    username = input("USERNAME: ")
    passw = input("PASSWORD: ")

    for i in range(len(USER)):
        if username == USER[i] and passw == password:
            print("Good!")
            break
    else:
        print("Invalid credentials. Please try again.")

auth()
