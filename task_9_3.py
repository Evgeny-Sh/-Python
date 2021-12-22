class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        print('Full name:', full_name)
        return full_name

    def get_total_income(self):
        total_income = self._income["wage"] + self._income["bonus"]
        print(f'Total income: {total_income}')
        return total_income
    

for worker_data in (('Ivan', 'Ivanov', 'director', 1000, 3300),
                    ('Vasiliy', 'Petrov', 'manager', 500, 1000),
                    ('Evgeny', 'Shustov', 'developer', 5000, 1000)):
    
    worker_i = Position(*worker_data)
    print(worker_i.name)
    print(worker_i.surname)
    print(worker_i.position)
    print(worker_i._income)
    worker_i.get_full_name()
    worker_i.get_total_income()
    print()
