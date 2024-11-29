class BankAccount:
    """
    은행 계좌 클래스
    """

    def __init__(self, name, age, balance):
        """
        은행 계좌의 필요 변수 생성
        :param name: 이름
        :param age: 나이
        :param balance: 계좌 잔액
        """
        self.name = name
        self.age = age
        self.balance = balance

    def deposit(self, amount):
        """
        예금: 본인의 은행 계좌에 예금액 만큼 예금
        :param amount: 예금액
        :return: None
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        출금: 인의 은행 계좌에 출금액 만큼 출금
        :param amount: 출금액
        :return: None
        """
        # 계좌 잔액이 출금액보다 많이 남아있는 경우메만 출금합니다.
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds!")


# 은행 계좌 객체 생성 및 사용
account = BankAccount(name="Alice", age=30, balance=1000)

print("Initial balance:", account.balance)
account.deposit(200)
print("After deposit:", account.balance)
account.withdraw(500)
print("After withdrawal:", account.balance)
