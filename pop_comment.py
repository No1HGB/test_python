# 데이터 정의
user_data: dict = {"name": "Alice", "age": 30, "balance": 1000}


# 함수 정의
def deposit(balance: int, amount: int) -> int:
    """
    예금 함수
    :param balance: 계좌 잔액
    :param amount: 입금액
    :return: 입급 후 계좌 잔액
    """
    return balance + amount


def withdraw(balance: int, amount: int) -> int:
    """
    출금 함수
    :param balance: 계좌 잔액
    :param amount: 출금액
    :return: 출금 후 계좌 잔액
    """
    if balance >= amount:
        return balance - amount
    else:
        print("Insufficient funds!")
        return balance


# 실행
print("Initial balance:", user_data["balance"])
user_data["balance"] = deposit(user_data["balance"], 200)
print("After deposit:", user_data["balance"])
user_data["balance"] = withdraw(user_data["balance"], 500)
print("After withdrawal:", user_data["balance"])
