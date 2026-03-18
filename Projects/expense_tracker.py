'''
Expense Tracker
Requirements:
    Users can add an expense with a description and amount.
    Users can update an expense.
    Users can delete an expense.
    Users can view all expenses.
    Users can view a summary of all expenses.
    Users can view a summary of expenses for a specific month (of current year).

'''
print('----- Expense Tracker Project ---------')


all_items = []

def add_items(expense, description , amount):
    items = {
        'expense': expense,
        'description': description,
        'amount': amount
    }
    all_items.append(items)
    print('Items Added Successfully!')

def update_expense(index , new_expense):
    if 0 <= index  < len(all_items):
        all_items[index]['expense'] = new_expense
        print('expense Updated')
    else:
        print('Recored Not Found!')

def delete_expense(index):
    if 0 <= index < len(all_items):
        all_items.pop(index)
        print('Expense Deletd')
    else:
        print('Expense Not found!')


def view_all_expense():
    print(f"{'ID':<5}{'Expense':<15}{'Description':<20}{'Amount'}")
    for i, item in enumerate(all_items, start=1):
        print(f"{i:<5} ${item['expense']:<15} {item['description']:<20}${item['amount']}")

def expense_summery():
    total = sum([item['amount'] for item in all_items])
    print(f'Total Expense is: ${total}')


while True:
    print('\n1. Add Items')
    print('2. Update Expense')
    print('3. Delete Expense')
    print('4. view All Expense')    
    print('5. Expense Summery')    
    print('6. Exits')

    choice = input('Enter Your Choice: ')

    if choice == '1':
        expense = input('Enter the Expense $: ') 
        description = input('Enter the Description: ')
        amount = int(input('Enter the Amount: '))

        add_items(expense,description,amount)

    elif choice == '2':
        view_all_expense()
        index = int(input('Enter the iD: ')) -1
        new_expense = input('Enter the New expense $: ')
        update_expense(index, new_expense)

    elif choice == '3':
        view_all_expense()
        index = int(input('Enter the Expense ID: ')) -1
        delete_expense(index=index)

    elif choice == '5':
        expense_summery()

    elif choice == '4':
        view_all_expense()

    elif choice == '6':
        print('Goodbye....')
        break

    else:
        print('Invalid Choice')


