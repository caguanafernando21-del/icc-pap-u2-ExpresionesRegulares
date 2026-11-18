import re


def main():
    runEjemplo1()
    runEjemplo2()
    runEjemplo3()
    
    
def runEjemplo():
    patron = r"ab*"
    palabras = {"a","ab","abbb","abab","b",""}
    for n in palabras:
        coincide = re.match(patron, n)
        print(f"{n} => {coincide}")    

    
def runEjemplo2():
        regex = r"[T0][0-9]{3}"

        lista = ["T001", "0120", "T01", "X001", "T0001"]

        for codigo in lista:
            print(f"{codigo} => {re.match(regex, codigo)}")
    
def runEjemplo3():
        texto = "Sensores: T001 reporta 23.5 C; O001 reporta 12 PERSONAS; T002 reporta -2 C."

        patron = r"[TO][0-9]{3}"

        for matcher in re.finditer(patron, texto):
            print(f"Encontrado: {matcher.group()}, posicion: {matcher.start()}")

if __name__ == "__main__":
    main()