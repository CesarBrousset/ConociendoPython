class Gato:
     
    def __init__(self, nombre):
        self.nombre = nombre   

    def hablar(self):
        print(f'soy un objeto de la {type(self)} y me llaman {self.nombre}')
        
    def __getitem__(self, pos):
        return 1

