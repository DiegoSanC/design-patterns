class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0
    
    def add_entry(self, text:str) -> None:
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos: int) -> None:
        del self.entries[pos]

    def __str__(self) -> str:
        return "\n".join(self.entries)

    # #Rompemos single responsability
    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()

    # #Rompemos single responsability 
    # # Ahora no solo tiene la responsabilidad la clase Journal de guardar la informacion si no que
    # # tiene la de guardar y cargar en ficheros (persistencia)  
    # def load(self, filename):
    #     pass

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()

j = Journal()

j.add_entry("hoy llore")
j.add_entry("me comi una cucaracha")
print(f"Journal entries:\n{j}")

file = r"prueba.txt"
PersistenceManager.save_to_file(j, file)