from pprint import pprint
import datetime
import uuid


class Bank:
    value = 1000
    value_deposit = 0
    list_of_transaction = []
    now = datetime.datetime.now()
    data = now.strftime(('%Y-%m-%d_%H:%M'))

    def __init__(self, amount_of_output, amount_to_deposit):
        self.UUID = uuid.uuid4()
        self.First_name = 'Vladyslav'
        self.Last_name = 'Sadullaiev'

        self.amount_of_output = amount_of_output
        self.amount_to_deposit = amount_to_deposit


    # return value of money, deposits
    def get_value():
        return ("Money: {} | Deposit: {}").format(Bank.value, Bank.value_deposit)


    # output cash from money
    def output(self):
        # test for correct input (int/float)
        try: float(self.amount_of_output)
        except: 
            try: int(self.amount_of_output)
            except: self.amount_of_output = 100

        # test for enought money to output
        if Bank.value - self.amount_of_output < 0:
            return "Not enought money"
        else:
            Bank.value = Bank.value - self.amount_of_output
            Bank.value = Bank.value - (self.amount_of_output/100*1)
            # add transaction "output money" to transaction list
            transaction = ("{}: Output money: {}").format(Bank.data, self.amount_of_output)
            Bank.list_of_transaction.append(transaction)
            return "Operation [output money] was successful"


    def deposit(self):
        # test for correct input (int/float)
        try: float(self.amount_to_deposit)
        except: 
            try: int(self.amount_to_deposit)
            except: self.amount_to_deposit = 100

        # test for enought money to make deposit
        if Bank.value - self.amount_to_deposit < 0:
            return "Not enought money"
        else:
            Bank.value_deposit = Bank.value_deposit + self.amount_to_deposit
            Bank.value = Bank.value - self.amount_to_deposit
            Bank.value = Bank.value - (self.amount_to_deposit/100*1)
            # add transaction "made a deposit" to transaction list
            transaction = ("{}: Made a deposit: {}").format(Bank.data, self.amount_to_deposit)
            Bank.list_of_transaction.append(transaction)
            return "Operation [make a deposit] was successful"

    
    # get list of transaction
    def get_transaction():
        return Bank.list_of_transaction


if __name__ == '__main__':
    print(Bank.get_value())
    transaction1 = Bank(234.56, 123.45)
    print(transaction1.output())
    print(transaction1.deposit())
    pprint(Bank.get_transaction())
    print(Bank.get_value())

