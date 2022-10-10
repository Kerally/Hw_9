import pprint
import datetime
from decimal import Decimal



class Bank:
    UUID = '123e4567-e89b-12d3-a456-426614174000'
    value = 1000
    value_deposit = 0
    list_of_transaction = []
    now = datetime.datetime.now()
    data = now.strftime(('%Y-%m-%d_%H:%M'))


def get_value():
    print("Money: ", Bank.value)
    print("Deposit: ", Bank.value_deposit)
    main()


def output():
    amount_of_output = input("Enter the amount to output(defoult: 100): ")
    # проверка на число
    try: float(amount_of_output)
    except: 
        try: int(amount_of_output)
        except: amount_of_output = 100


    # проверка на возможность снять деньги
    if Bank.value - Decimal(amount_of_output) < 0:
        print("Not enought money")
        main()
    else:
        Bank.value = Bank.value - Decimal(amount_of_output)
        # заполняем масив транзакций транзакцией Output money
        transaction = Bank.data = 'Output money: ', amount_of_output
        Bank.list_of_transaction.append(transaction)
        main()


def deposit():
    amount_to_deposit = input("Enter the amount to output(defoult: 100): ")
    # проверка на число
    try: float(amount_to_deposit)
    except: 
        try: int(amount_to_deposit)
        except: amount_to_deposit = 100

    # проверка на возможность положить деньги под депозит
    if Bank.value - Decimal(amount_to_deposit) < 0:
        print("Not enought money")
        main()
    else:   
        Bank.value_deposit = Bank.value_deposit + Decimal(amount_to_deposit)
        Bank.value = Bank.value - Decimal(amount_to_deposit)
        # заполняем масив транзакций транзакцией Invest to deposit
        transaction = Bank.data = 'Invest to deposit: ', Bank.value_deposit
        Bank.list_of_transaction.append(transaction)
        main()


def transaction():
    pprint.pprint(Bank.list_of_transaction)
    main()
    return True


def main():
    print("""
    1 - Amount of money
    2 - Output money
    3 - Deposit
    4 - transaction
    5 - End
    """)
    choise = input("Enter the number: ")

    match choise:
        case '1':
            get_value()
        case '2':
            output()
        case '3':
            deposit()
        case '4':
            transaction()
        case '5':
            quit()
        case _:
            print("Enter the number again (1-5)")
            main()
            


if __name__ == '__main__':
    main()

