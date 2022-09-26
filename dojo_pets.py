class Mascota():
    # implementa __init__( name , tipo , golosinas):
    def __init__(self, nombre, tipo, golosina):
        self.nombre=nombre
        self.tipo= tipo
        self.golosina=golosina

    # implementa los siguientes métodos:
    # dormir() - incrementa la energía de la mascota en 25
    def dormir(self):
        self.energia +=25
        return self
    # comer() - incrementa la energía de la mascota en 5 y la salud en 10
    def comer(self):
        self.energia +=5
        self.salud +=10
        return self
    # jugar() - incrementa la salud de la mascota en 5
    def jugar(self):
        self.salud +=5
        return self
    # sonido() - incrementa la salud de la mascota en 5
    def sonido(self):
        self.salud +=5
        return self


class Perro(Mascota):
    def __init__(self,nombre, tipo, golosina, salud, energia):
        super().__init__(nombre,tipo,golosina)

    def sonido(self):
        print("Guauuu")

class Gato(Mascota):
    def __init__(self,nombre, tipo, golosina, salud, energia):
        super().__init__(nombre,tipo,golosina)

    def sonido(self):
        print("Miauu")

    
    
