class ExcecaoCPFInvalido(Exception):
    pass

def validandoCpf(CPF):
    if len(CPF)  != 11:
        print("\nseu cpf deve conter 11 digitos.")
        raise ExcecaoCPFInvalido()
    elif CPF.isnumeric() == False:
        print("\nseu cpf deve conter apenas números.")
        raise ExcecaoCPFInvalido()
    else:
        print("CPF válido")
        return True 