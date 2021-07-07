class Person:
    def __init__(self) -> None:
        #adress
        self.street_address = None
        self.postcode = None
        self.city = None

        #employment
        self.company_name = None
        self.position = None
        self.anual_income = None


    def __str__(self) -> str:
        return f"Address: {self.street_address}, {self.postcode}, {self.city} " + \
            f"Employed at {self.company_name} as a {self.position} earning {self.anual_income}"
    
#Lo que vamos a dicutir es la posibilidad de tener 2 constructores: uno para la información sobre
# la dirección y otro sobre la información del empleo

#para tener estos dos constructores, vamos a creear un tercero que funcionará como clase base
#Utilizar una instanciacion del objeto Person en el constructor es un truco que permite a los sub
#builders trabajar con objetos que ya están construidos
class PersonBuilder:
    def __init__(self, person=Person()) -> None:
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAdressBuilder(self.person)

    def build(self):
        return self.person

#subbuilder job
class PersonJobBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person)
        #por que no setear como aquí debajo
        #elf.person = person
    
    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self
    
    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self

class PersonAdressBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person)
    
    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self
    
    def in_city(self, city):
        self.person.city = city
        return self


pb = PersonBuilder()
person =pb\
    .lives\
        .at("123 London Road")\
        .in_city("London")\
        .with_postcode("SW12BC")\
    .works\
        .at("Fabrikam")\
        .as_a("Engineer")\
        .earning(123000)\
    .build()

print(person)
