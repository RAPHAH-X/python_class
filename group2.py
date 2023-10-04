import random
def group2():
    Account_name = input("enter user account name: " )
    Password = int(input("enter password"))
    Account_num = int( random.randint(100000000, 999999999))
    Account_bal =(0.00)
    return Account_name, Password , Account_num, Account_bal

    # print(f"Account_name: {Account_name}")
    # print(f"password: {Password}")
    # print(f"Account_num: {Account_num}")
    # print(f"Account_bal: {Account_bal}")

group2()