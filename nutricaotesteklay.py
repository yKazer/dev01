espadas  = {
    "Madeira": {
        "Você precisa de": "1x Graveto e dois blocos de madeira",
    "Diamante": {
        "Você precisa de": "1x Graveto e dois diamantes",
    "Ferro": {
        "Você precisa de": "1x Graveto e dois ferros",
        
    }
    }
    }
}

como_fazer_espada = input("Qual o tipo da sua espada?: ")

if como_fazer_espada == "Madeira":
    print(espadas[0])
elif como_fazer_espada == "Diamante":
    print(espadas[1])
elif como_fazer_espada == "Ferro":
    print(espadas[2])

else:
    print("Tipo de espada não encontrado!")