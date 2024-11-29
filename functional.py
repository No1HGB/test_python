from functools import reduce


# 순수 함수 정의
def deposit(balance, amount):
    return balance + amount


def withdraw(balance, amount):
    return balance - amount if balance >= amount else balance


# 초기 데이터 정의
transactions = [
    ("deposit", 200),
    ("withdraw", 500),
    ("deposit", 500),
]

# 함수 적용
initial_balance = 1000


# 고차 함수로 처리
def process_transaction(balance, transaction):
    action, amount = transaction
    if action == "deposit":
        return deposit(balance, amount)
    elif action == "withdraw":
        return withdraw(balance, amount)


final_balance = reduce(process_transaction, transactions, initial_balance)

print("Final balance:", final_balance)
