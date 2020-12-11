# on Saute des lignes et ecrit le nom du programme
print(" ")
print(" ")
print(" ")
print("Resolveur d'equation")
print(" ")
print(" ")
print(" ")

#############################################
#############################################

resultat: int = 0

# On crée cette variable qui va poser des questions a l'utilisateur
utiliser2 = input("votre equation est-elle simple ou complexe (ecrivez s pour simple et c pour complexe): ")
signe1 = input("Entrez le premier signe apres le x (* ou / ou - ou +): ")
print(" ")
nombre1 = int(input("entrez le premier nombre: "))
print(" ")
if utiliser2 == "c" :
    signe2 = input("entrez le deuxiéme signe : ")
    print(" ")
    nombre2 = int(input("entrez le deuxiéme nombre: "))
print(" ")
resultat = int(input("entrez le resultat de l'equation: "))

signefinal1 = ""
signefinal2 = ""
nombrefinal1 = 0
nombrefinal2 = 0
resultat1 = 0
resultat2: int = 0
egaliteDeX = 0
result1 = 0
result2 = 0

if utiliser2 == "c":
    if signe2 == "*":
        resultat2 = resultat / nombre2
        if signe1 == "*":
            egaliteDeX = resultat2 / nombre1

        if signe1 == "/":
            egaliteDeX = resultat2 * nombre1

        if signe1 == "-":
            egaliteDeX = resultat2 + nombre1


        if signe1 == "+":
            egaliteDeX = resultat2 - nombre1

    if signe2 == "/":
        resultat2 = resultat * nombre2
        if signe1 == "*":
            egaliteDeX = resultat2 / nombre1

        if signe1 == "/":
            egaliteDeX = resultat2 * nombre1

        if signe1 == "-":
            egaliteDeX = resultat2 + nombre1

        if signe1 == "+":
            egaliteDeX = resultat2 - nombre1

    if signe2 == "-":
        resultat2 = resultat + nombre2
        if signe1 == "*":
            egaliteDeX = resultat2 / nombre1

        if signe1 == "/":
            egaliteDeX = resultat2 * nombre1

        if signe1 == "-":
            egaliteDeX = resultat2 + nombre1

        if signe1 == "+":
            egaliteDeX = resultat2 - nombre1

    if signe2 == "+":
        resultat2 = resultat - nombre2
        if signe1 == "*":
            egaliteDeX = resultat2 / nombre1

        if signe1 == "/":
            egaliteDeX = resultat2 * nombre1

        if signe1 == "-":
            egaliteDeX = resultat2 + nombre1

        if signe1 == "+":
            egaliteDeX = resultat2 - nombre1
else:
    if signe1 == "*":
        egaliteDeX =  resultat / nombre1

    if signe1 == "/":
        egaliteDeX =  resultat * nombre1

    if signe1 == "-":
        egaliteDeX =  resultat + nombre1

    if signe1 == "+":
        egaliteDeX =  resultat - nombre1

#Aprés tout ce bordel, on peut enfin ecrire la valeur finale de x
print(egaliteDeX)
