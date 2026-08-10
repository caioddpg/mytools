def pi_real(entrada):
    try:
        if entrada == "0":
            print(3)
        else:
            print("3,"+PI_INT[:int(entrada)])
    except:
        print("entrada inválida")

def e_real(entrada):
    try:
        if entrada == "0":
            print(2)
        else:
            print("2,"+E_INT[:int(entrada)])
    except:
        print("entrada inválida")



PI_INT = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
E_INT = "7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274"


