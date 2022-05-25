import configparser
import crayons


def calculVir(nbr, percentage):  # Function pour calculer le découpage du virement
    nbr = int(nbr)
    percentage = float(percentage)
    calc = round(nbr - (nbr * percentage/100) - nbr, 1)
    return float(calc)


def printCrGreen(string):
    return print('{}'.format(crayons.green(string)))


print('{}'.format(crayons.green()))
# Lecture du fichier.ini
config = configparser.ConfigParser()
config.read('my-accounts.ini')

# insertion du montants / tableau des restes
print(" ")
vir = input("Rentrer le montant du virement : ")
rest = float(vir)
print("=====€=====")
print(" ")
# On boucle sur les différentes valeurs du fichier et on calcul le tout
for key in config['COMPTE']:
    readPercentage = float(config['COMPTE'][key])
    withdrew = calculVir(vir, readPercentage)
    rest = rest + withdrew
    printCrGreen("Montant à retiré et transférer sur le compte " +
                 str(key) + " : ") + crayons.red(str(withdrew) + "€")
    # print("Montant à retiré pour transférer sur le compte " +
    #       str(key) + " : " + str(withdrew) + "€")
print("Reste : " + crayons.yellow(str(round(rest, 1)) + "€"))
print(" ")
print("=====€=====")
input("Appuyer sur Entrer pour terminer...")
