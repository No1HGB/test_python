# 데이터 정의
user_data = {"name": "Alice", "age": 30, "balance": 1000}


# 함수 정의
def deposit(balance, amount):
    return balance + amount


def withdraw(balance, amount):
    if balance >= amount:
        return balance - amount
    else:
        print("Insufficient funds!")
        return balance


draw = withdraw(30, 100)

# 실행
print("Initial balance:", user_data["balance"])
user_data["balance"] = deposit(user_data["balance"], 200)
print("After deposit:", user_data["balance"])
user_data["balance"] = withdraw(user_data["balance"], 500)
print("After withdrawal:", user_data["balance"])
