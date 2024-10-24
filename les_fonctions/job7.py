def langage(x):
    if x == "JavaScript":
        print("Tu es un développeur web !")
    elif x == "Python":
        print("Tu es un dévéloppeur IA !")
    elif x == "java":
        print("Tu es un développeut logiciel !")
    elif x == "reactjs":
        print("Tu es un développeur mobile !")
    elif x == 0:
        print("Un jour, je serais le meilleur développeur...")
    else:
        return


langage("Python")
langage("JavaScript")
langage("reactjs")
langage(0)