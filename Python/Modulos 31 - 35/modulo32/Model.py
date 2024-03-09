import re

class Model:
    # Trabalhando com regular expressions e tkinter
    def __init__(self, email):
        self.email = email
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Endereço de email invalido: {value}')
        
    def save(self):
        with open('emails.txt', 'a') as f:
            f.write(self.email + '\n')
        
    