from random import randint

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
websites = ["www.youtube.com", "youtube.com"]

try:
    with open(hosts_path, "r+") as file:
        content = file.read()

        for website in websites:
            if website not in content:
                file.write(f"127.0.0.1 {website}\n")

except PermissionError:
    print("Run as admin")    

def unblock_websites(websites):
    try:
        with open(hosts_path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()

    except PermissionError:
        print("Run as admin")

def quiz(questions):
    questions_right = 0

    for i in range(1, questions + 1):
        num1 = randint(1, 10)
        num2 = randint(1, 10)

        while True:
            try:
                ans = int(input(f"{num1} x {num2} = "))
                break

            except ValueError:
                print("Enter a number")

        if num1 * num2 == ans:
            questions_right += 1

    if questions_right == questions:
        return True 

    return False           

print("\nWays to unblock YouTube:\n")

print("1. Unblock Websites With Password")
print("2. Math Quiz\n")

choice = None

while True:
    try:
        choice = int(input("Enter your choice: "))

        if choice in range(1, 3):
            break
        
        else:
            print("Enter a number between 1 & 2")
    
    except ValueError:
        print("Enter a number between 1 & 2")

if choice == 1:
    password = input("Enter password: ")

    if password == "ILoveFootball":
        unblock_websites(websites)        
        print("Websites successfully unblocked")

else:
    if quiz(10):
        print("Hooray! You completed the quiz!")
        unblock_websites(websites)

    else:
        print("You lost! Better luck next time")    