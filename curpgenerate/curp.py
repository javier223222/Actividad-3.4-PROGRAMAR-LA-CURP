import random
import math
class CurpGenerator:
    def __init__(self,nombre:str, apellido_paterno:str, apellido_materno:str, fecha_nacimiento:str, sexo:str, estado:str):
        self.nombre=nombre.upper()
        self.apellido_paterno=apellido_paterno.upper()
        self.apellido_materno=apellido_materno.upper()
        self.fecha_nacimiento=fecha_nacimiento.split("-")
        self.sexo=sexo.upper()
        self.estado=estado.upper()
        self.curp=""
    def calculateCurp(self) -> str:
        self.curp+=self.apellido_paterno[0]
        self.curp+=self.first_vocal(self.apellido_paterno)
        self.curp+=self.apellido_materno[0]
        self.curp+=self.nombre[0]
        self.curp+=str(self.fecha_nacimiento[2])[2]+str(self.fecha_nacimiento[2])[3]
        self.curp+=str(self.fecha_nacimiento[1])
       
        self.curp+=str(self.fecha_nacimiento[0])
        
        self.curp+=self.sexo
        self.curp+=self.estado
        self.curp+=self.consonant(self.apellido_paterno)
        self.curp+=self.consonant(self.apellido_materno)
        self.curp+=self.consonant(self.nombre.split()[0])
        if(int(self.fecha_nacimiento[2])<=1999):
            self.curp+=str(self.generate_number())
        else :
            self.curp+=self.generate_letter().upper()
        self.curp+=str(self.generate_number())
        
        
        


        return self.curp
    
    def first_vocal(self,text:str)->str:
        for word in text:
            if word == "A" or word =="E" or word=="I" or word == "O" or word=="U":
                return word
    def generate_number(self):
        return random.randint(1,9)
    def generate_letter(self):
        letter=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        number=random.randint(0,len(letter)-1)
        return letter[number]
    def consonant(self,text:str)->str:
        letters=list(text.strip())
        num=len(letters)/2
        if (num%2 != 0):
            num=math.floor(num)-1
            
        letters=letters[num:]
        for word in letters:
            if word.lower()  in [ "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"] :
                return word
        

    
    
            
            
    
