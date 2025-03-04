import pandas 
from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD
from script.utils import le_dados

capacidades = [50, 30]
p , v = le_dados('data001.xlsx')

itens = ['Item_' + str(i + 1) for i in range(len(p))]
mochilas = ['Mochila_' + str(i+1) for i in range(len(capacidades))]

#Definição do Objeto 
model = LpProblem('mochila_multipla', LpMaximize)

# Variavel de Decisão
x = {(i, m): LpVariable(name=f'x_{i}_{m}', cat = 'Binary') for i in range(len(itens)) for m in range(len(mochilas))}

# Definição da Função Objetivo
model += sum(p[i] * x[i, m] for i in range(len(itens)) for m in range(len(mochilas)))

# Restrição 1: Capacidade das Mochilas
for m in range(len(mochilas)):
    model += sum(p[i] * x[i, m] for i in range(len(itens))) <= capacidades[m]

# Restrição 2: Um item não pode estar em duas mochilas
for i in range(len(itens)):
    model += sum(x[i,m] for m in range(len(mochilas))) <= 1

solver = PULP_CBC_CMD(msg=False)
model.solve(solver)

print('Itens Selecionados:')
for m in range(len(mochilas)):
    print(f'\n {mochilas[m]}')
    peso_total = 0 
    valor_total = 0
    for i in range(len(itens)):
        if x[i,m].value() == 1:
            print(f' - {itens[i]} (Peso: {p[i]} KG, Valor: R$ {v[i]})')
            peso_total += p[i]
            valor_total += v[i]
    print(f'\nPeso Total: {peso_total:.02f} KG')
    print(f'Valor Total: R$ {valor_total:.02f}')
