"""
Enum centralizado para perfis de usuário.

Este módulo define o Enum Perfil que é a FONTE ÚNICA DA VERDADE
para perfis de usuário no sistema.
"""

from util.enum_base import EnumEntidade


class Perfil(EnumEntidade):
    ADMIN = "Administrador"
    AUTOR = "Autor"
    LEITOR = "Leitor"
