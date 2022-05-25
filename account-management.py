import configparser
import crayons

# variable
file = "my-accounts.ini"


def calculVir(nbr, percentage):  # Function pour calculer le découpage du virement
    nbr = float(nbr)
    percentage = float(percentage)
    calc = round(nbr - (nbr * percentage/100) - nbr, 1)
    return float(calc)


def log(string):
    return print('{}'.format(string))


# Lecture du fichier.ini
with open(file, 'a') as configfile:
    config = configparser.ConfigParser()
    config.read(file)
    try:
        config.add_section('COMPTE')
        config.set('COMPTE', 'CA', '20')
        config.write(configfile)
        log("Création du fichier " + file + "...")
    except:
        log("Lecture du fichier " + file + "...")

# insertion du montants / tableau des restes
vir = input("Rentrer le montant du virement : ")
rest = float(vir)
log("=====€=====\n")

# On boucle sur les différentes valeurs du fichier et on calcul le tout
for key in config['COMPTE']:
    readPercentage = float(config['COMPTE'][key])
    withdrew = calculVir(vir, readPercentage)
    rest = rest + withdrew
    log(crayons.green("Montant à retiré et transférer sur le compte ") +
        crayons.yellow(str(key)) + " : " + crayons.red(str(withdrew) + "€\n"))

log("Reste : " + crayons.yellow(str(round(rest, 1)) + "€\n"))
log("=====€=====\n")
input("Appuyer sur Entrer pour terminer...")
