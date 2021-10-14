# OOP

# encapsulare
# abstractizare
# mostenire (inheritance)
# polimorfism

# PascalCaseClassName
# nume_de_functii 
# numeDeFunctie

import abc


class Masina:
    consum = None 

    def __init__(self, model=None, cc=None, combustibil=None, tractiune=None, an_fabricatie=None, km=None, *args):
        self.model = model
        self.capacitate = cc
        self.combustibil = combustibil
        self.tractiune = tractiune
        self.an_fabricatie = an_fabricatie
        self._alti_parametri = args
        if km is not None:
            self.km_parcursi = km
        else:
            self.km_parcursi = 0
        self.__proprietar = None
        self.nume = None 

    def mergi(self, distanta):
        if (self.combustibil_ramas):
            self.km_parcursi += distanta
    
    def consuma_rezervor(self):
        self.__distribuie_combustibil()

    def adauga_combustibil(self, combustibil_l):
        try:
            self.combustibil_ramas += combustibil_l
        except Exception as e:
            self.combustibil_ramas = combustibil_l

    def adauga_proprietar(self, nume):
        self.__proprietar = nume

    def afiseaza_proprietar(self):
        print(f"Proprietar: {self.__proprietar}")

    def __distribuie_combustibil(self):
        self.km_parcursi = self.km_parcursi + 5 * self.combustibil_ramas 
        self.combustibil_ramas = 0

class Echipa:
    consum = 5
    def __init__(self, nume): 
        self.nume = nume 
        self.__proprietar = None 

    def adauga_proprietar(self, nume):
        self.__proprietar = nume

    def afiseaza_proprietar(self):
        print(f"Proprietar: {self.__proprietar}")

    @classmethod
    def fromstring(cls, text): # assume text "dsdakshjdkshjfkjd fsdfdsjf: name"
        name = text.split(":")[1]
        return cls(name)

    def add_name(self, name):
        self.nume = name
        return self 

    def add_owner(self, name):
        self.adauga_proprietar(name)
        return self 

class MasinaF1(Masina):
    def __init__(self, constructor=None, *args):
        self.constructor = constructor
        super().__init__(*args)

class MasinaF2(Masina, Echipa):
    def __init__(self, nume, *args):
        Echipa.__init__(self, nume)
        Masina.__init__(self, *args)
        
class MasinaAbstracta(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def change_name(self, name):
        pass 

class CopilMasinaAbstracta(MasinaAbstracta):
    def change_name(self, name):
        self.name = name

class Copil2MasinaAbstracta(MasinaAbstracta):
    def change_name(self, name):
        self.name = name.upper()

class MySequence():
    def __init__(self, **kwargs):
        self.__dict = dict(kwargs)
    
    def __len__(self):
        return len(self.__dict)

    def __getitem__(self, index):
        return self.__dict[index]

    def __getattribute__(self, name: str):
        if name == "_MySequence__dict":
            raise TypeError("Immutable, stupid! Leave me alone!")
        else:
            return self.__getattribute__(name)

    def __setattribute__(self, name: str, value):
        if name == "_MySequence__dict":
            raise TypeError("Immutable, stupid! Leave me alone!")
        else:
            self.__setattr__(name, value)
        
    def __setitem__(self, index, value):
        raise TypeError("Unable to set value. Type is not mutable")
    
# ms = MySequence(1,2,3,4,5,6,7)
# print("Length my sequence: %s" % len(ms))
# # for i in ms:
# #     print(i)
# ms[2] = 1000
# print(ms[2])

ms2 = MySequence(name="andrei", location="romania")
print(ms2["name"])
# ms2["name"] = "liviu"
# print(ms2["name"])

ms2._MySequence__dict["name"] = 10



# m1 = MasinaAbstracta("ford")
# m2 = CopilMasinaAbstracta("")
# m2.change_name("logan")
# print(m2.name)

# m3 = Copil2MasinaAbstracta("")
# m3.change_name("ford")
# print(m3.name)

# Masina.consum = 10      
# masina1 = Masina("logan", 1600, "benzina", "fata", 2010)
# masina2 = Masina("ford", 2000, "motorina", "4x4", 2016, 4, 1)

# print("ambele")
# print(masina1.consum)
# print(masina2.consum)

# print("change object consum")
# masina1.consum = 20
# print(masina1.consum)
# print(masina2.consum)

# print("modify class")
# Masina.consum = 30
# print(masina1.consum)
# print(masina2.consum)


# if masina1.model == "logan":
#     print(masina1)
# else: 
#     print("Nu stiu ce tip de masina avem.")

# print(f"Masina {masina2.model} este fabricata in {masina2.an_fabricatie}")

# masina1.adauga_combustibil(10)
# print(f"Masina {masina1.model} are {masina1.km_parcursi} km")
# masina1.mergi(50)
# print(f"Masina {masina1.model} are {masina1.km_parcursi} km")

# print("Private atrribute + Methods")
# masina1.afiseaza_proprietar()
# masina1.adauga_proprietar("andrei")
# masina1.afiseaza_proprietar()

# print(masina1.km_parcursi, masina1.combustibil_ramas)
# masina1.consuma_rezervor()
# print(masina1.km_parcursi, masina1.combustibil_ramas)

# masinaf11 = MasinaF1("alpha", "logan", 1600, "benzina", "fata", 2010)
# print(masinaf11.__dict__)

# masinaf12 = MasinaF2("alpha", "logan", 1600, "benzina", "fata", 2010)
# print(masinaf12.__dict__)

# masinaf12.adauga_proprietar("andrei")
# Echipa.afiseaza_proprietar(masinaf12)
# Masina.afiseaza_proprietar(masinaf12)

e = Echipa.fromstring("sdjflksajflksjd fksdjf sdsdfjkhgfuiwyeuifje: echipa1")
print(e)
e2 = Echipa("echipa1")
print(e2)

e3 = Echipa.fromstring("sdas:echipa2").add_owner("andrei").add_name("andrei's echipa2")
print(e3.__dict__)