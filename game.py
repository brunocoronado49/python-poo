class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def get_attr(self):
        print(self.nombre, ":", sep="")
        print(f"Fuerza: {self.fuerza}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")

    def power_up(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def atack(self, enemigo):
        damage = self.damage(enemigo)
        enemigo.vida = enemigo.vida - damage
        print(f"{self.nombre} ha causado {damage} puntos de damage a {enemigo.nombre}")
        if enemigo.live():
            print(f"La vidad el enemigo {enemigo.nombre} es {enemigo.vida}")
        else:
            return enemigo.dead()

    def live(self):
        return self.vida > 0

    def damage(self, enemigo):
        return self.fuerza - enemigo.defensa

    def dead(self):
        self.vida <= 0
        print(f"{self.nombre} esta muerto!")


personaje = Personaje("Humano", 5, 2, 3, 50)
#personaje.get_attr()


class Brujo(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def change_weapon(self):
        opcion = int(input("Elije tu espada: 1) Plata: Util contra los monstruos. 2) Acero: Util contra humanos y otras bestias "))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 6
        else:
            print("Elije una espada correcta")
            
    def get_attr(self):
        super().get_attr()
        print(f"Espada: {self.espada}")
        
    def damage(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa
    
geralt = Brujo("Geralt de Rivia", 60, 80, 70, 100, 5)
#geralt.get_attr()


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
        
    def get_attr(self):
        super().get_attr()
        print(f"Libro: {self.libro}")

    def damage(self, enemigo):
        return self.fuerza * self.libro - enemigo.defensa

keira = Mago("Keira", 50, 85, 60, 100, 5)
#Keira.get_attr()


class Monstruo(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, veneno):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.veneno = veneno
        
    def get_attr(self):
        super().get_attr()
        print(f"Veneno: {self.veneno}")
        
    def damage(self, enemigo):
        return self.fuerza * self.veneno - enemigo.defensa
    
eredin = Monstruo("Heredin", 70, 90, 70, 100, 6)
#eredin.get_attr()


def combat(player_one, player_two):
    turno = 0
    while player_one.live() and player_two.live():
        print(f"\nTurno {turno}")
        print(">>> Acción de ", player_one.nombre,":", sep="")
        player_one.atack(player_two)
        print(">>> Acción de ", player_two.nombre,":", sep="")
        player_two.atack(player_one)
        turno += 1
    if player_one.live():
        print("\nHa ganado", player_one.nombre)
    elif player_two.live():
        print("\nHa ganado", player_two.nombre)
    else:
        print("\nEmpate")
        
geralt.get_attr()
eredin.get_attr()

geralt.change_weapon()

combat(geralt, eredin)