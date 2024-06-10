def determiner_statut(age):
    if age >= 18:
        return "majeur"
    else:
        return "mineur"

def main():
   annee_de_naissance = int(input("Veuillez entrer votre année de naissance : ")) 
   age = 2024 - annee_de_naissance
   statut = determiner_statut(age)
   print("Vous êtes", statut)

if __name__ == "__main__":
    main()