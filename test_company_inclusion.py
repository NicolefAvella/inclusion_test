# Python Developer Test Questions

# Answer 1 and 2
from abc import ABC, abstractmethod
    
class UniversityProgram(ABC):
    """
    Abstract class of university program
    """
    
    def __init__(self, full_name: str, months: int, program_contact: str):
        self.full_name = full_name
        self.months = months
        self.program_contact = program_contact

    @classmethod
    def new(cls, name, months, program_contact):
        pass
    
    @abstractmethod
    def duration_years(self):
        pass

    @abstractmethod
    def show(self):
        pass


class Ungraduate(UniversityProgram):
    """
    Concrete class for create Ungraduate Programs
    """
    
    def __init__(self, full_name: str, months: int, program_contact: str):
        super().__init__(full_name, months, program_contact)

    @classmethod
    def new(cls, name, months, program_contact):
        full_name = f'{name} Ungraduate'
        return cls(full_name, months, program_contact)

    def duration_years(self):
        return self.months/12
    
    def show(self):
        print(f'The program: {self.full_name} has a duration of {self.months} months')


instance_1 = Ungraduate(
    full_name='Electrical Engineering Ungraduate',
    months=60,
    program_contact="Tesla"
)
instance_1.show()
print('Duration in years instance 1:', instance_1.duration_years())

instance_2 = Ungraduate.new(
    name='History',
    months=36,
    program_contact='Voltaire'
)
instance_2.show()
print('Duration in years instance 1:', instance_2.duration_years())


# Answer 3
final_number = 40

#With list comprehension
even_list = [number for number in range(1, final_number+1) if number%2 == 0]
print('Result Answer 3 with list comprehension: ', even_list)

#With lambda function
numbers_list = list(range(1, final_number+1))
event_list_lambda = list(filter(lambda x: (x % 2 == 0), numbers_list))
print('Result Answer 3 with lambda function: ', event_list_lambda)


# Answer 4
list_of_dicts_1 = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'a': 5, 'b': 6}, {'x': 5, 'a': 7, 'b': 8}]
list_of_dicts_2 = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'a': 5, 'b': 6}, {'x': 7, 'a': 8, 'b': 9}]

next_element = next((element for element in list_of_dicts_1 if element.get('x')==5), {})
next_element_default = next((element for element in list_of_dicts_2 if element.get('x')==5), {})

print('Result next element x=5: ', next_element)
print('Result next element default: ', next_element_default)


# Answer 5
import os
import json
import datetime

def convert_time(integer_timestamp):
    datetime_obj = datetime.datetime.fromtimestamp(integer_timestamp / 1e3)
    return str(datetime_obj)

with open(os.path.dirname(__file__)+'/'+'test_data.json') as file:
    data = json.load(file)
    invoice_ids = data['invoiceIds']
    invoice_matches = [invoice for invoice in invoice_ids if "583" in invoice]

    print('Payee id: ', data['payee']['id'])
    print('Invoices with 583:', invoice_matches)
    
    #Convert dates
    data['fileDateTime'] = convert_time(data['fileDateTime'])
    data['receivedDateTime'] = convert_time(data['receivedDateTime'])
    
    print('Formated fileDateTime: ', data['fileDateTime'])
    print('Formated receivedDateTime: ', data['receivedDateTime'])

with open(os.path.dirname(__file__)+'/'+'new_test_data.json', 'w') as outfile:
    json.dump(data, outfile)
    
    