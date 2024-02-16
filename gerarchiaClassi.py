class Persona(object):
    def __init__(self, nome, cognome,*arg):
        self.nome = nome
        self.cognome = cognome
        super().__init__(*arg)

    def visualizza(self):
        print('Nome ', self.nome)
        print('Cognome ', self.cognome)

class Impiegato(Persona):
    def __init__(self, livello, azienda, *args):
        self.livello = livello
        self.azienda = azienda
        super().__init__(*args)

    def visualizza(self):

        Persona.visualizza(self)
        print('Livello ', self.livello)
        print('Azienda ', self.azienda)

class Tempo(object):

    sep = ':'
    def __init__(self, ora, minuto, secondo,*args):

        self.ora = ora
        self.minuto = minuto
        self.secondo = secondo
        super(Tempo, self).__init__(*args)

    def visualizza(self):
        print('Ora ', self.ora, self.sep, end = ' ')
        print (self.minuto, self.sep, self.secondo)

class Orario(Impiegato, Tempo):
    def __init__(self, giorno, *args):
        self.giorno = giorno
        super().__init__(*args)
    def visualizza(self):

        print (self.giorno)
        Impiegato.visualizza(self)
        Tempo.visualizza(self)
print(Orario.__mro__)
o1 = Orario('Lunedì', 3, 'Mathema', 'Alex', 'Bellini', 10, 0, 0)
o1.visualizza()