from os import renames
from os import remove
def Ajouter_contact():
    Nom=input("Entrez le nom du contact \n")
    Prenom=input("Entrez le prenom \n")
    Tel=input("Entrez le tel ")
    MonFic=open("contact.txt","a",encoding="utf8")
    MonFic.write(Nom + "\n")
    MonFic.write(Prenom + "\n")
    MonFic.write(Tel + "\n")
    MonFic.close
def Lister():
    MonFic=open("contact.txt","r",encoding="utf8")
    Uneligne=MonFic.readline()
    while Uneligne!="":
        print(Uneligne)
        Uneligne=MonFic.readline()
def Modifier_contact():
    print("Que voulez vous modifier\n") 
    print("Tapez 1 pour le Nom")
    print("Taper 2 pour le Prenom")
    print("Tapez 3 pour le Tel")
    choix=int(input("Faites votre choix"))
    if choix==1:
        annom=input("Quelle est le nom à Modifier")
        nvnom=input("Quelle est le nouveau nom")
        MonFic=open("contact.txt","r",encoding="utf8")
        tempon=open("temp.txt","w",encoding="utf8")
        LigNom=MonFic.readline()
        LigPrenom=MonFic.readline()
        LigTel=MonFic.readline()
        while LigNom!="" or LigPrenom!="" or LigTel!="":
            if choix==1:
                annom=input("Quelle est le Nom à Modifier ")
                nvnom=input("Quelle est le nouveau Nom ")
                MonFic=open("contact.txt","r",encoding="utf8")
                tempon=open("temp.txt","w",encoding="utf8")
                LigNom=MonFic.readline()
                LigPrenom=MonFic.readline()
                LigTel=MonFic.readline()
                while LigNom!="" or LigPrenom!="" or LigTel!="":
                    if LigNom==annom:
                        tempon.write(nvnom+ "\n")
                        tempon.write(LigPrenom+ "\n")
                        tempon.write(LigTel+ "\n")
                    else:
                        tempon.write(nvnom+ "\n")
                        tempon.write(LigPrenom+ "\n")
                        tempon.write(LigTel+ "\n")
                   
                    LigNom=MonFic.readline()
                    LigPrenom=MonFic.readline()
                    LigTel=MonFic.readline()
        MonFic.close()
        tempon.close()
        remove("contact.txt")
        renames("temp.txt," "contact.txt")
    if choix==2:
                anprenom=input("Quelle est le Prenom à Modifier ")
                nvnom=input("Quelle est le nouveau prenom ")
                MonFic=open("contact.txt","r",encoding="utf8")
                tempon=open("temp.txt","w",encoding="utf8")
                LigNom=MonFic.readline()
                LigPrenom=MonFic.readline()
                LigTel=MonFic.readline()
                while LigNom!="" or LigPrenom!="" or LigTel!="":
                    if LigPrenom==annom:
                        tempon.write(nvnom+ "\n")
                        tempon.write(LigPrenom+ "\n")
                        tempon.write(LigTel+ "\n")
                    else:
                        tempon.write(LigNom+ "\n")
                        tempon.write(LigPrenom+ "\n")
                        tempon.write(LigTel+ "\n")
                   
                    LigNom=MonFic.readline()
                    LigPrenom=MonFic.readline()
                    LigTel=MonFic.readline()
                MonFic.close()
                tempon.close()
                remove("contact.txt")
                renames("temp.txt," "contact.txt")                
def Supprimer_contact():
   nom_contact=input("Donner le nom du contact à supprime \n")
   MonFic=open("contact.txt","r",encoding="utf8")
   tempon=open("temp.txt","w",encoding="utf8")
   LigNom=MonFic.readline()
   LigPrenom=MonFic.readline()
   LigTel=MonFic.readline() 
   while LigNom!="" or LigPrenom!="" or LigTel!="":
    print(LigNom)
    print(nom_contact)
    if (LigNom.strip()!=nom_contact):
        tempon.write(LigNom)
        tempon.write(LigPrenom)
        tempon.write(LigTel)
    LigNom=MonFic.readline()
    LigPrenom=MonFic.readline()
    LigTel=MonFic.readline()
MonFic.close()
tempon.close()
remove("contact.txt")
renames("temp.txt","contact.txt")
def Rechercher_contact():
    nom_contact=input("Donner le nom du contact à chercher\n")
    MonFic=open("contact.txt", "r",encoding="utf8")
    LigNom=MonFic.readline()
    LigPrenom=MonFic.readline()
    LigTel=MonFic.readline()
    t=0
    while LigNom!="" or LigPrenom!="" or LigTel!="":
        if (LigNom.strip()==nom_contact):
            print("Contact Trouvé :\n")
            print(LigNom)
            print(LigPrenom)
            print(LigTel)
            t=1
            LigNom=MonFic.readline()
        
