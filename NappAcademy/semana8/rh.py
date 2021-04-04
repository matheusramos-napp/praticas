from rh.classes.Departamento import Departamento

from datetime import date, timedelta
dt1 = date.today() - timedelta(days=4)
hoje = date.today()

<<<<<<< HEAD
departamento = Departamento(
    'Departamento XYZ',
    'José da Silva',
    dt1.day,
    dt1.month, 1990
)

# departamento.informar_responsavel('José da Silva', dt1.day, dt1.month, 1990)
=======
departamento = Departamento('Departamento XYZ')
departamento.informar_responsavel('José da Silva', dt1.day, dt1.month, 1990)
>>>>>>> e15e080a0e66e52565f7adba9129cc94334e41dd
departamento.add_colaborador('João Oliveira', hoje.day, hoje.month, 1992)
departamento.add_colaborador('Pedro Mendonça', dt1.day, dt1.month, 1993)
departamento.add_colaborador('Luis Fernando', hoje.day, hoje.month, 2000)
departamento.add_colaborador('Maurício Souza', dt1.day, dt1.month, 1985)

<<<<<<< HEAD

=======
>>>>>>> e15e080a0e66e52565f7adba9129cc94334e41dd
aniversariantes = departamento.verificar_aniversariantes()

for aniversariante in aniversariantes:
    print('Parabéns ' + aniversariante[0] + ' pelo seu dia')
<<<<<<< HEAD

print(aniversariantes)
print(Departamento.aniversario_resp)
=======
>>>>>>> e15e080a0e66e52565f7adba9129cc94334e41dd
