def tests(parametrs):
    a = parametrs #darbības ar parametriem
    return a #Funkcijas rezultāts

print(tests("kaķis"))

def pirmais(par1, par2):
    reizinajums = par1*par2
    summa = par1+par2
    if reizinajums<1000 :
        return reizinajums
    else:
        return summa

print("The result is", pirmais(20,30))

def otrais():
    esosais = 0
    ieprieksejais = 0
    for i in range(10):
        ieprieksejais = esosais
        esosais = i
        summa = ieprieksejais+esosais
        print("Current number", esosais, "Previous number", ieprieksejais, "Sum:", summa)
    return
otrais()

#otrais

def tresais(teksts):
    print("Sākotnējais teksts ir", teksts)
    print("Tikai pāra indeksa burti:")
    for i in range(0, len(teksts), 2):
        print(teksts[i])
    return
tresais("pynative")

#tresais

def ceturtais(teksts, n):
    print("Teksts:", teksts)
    print("Noņemot pirmos",n,"burtus sanāk:", teksts [n:])
    return
ceturtais("pynative",4)

#ceturtais

def piektais(saraksts):
    print("Dotais saraksts:", saraksts)
    print("Result is", saraksts[0]==saraksts[-1])
    return

skaitli1 = [10, 20, 30, 40, 10]
skaitli2 = [75, 65, 35, 75, 30]

piektais(skaitli1)

#piektais
