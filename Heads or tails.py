import random

def heads_or_tails():
    opcoes = ["Heads", "Tails"]
    escolha_usuario = input("Choose heads or tails : ")
    
    escolha_computador = random.choice(opcoes)
    
    print(f"You choose: {escolha_usuario}")
    print(f"The IA choose: {escolha_computador}")
    
    if escolha_usuario == escolha_computador:
        print("You win!")
    else:
        print("You lose!")

heads_or_tails()
