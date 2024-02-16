## Bootcamp Back-End Python e Django

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

## 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
# cursor.execute('CREATE TABLE alunos(id INT, nome VARCAHR(100), idade INT, curso VARCHAR(100));')

## 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1,"Isadora", 21, "matemática")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2,"Marianna", 21, "geologia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3,"Isaac", 21, "matemática")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4,"Monica", 21, "matemática")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5,"Marcos", 31, "engenharia")')

#3. Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
    #dados = cursor.execute('SELECT * FROM alunos')

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
    #dados = cursor.execute('SELECT * FROM alunos WHERE idade > 20')


#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
    # dados = cursor.execute('SELECT * FROM alunos WHERE curso = "engenharia" ORDER BY nome ASC')

#for alunos in dados :
    #print(alunos)

# d) Contar o número total de alunos na tabela

# Executar a consulta
#tot_alunos = cursor.execute('SELECT COUNT(*) FROM alunos')

# Buscar o resultado
#resultado = cursor.fetchone()

# Extrair o valor do resultado
#tot_alunos = resultado[0]

# Imprimir o número total de alunos na tabela
#print(tot_alunos)

# 4. Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela.
#cursor.execute('UPDATE alunos SET idade  = 3 WHERE nome="Isaac"')

# b) Remova um aluno pelo seu ID.
#cursor.execute('DELETE FROM alunos WHERE id = 1')

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

# cursor.execute('CREATE TABLE clientes(id INT, nome VARCAHR(100), idade INT, saldo FLOAT);')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1,"Isadora", 21, 5000)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2,"Marianna", 27, 100.25)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3,"Isaac", 21, 100000.5)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4,"Monica", 21, 20000)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (5,"Marcos", 31, 50000.25)')

#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
#dados = cursor.execute('SELECT nome,idade FROM clientes WHERE idade > 30')

#for clientes in dados :
#    print(clientes)

#b) Calcule o saldo médio dos clientes.

#cursor.execute('SELECT AVG(saldo) as saldo_medio FROM clientes')

# Buscar o resultado
#resultado = cursor.fetchone()

# Extrair o valor do resultado
#saldo_medio = resultado[0]

# Imprimir o número total de alunos na tabela
#print(saldo_medio)

#c) Encontre o cliente com o saldo máximo.
# Executar a consulta para encontrar o cliente com o saldo máximo
#cursor.execute('SELECT nome FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')

# Recuperar o resultado da consulta
#resultado = cursor.fetchone()

# Verificar se o resultado não é nulo antes de acessá-lo
#if resultado:
#    nome_cliente_max_saldo = resultado[0]
#    print("O cliente com o saldo máximo é:", nome_cliente_max_saldo)
#else:
#    print("Nenhum cliente encontrado.")

#d) Conte quantos clientes têm saldo acima de 1000.
#cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')

# Recuperar o resultado da consulta
#resultado = cursor.fetchone()

# Verificar se o resultado não é nulo antes de acessá-lo
#if resultado:
#    tot_cliente_saldo_acima = resultado[0]
#    print("A quantidade de clientes com o saldo acima de 1000 é:", tot_cliente_saldo_acima)
#else:
#    print("Nenhum cliente encontrado.")


#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
#cursor.execute('UPDATE clientes SET saldo = 150.25 WHERE nome="Marianna"')
    
#b) Remova um cliente pelo seu ID.
#cursor.execute('DELETE FROM clientes WHERE id = 1')

#8. Junção de Tabelas
# Crie uma segunda tabela chamada "compras" com os campos: id(chave primária), cliente_id (chave estrangeira referenciando o id
# da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes".

#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

# cursor.execute('CREATE TABLE compras(id INT, cliente_id INT, produto VARCAHR(100), valor FLOAT);')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (1,2,"Fogão",2000)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (2,2,"Geladeiro",2500)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (3,3,"Sofá",5000)')

dados = cursor.execute('SELECT c.nome, co.produto, co.valor FROM clientes c RIGHT JOIN compras co ON c.id = co.cliente_id')

for clientes in dados :
    print(clientes)

conexao.commit()
conexao.close

