from rh.classes.Colaborador import Colaborador
<<<<<<< HEAD
from datetime import date


class Departamento:
    def __init__(
        self,
        nome_setor,
        nome_responsavel=None,
        dia=None,
        mes=None,
        ano=None
    ):
        self._nome_setor = nome_setor
        self._responsavel = nome_responsavel
        self._colaboradores = []
        self._hoje = date.today()

        try:
            self._aniversario_resp = date(ano, mes, dia)
        except TypeError:
            raise TypeError('Informe dia, mês e ano')
    @property
    def aniversario_resp(self):
        return self._aniversario_resp.isoformat()
=======


class Departamento:
    def __init__(self, nome_setor):
        self._nome_setor = nome_setor
        self._responsavel = None
        self._colaboradores = []

>>>>>>> e15e080a0e66e52565f7adba9129cc94334e41dd
    @property
    def nome(self):
        return self._nome_setor

    @nome.setter
    def nome(self, value):
        self._nome_setor = value

    @property
    def responsavel(self):
        if self._responsavel is None:
            return None
        return str(self._responsavel)

    @property
    def colaboradores(self):
        return self._colaboradores

    def informar_responsavel(self, nome, dia, mes, ano):
        self._responsavel = Colaborador(nome, dia, mes, ano)

    def add_colaborador(self, nome, dia, mes, ano):
        self._colaboradores.append(Colaborador(nome, dia, mes, ano))

<<<<<<< HEAD
    def aniversario_hoje(self):
        if Colaborador._aniversario.day == self._hoje.day:
            if Colaborador._aniversario.month == self._hoje.month:
                return True
        return False

=======
>>>>>>> e15e080a0e66e52565f7adba9129cc94334e41dd
    def verificar_aniversariantes(self):
        lista = []
        for colaborador in self.colaboradores:
            if colaborador.aniversario_hoje():
<<<<<<< HEAD
                lista.append((
                    colaborador.nome,
                    colaborador.aniversario,
                    self.nome))
        if Departamento.responsavel:
            if self._aniversario_resp.day == self._hoje.day:
                if self._aniversario_resp.month == self._hoje.month:
                    lista.append((
                        self.responsavel,
                        self.aniversario_resp,
                        self.nome))
=======
                lista.append((colaborador.nome, colaborador.aniversario))
>>>>>>> e15e080a0e66e52565f7adba9129cc94334e41dd
        return lista

    def __str__(self):
        return self._nome_setor

    def __repr__(self):
        return 'Departamento = ' + self._nome_setor
