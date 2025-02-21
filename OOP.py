class Auto():
    """
    Das ist meine Autoklasse
    """

    def __init__(self, marke, modell, baujahr, tuere, ps):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.raeder = 4
        self.tuere = tuere
        self.ps = ps

    def begruesung(self):
        print('Hallo ich bin dein Auto, ' + self.marke)

    def fahren(self):
        print('Brum Brum Brum ' * int(self.ps / 10))


auto1 = Auto('Dacia', 'jogger', '2020', 2, 110)
print(auto1.marke)
auto1.begruesung()
auto1.fahren()
