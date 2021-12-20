
class Worker:
    def __init__(self, name, surname, position, profit, bonus):
        income_dict = {
            "wage": profit,
            "bonus": bonus
        }
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income_dict

class Position(Worker):
    def get_full_name(self):
        w = f'{self.name} {self.surname}'
        print(w)

    def get_total_income(self):
        e = (sum(map(int,self._income.values())))
        print(e)





q = Position('Elena', 'Petrova', 'Worker','5000','50')
q.get_full_name()
q.get_total_income()
