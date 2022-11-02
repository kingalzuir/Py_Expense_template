import csv

def show_status ():
    users = 0
    lUsers = []
    with open('users.csv', newline='') as csvfile1:
        reader = csv.reader(csvfile1, delimiter=' ', quotechar='|')
        for row in reader:
            lUsers.append(row[0])
            users += 1
    print (lUsers)
    matrix = [[0 for _ in range(users)] for _ in range(users)]
    with open('expense_report.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            amount = row[0]
            label = row[1]
            spender = row[2]
            involves = row[3]
            actual_len = len(involves)
            if  actual_len > 2:
                for person in involves:
                    if (person == spender):
                        continue
                    matrix[lUsers.index(person)[lUsers.index(spender)]] -= amount
    i = 0
    for person in lUsers:
        i += 1
        print(person + " owes " + matrix[i].count + "€")