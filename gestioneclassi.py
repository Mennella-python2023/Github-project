class Persona(object):
    def __init__(self, nome, cognome):

        self.nome = nome 
        self.cognome = cognome

    def cambiaNome(self, nome):
        self.nome = nome

    def visualizza(self):

        print('Nome ', end = '')
        print(self.nome, end = '')
        print()
        print('Cognome ', end = '')
        print (self.cognome, end = '')
        print()

p1 = Persona('Andrea', 'Guidi')
p1.visualizza()
p1.cambiaNome('Pippo')
p1.visualizza()