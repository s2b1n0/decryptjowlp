import crypt

cryptSenha = input("Digite a senha cifrada:")
cryptSalt = input('Digite o salt:')

with open("rockyou.txt", "r") as wordlist:
    for key in wordlist:
        key = key.rstrip("\n")
        print("Testando " + key + "\r")
        comp = crypt.crypt(key, cryptSalt)
        if comp == cryptSenha:
            print("\r\n Senha descoberta " + key)
            exit()
