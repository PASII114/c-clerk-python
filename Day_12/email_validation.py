import time
def check_email(email):

    if len(email) == 0:
        return False

    if '@' not in email:
        return False

    if email.index('@'):
        if email.startswith('@') or email.endswith('@'):
            return False

        else:
            return True

    return None

def main():
    try:
        email = input("Enter your email: ")

        if check_email(email):
            print("You email format is correct")
        else:
            print("Please enter a valid email")
    except KeyboardInterrupt:
        print("\nExiting Programme.........")
        time.sleep(2)
        exit()

while True:
    main()