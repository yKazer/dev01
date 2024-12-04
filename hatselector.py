## Escolher um personagem do harry potter:

personagem = input("Escolha um personagm: ").title()

## Se for tal personagem, sua casa é tal tal:
  
if personagem == "Harry Potter" or personagem == "Hermione Granger" or personagem == "Bony Weasley":
    print("Grifinória")
elif personagem == "Draco Malfoy":
   print("Sonserina")
elif personagem == "Luna Lovegood":
    print("Corvinal")
elif personagem == "Cedric Diggory":
    print("Lufa-Lufa")
else:
    print("personagem não encotrado")