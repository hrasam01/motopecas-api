import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from app.dto.validators import validar_cpf, validar_cnpj


class TestValidarCPF:

    def test_cpf_valido(self):
        assert validar_cpf("529.982.247-25") == "52998224725"

    def test_cpf_valido_sem_mascara(self):
        assert validar_cpf("52998224725") == "52998224725"

    def test_cpf_digitos_iguais(self):
        with pytest.raises(ValueError, match="CPF inválido"):
            validar_cpf("111.111.111-11")

    def test_cpf_tamanho_invalido(self):
        with pytest.raises(ValueError, match="CPF deve ter 11 dígitos"):
            validar_cpf("123.456.789-0")

    def test_cpf_com_caracteres_especiais(self):
        with pytest.raises(ValueError, match="CPF deve ter 11 dígitos"):
            validar_cpf("abc.def.ghi-jk")


class TestValidarCNPJ:

    def test_cnpj_valido(self):
        assert validar_cnpj("06.215.096/0001-91") == "06215096000191"

    def test_cnpj_valido_real(self):
        assert validar_cnpj("89462776000137") == "89462776000137"

    def test_cnpj_digitos_iguais(self):
        with pytest.raises(ValueError, match="CNPJ inválido"):
            validar_cnpj("11.111.111/1111-11")

    def test_cnpj_tamanho_invalido(self):
        with pytest.raises(ValueError, match="CNPJ deve ter 14 dígitos"):
            validar_cnpj("11.222.333/0001-4")

    def test_cnpj_invalido(self):
        with pytest.raises(ValueError, match="CNPJ inválido"):
            validar_cnpj("00.000.000/0000-00")
