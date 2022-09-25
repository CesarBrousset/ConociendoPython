class Persona:
    primera_parte = 'cuerpo'
    segunda_parte = 'alma'
    
    def __init__(self, color, raza, religion):
        self.color = color
        self.raza = raza
        self.religion = religion
        
    def hablar(self):
            print('hola')
        
    def caminar(self, pasos):
        print(f'esta persona ha caminado {pasos} pasos')
        
Javier = Persona('blanco', 'ario', 'catolico')

print(f'Javier tiene:{Javier.primera_parte}')        
print(f'Javier tiene:{Javier.segunda_parte}')

Javier.hablar()
Javier.caminar(6)               