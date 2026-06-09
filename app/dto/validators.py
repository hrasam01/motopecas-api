import re


def validar_cpf(cpf: str) -> str:
    cpf = re.sub(r"\D", "", cpf)

    if len(cpf) != 11:
        raise ValueError("CPF deve ter 11 dígitos")

    if cpf == cpf[0] * 11:
        raise ValueError("CPF inválido")

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[9]):
        raise ValueError("CPF inválido")

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[10]):
        raise ValueError("CPF inválido")

    return cpf


def validar_cnpj(cnpj: str) -> str:
    cnpj = re.sub(r"\D", "", cnpj)

    if len(cnpj) != 14:
        raise ValueError("CNPJ deve ter 14 dígitos")

    if cnpj == cnpj[0] * 14:
        raise ValueError("CNPJ inválido")

    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cnpj[i]) * pesos1[i] for i in range(12))
    resto = soma % 11
    dig1 = 0 if resto < 2 else 11 - resto
    if dig1 != int(cnpj[12]):
        raise ValueError("CNPJ inválido")

    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cnpj[i]) * pesos2[i] for i in range(13))
    resto = soma % 11
    dig2 = 0 if resto < 2 else 11 - resto
    if dig2 != int(cnpj[13]):
        raise ValueError("CNPJ inválido")

    return cnpj
