def main():
    espada = {

    "madeira": "Você precisa de 1x Graveto e dois blocos de madeira",
    "diamante": "Você precisa de 1x Graveto e dois diamantes",
    "ferros": "Você precisa de 1x Graveto e dois ferros",
    "netherites": "Você precisa de 1x Graveto e duas netherites"
    
    }

    Pergunte = input("Qual o tipo da picareta? ").lower()
   
    if Pergunte in espada:
        print(f"{espada[Pergunte]}")
    else:
        print("fodase")
main()
