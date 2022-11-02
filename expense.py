from PyInquirer import prompt
import csv

def getUsers():
    res = []
    with open('users.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            res.append(row[0])
            print(row)
    return res

def getUsersAsJSON(spender):
    res = []
    with open('users.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            if (row[0] == spender):
                res.append({"name": row[0], "checked": True})
                continue
            res.append({"name": row[0]})
            print(row)
    return res

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": getUsers()
    }
]

def expense_q(spender):
    return [{
        "type": "checkbox",
        'qmark': '😃',
        'message': 'Select people involved',
        'name': 'involves',
        'choices': getUsersAsJSON(spender),
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }]





def new_expense(*args):
    infos = prompt(expense_questions)

    amount = infos["amount"]
    label = infos["label"]
    spender = infos["spender"]
    
    infos_spender = prompt(expense_q(spender))
    involves = infos_spender["involves"]

    expense = [amount, label, spender, involves]
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a', newline='') as csvfile:
        tmp = csv.writer(csvfile, delimiter=' ')
        tmp.writerow(expense)
    print("Expense Added !")
    return True


