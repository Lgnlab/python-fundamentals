"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com os seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional) 
- Adicione também as docstrings
"""

def notas(*nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r["total"] = len(nota)
    r["maior"] = max(nota)
    r["menor"] = min(nota)
    r["média"] = sum(nota)/len(nota)
    if sit:
        if r["média"] >= 7:
            r["situação"] = "BOA"
        elif r["média"] >= 5:
            r["situação"] = "RAZOÁVEL"
        else:
            r["situação"] = "RUIM"
    return r


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)