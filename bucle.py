#from tracemalloc import start
from pynput.mouse import Controller

def run():

        menu = """
        Quieres ver CP?🐧

        1 - SI
        2 - NO

        Elije una opcion (1, 2): """
        opcion = int(input(menu))
        if opcion == 1:
            while opcion:         
                mouse = Controller()
                mouse.position = (300, 500)
                print("ERES BASURAAAAAAAAA")
        elif opcion == 2:
            print("Eres una gran persona❤")


if __name__ == "__main__":
    run()




#contador = 1
#print(contador)
#while contador < 10000000000000:
#    contador += 1
#    print(contador)


#for tabla in range(10):
#    print(10 * tabla)