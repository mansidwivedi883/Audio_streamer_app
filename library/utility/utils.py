import random 
from string import ascii_uppercase




class utils:
    def generate_unique_code(Length):
        while True:
            code = ""
            for _ in range(Length):
                code += random.choice(ascii_uppercase)
            if code not in rooms:
                break
        return code 
