from PyInquirer import prompt
import csv
user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
        "validate": lambda text: text != "" or "Please enter a name"
    }
]

def add_user():
    
    infos = prompt(user_questions)
    name = infos["name"]

    with open('users.csv', 'a', newline='') as csvfile:
        tmp = csv.writer(csvfile, delimiter=' ')
        tmp.writerow([name])
    # This function should create a new user, asking for its name
    return