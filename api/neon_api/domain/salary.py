class Salary:
    def __init__(self, date: str, amount: float, discount: float, cpf: str, id: int = None):
        self.id = id
        self.date = date
        self.amount = amount
        self.discount = discount
        self.cpf = cpf
