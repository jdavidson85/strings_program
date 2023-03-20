import os

accounts_file = 'accounts.txt'
overdue_file = 'over90.txt'

if not os.path.isfile(accounts_file):
    print('Error: ' + accounts_file + ' does not exist.')
    exit()
if not os.path.isfile(overdue_file):
    print('Error: ' + overdue_file + ' does not exist.')
    exit()

accounts = []
overdue_accounts = []

with open(accounts_file, 'r') as f:
    for line in f:
        accounts.append(line.strip())

with open(overdue_file, 'r') as f:
    for line in f:
        overdue_accounts.append(line.strip())

for account in accounts:
    account_info = account.split(',')
    if account_info[0] in overdue_accounts:
        print(account)
