nota = int(input("Qual é sua nota? "))

if nota == 100:
    print("Sua nota é (você é muito fodástico): A")
elif nota > 100:
    print("Porra, você é o cara, eitxa bobaaaa")
elif nota < 100 and nota > 90:
    print("Sua nota é: B")
else:
    print("Sua nota é: F")

    