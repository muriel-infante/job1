
def moyenne(a,b,c):
    moyenne_etudiant=(a+b+c)/3
    if moyenne_etudiant >= 15 and moyenne_etudiant <= 20:
        print("Très bon élève")
    elif moyenne_etudiant >=11 and moyenne_etudiant <= 14:
        print("Bon élève")
    elif moyenne_etudiant >=8 and moyenne_etudiant <= 10:
        print("Elève moyen")
    elif moyenne_etudiant >=0 and moyenne_etudiant <=7:
        print("Elève devant faire des efforts")
    else:
        return

num1 = int(input("Saisis une note :"))
num2 = int(input("Saisis une note :"))
num3 = int(input("Saisis une note :"))

moyenne(num1, num2, num3)


