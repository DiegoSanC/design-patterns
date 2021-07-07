#Motivación: aumentar la funcionalidad de un objeto sin necesidad de reescribir o alterar el código
# de una clas (open close principle)
#Mantener una nueva funcionalidad separada (single responsability principle)
import time

def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"{func.__name__} took {int((end -start)*1000)} ms")
        return result
    return wrapper

@time_it
def some_op():
    print("Starting op")
    time.sleep(1)
    print("We are done")
    return 123

if __name__ == "__main__":
    #time_it(some_op)() Esto funciona si no ponemos el decorador
    some_op()