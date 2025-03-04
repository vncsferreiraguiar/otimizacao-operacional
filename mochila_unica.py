import pandas 
from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD
from script.utils import le_dados

arquivo = 'data001.xlsx'
p, v = le_dados(arquivo)
capacidade = 50 

#Lista de Itens
itens = ['Item_' + str(i+1) for i in range(len(p))]

# Definição do Objeto
prob = LpProblem('MyProblem', LpMaximize)

x = {i: LpVariable(name=itens[i], cat='Binary') for i in range(len(itens))}

# Definição da Função Objetivo
prob += sum(v[i] * x[i] for i in range(len(itens)))

#Restrição Capacidade da Mochila
prob += sum(p[i] * x[i] for i in range(len(itens))) <= capacidade

prob.solve(PULP_CBC_CMD(msg=False))

peso_total = sum(p[i] * x[i].value() for i in range(len(itens)))

print('Itens Selecionados:')
for i in range(len(itens)):
    if x[i].value() == 1:
        print(f' - {itens[i]}')

print(f'\nValor Total: R$ {prob.objective.value()}') 
print(f'Peso Total: {peso_total} KG\n') 

