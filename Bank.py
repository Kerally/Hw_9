import datetime
import uuid
import pprint
from decimal import Decimal


class Bank:
    UUID = uuid.uuid4()
    First_name = 'Vladyslav'
    Last_name = 'Sadullaiev'
    now = datetime.datetime.now()
    data = now.strftime(('%Y-%m-%d %H:%M'))
    value = 1000
    value_deposit = 0
    list_of_transaction = []


    def __init__(self, amount_to_output, amount_to_deposit):
        self.amount_to_output = amount_to_output
        self.amount_to_deposit = amount_to_deposit


    def get_value(self):
        return "Money: {}, Deposit: {}".format(self.value, self.value_deposit)


    def output(self):
        # проверка на возможность снять деньги
        if Bank.value - Decimal(self.amount_to_output) < 0:
            return "Not enought money"
        else:
            Bank.value = Bank.value - Decimal(self.amount_to_output)
            # заполняем масив транзакций транзакцией Output money
            transaction = "{}, Output money: {}".format(Bank.data, self.amount_to_output)
            Bank.list_of_transaction.append(transaction)
            return "Operation [Output money] was successful!"


    def deposit(self):
        # проверка на возможность положить деньги под депозит
        if Bank.value - Decimal(self.amount_to_deposit) < 0:
            return "Not enought money"
        else:   
            Bank.value_deposit = Decimal(Bank.value_deposit) + Decimal(self.amount_to_deposit)
            Bank.value = Bank.value - Decimal(self.amount_to_deposit)
            # заполняем масив транзакций транзакцией Invest to deposit
            transaction = "{}, Invest to deposit: {}".format(Bank.data, self.amount_to_deposit)
            Bank.list_of_transaction.append(transaction)
            return "Operation [Invest to deposit] was successful!"


    def transaction(self):
        return self.list_of_transaction


if __name__ == '__main__':
    Operation1 = Bank(100, 300)
    print(Operation1.output())
    print(Operation1.deposit())
    pprint.pprint(Operation1.transaction())

    Operation2 = Bank(150, 200)
    print(Operation2.output())
    print(Operation2.deposit())

    pprint.pprint(Operation2.transaction())
    print(Operation2.get_value())






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
#             print(Bank.output(Bank.amount_of_outpto))
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
# amount_of_outpto = input("Enter the amount to output(defoult: 100): ")
# проверка на число
# try: float(amount_of_outpto)
# except: 
#     try: int(amount_of_outpto)
#     except: amount_of_outpto = 100

