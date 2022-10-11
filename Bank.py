import datetime
import uuid
import pprint
from decimal import Decimal


class Bank:
    def __init__(self, UUID, First_name, Last_name):
        self.UUID = uuid.uuid4()
        self.First_name = 'Vladyslav'
        self.Last_name = 'Sadullaiev'

    value = 1000
    value_deposit = 0
    list_of_transaction = []
    now = datetime.datetime.now()
    data = now.strftime(('%Y-%m-%d %H:%M'))
    amount_of_output = 100
    amount_to_deposit = 100


    def get_value(value, value_deposit):
        return "Money: {}, Deposit: {}".format(Bank.value, Bank.value_deposit)


    def output(amount_of_output):
        # проверка на возможность снять деньги
        if Bank.value - Decimal(amount_of_output) < 0:
            return "Not enought money"
        else:
            Bank.value = Bank.value - Decimal(amount_of_output)
            # заполняем масив транзакций транзакцией Output money
            transaction = "{}, Output money: {}".format(Bank.data, amount_of_output)
            Bank.list_of_transaction.append(transaction)
            return "operation was successful"


    def deposit(amount_to_deposit):
        # проверка на возможность положить деньги под депозит
        if Bank.value - Decimal(amount_to_deposit) < 0:
            return "Not enought money"
        else:   
            Bank.value_deposit = Decimal(Bank.value_deposit) + Decimal(amount_to_deposit)
            Bank.value = Bank.value - Decimal(amount_to_deposit)
            # заполняем масив транзакций транзакцией Invest to deposit
            transaction = "{}, Invest to deposit: {}".format(Bank.data, amount_to_deposit)
            Bank.list_of_transaction.append(transaction)
            return "operation was successful"


    def transaction(list_of_transaction):
        return Bank.list_of_transaction


if __name__ == '__main__':
    print(Bank.get_value(Bank.value, Bank.value_deposit))
    print(Bank.output(Bank.amount_of_output))
    print(Bank.deposit(Bank.amount_to_deposit))
    pprint.pprint(Bank.transaction(Bank.list_of_transaction))
    print(Bank.get_value(Bank.value, Bank.value_deposit))


#-----------------------------------------------------------------------
# меню программы
# def main():
#     print("""
#     1 - Amount of money
#     2 - Output money
#     3 - Deposit
#     4 - Transaction
#     5 - End
#     """)
#     choise = input("Enter the number: ")
#     match choise:
#         case '1':
#             print(Bank.get_value(Bank.value, Bank.value_deposit))
#         case '2':
#             print(Bank.output(Bank.amount_of_output))
#         case '3':
#             print(Bank.deposit(Bank.amount_to_deposit))
#         case '4':
#             pprint.pprint(Bank.transaction(Bank.list_of_transaction))
#         case '5':
#             quit()
#         case _:
#             print("Enter the number again (1-5)")
#             main()
#-----------------------------------------------------------------------
# amount_of_output = input("Enter the amount to output(defoult: 100): ")
# проверка на число
# try: float(amount_of_output)
# except: 
#     try: int(amount_of_output)
#     except: amount_of_output = 100


