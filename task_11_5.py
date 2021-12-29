class Storehouse:
    def __init__(self, name, address, max_storing_place):
        self.name = name
        self.address = address
        self._stored_items = dict()


    def add_equipment(self, equipment):
        if equipment in self._stored_items:
            self._stored_items[equipment] += 1
        else:
            self._stored_items[equipment] = 1


    def equipment_delivery(self, equipment, equipment_num, department_name):
        if equipment in self._stored_items and self._stored_items[equipment] >= equipment_num:
            self._stored_items[equipment] -= equipment_num
            print(f'Equipment with id {equipment.id} delivered to {department_name}')
        elif type(equipment).__bases__[0] == Equipment:
            print(f'No enough equipment with id {equipment.id} in store')


class Equipment:
    def __init__(self, id_number, model, producer, year_of_production):
        self.id = id_number
        self.model = model
        self.producer = producer
        self.year_of_production = year_of_production


class Printer(Equipment):
    def __init__(self, id_number, model, producer, year_of_production, printer_type, colored,
                 print_speed):
        super().__init__(id_number, model, producer, year_of_production)
        self.printer_type = printer_type
        self.colored = colored
        self.print_speed = print_speed


class Scanner(Equipment):
    def __init__(self, id_number, model, producer, year_of_production,
                 scan_speed, resolution):
        super().__init__(id_number, model, producer, year_of_production)
        self.scan_speed = scan_speed
        self.resolution = resolution


class Copier(Equipment):
    def __init__(self, id_number, model, producer, year_of_production, copier_type, colored,
                 copier_speed, resolution):
        super().__init__(id_number, model, producer, year_of_production)
        self.copier_type = copier_type
        self.colored = colored
        self.copier_speed = copier_speed
        self.resolution = resolution

# test
my_storehouse = Storehouse('Main', 'Moscow, Tverskaiya 10', 20)

printer_1 = Printer(434, 'Abc', 'HP', 2020, 'inkjet', True, 350)
printer_2 = Printer(435, 'Bca', 'PH', 2021, 'inkjet', False, 400)
printer_3 = Printer(436, 'ACda', 'RAD', 2010, 'inkjet', True, 450)

scanner_1 = Scanner(437, 'Abc', 'HP', 2020, 'inkjet', 200)
scanner_2 = Scanner(438, 'Bca', 'PH', 2021, 'inkjet', 140)
scanner_3 = Scanner(439, 'ACda', 'RAD', 2010, 'inkjet', 550)

copier_1 = Copier(440, 'Abc', 'HP', 2020, 'inkjet', False, 20, 200)
copier_2 = Copier(441, 'Bca', 'PH', 2021, 'inkjet', True, 40, 140)
copier_3 = Copier(442, 'ACda', 'RAD', 2010, 'inkjet', True, 50, 550)

available_equipement = [printer_1, printer_2, printer_3,
                        scanner_1, scanner_2, scanner_3,
                        copier_1, copier_2, copier_3]

for i in available_equipement:
    print(i.id, i.model,i.producer, i.year_of_production)
    my_storehouse.add_equipment(i)
    my_storehouse.add_equipment(i)

    
print(my_storehouse._stored_items)
print()
my_storehouse.equipment_delivery(scanner_1, 2, 'department')
print(my_storehouse._stored_items)
print()
my_storehouse.equipment_delivery(scanner_1, 1, 'department')
print()
