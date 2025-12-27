import secrets
import string

def generate_password(length = 12):

    if length <8:
        return "Password too short"
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    symbols = string.punctuation
    digits = string.digits


    password  = [ secrets.choice(lowercase), secrets.choice(uppercase), secrets.choice(symbols), secrets.choice(digits) ]

    rest_char = lowercase+ uppercase+symbols+ digits

    for i in range(length-4):
        password.append(secrets.choice(rest_char))
        
    secrets.SystemRandom().shuffle(password)
    return "".join(password)

if __name__ == "__main__":
    print(generate_password())