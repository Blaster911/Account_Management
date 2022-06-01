import configparser
import crayons

# -----------------------------------------------     Variables Global     -----------------------------------------------
nameFileConfig = "my-accounts.ini"
nameCount = 'MONTANT COMPTE'
addSection = {'ALLOCATION COMPTE': {'CA': '10',
                                    'N26': '30',
                                    'LivretA': '40'},
              nameCount: {'CA': '0',
                          'N26': '0',
                          'LivretA': '0'},
              'OBJECTIF COMPTE': {'CA': '210',
                                  'N26': '250',
                                  'LivretA': '300'}
              }
# -----------------------------------------------         functions        -----------------------------------------------


def calculVir(nbr, percentage):  # traitement des comptes
    nbr = float(nbr)
    percentage = float(percentage)
    calc = round(nbr - (nbr * percentage/100) - nbr, 1)
    return float(calc)


def log(string):  # formatage des logs
    return print('{}'.format(string))


# -------- function gestion des fichiers --------

# nameFile: nom du fichier;
# typeFile: type de fichier;


# function Lecture du fichier ou création de celui-ci avec les paramètres par défaut
def openOrCreateFile(nameFile, typeFile, addSectionDefault):
    if (typeFile == "config"):
        try:
            with open(nameFile, 'r') as configfile:
                config = configparser.ConfigParser()
                config.read(nameFile)
                log("Lecture du fichier " + crayons.yellow(nameFile) + "...")
                # for key in config[nameCount]:
                #     log(config[nameCount][key])
                return config
        except:
            with open(nameFile, 'w') as configfile:
                config = configparser.ConfigParser()
                config.read_dict(addSectionDefault)
                config.sections()

                config.write(configfile)
                log("Création du fichier " + nameFile + "...")
                return config


def modifiedSectionConfig(nameFile, config, nameSection, Key, value):

    calcMontantAccount = float(config[nameSection][Key]) + float(value)
    with open(nameFile, 'w') as configfile:
        config[nameSection][Key] = str(calcMontantAccount)
        config.sections()
        config.write(configfile)


config = openOrCreateFile(nameFileConfig, "config", addSection)


# Insertion du montants / tableau des restes
vir = input("Rentrer le montant du virement : ")
rest = float(vir)
log("=====€=====\n")
totalAllCompte = 0

# On boucle sur les différentes valeurs du fichier et on calcul le tout
for key in config['ALLOCATION COMPTE']:
    readPercentage = float(config['ALLOCATION COMPTE'][key])
    withdrew = -calculVir(vir, readPercentage)
    totalCompte = float(config['MONTANT COMPTE'][key]) + withdrew
    rest = rest + -withdrew
    totalAllCompte += totalCompte
    log(crayons.green("Montant a retiré et transférer sur le compte ") +
        crayons.yellow(str(key)) + " : " + crayons.green(str(withdrew) + "€"))
    modifiedSectionConfig(nameFileConfig, config,  nameCount, key, withdrew)
    log("Total déposé sur le compte : " +
        crayons.yellow(str(totalCompte) + "€"))
    try:
        readObjectif = float(config['OBJECTIF COMPTE'][key])
        if(readObjectif > totalCompte):
            log(
                crayons.cyan("Objéctif: ") +
                crayons.yellow(str(readObjectif) + "€ ") +
                crayons.red("Objectif non atteint\n")
            )
        if(readObjectif <= totalCompte):
            log(
                crayons.cyan("Objectif : ") +
                crayons.yellow(str(readObjectif) + "€ ") +
                crayons.green("Objectif atteint!\n")
            )
    except:
        log("")

log("Total des Comptes : " + crayons.cyan(str(totalAllCompte) + " €"))
log("Reste : " + crayons.cyan(str(round(rest, 1)) + "€\n"))
log("=====€=====\n")

input("Appuyer sur Entrer pour terminer...")
