senha_correta = 6547
tentativas = 3
while tentativas > 0:
    senha_digitada = int(input("digite a senha: "))

    if senha_digitada == senha_correta:
        print("Senha correta. ")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Senha incorreta. Tente novamente voce ainda tem {tentativas} tentativas")
        else:
            print("Senha bloqueada. por excessos de tentativas")