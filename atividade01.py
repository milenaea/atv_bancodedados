import sqlite3

conexao = sqlite3.connect('baquinho')
cursor = conexao.cursor()

#1.Crie uma tabela chamada "alunos" com os seguintes campos:id(inteiro),nome(texto),idade(inteiro)ecurso(texto)

cursor.execute('CREATE TABLE alunos (id INTEGER, Nome TEXT, Idade INTEGER, Curso TEXT);')

#2.Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior

cursor.execute('INSERT INTO alunos(id, Nome,Idade,Curso) VALUES (1, "Marina",17,"Contabilidade")')
cursor.execute('INSERT INTO alunos(id, Nome,Idade,Curso) VALUES (2, "Luciana ",22,"Direito")')
cursor.execute('INSERT INTO alunos(id, Nome,Idade,Curso) VALUES (3, "Amarilís",19,"Filosofia")')
cursor.execute('INSERT INTO alunos(id, Nome,Idade,Curso) VALUES (4, "Rui",27,"Desing")')
cursor.execute('INSERT INTO alunos(id, Nome,Idade,Curso) VALUES (5, "Joaquim",19,"Engenharia")')
cursor.execute('INSERT INTO alunos(id, Nome,Idade,Curso) VALUES (6, "Diana",26,"Astrologia")')

#3.Consultas Básicas Escreva consultas SQL para realizar as seguintestarefas:
# a)Selecionar todos os registros da tabela"alunos".
#b)Selecionar o nome e a idade dos alunos com mais de 20 anos.
# c)Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
# d)Contar o número total de alunos na tabela


tabela =cursor.execute('SELECT * FROM alunos')
for usuario in tabela:
    print(usuario)

tabela =cursor.execute('SELECT nome,idade FROM alunos where idade>20')
for usuario in tabela:
    print(usuario)

tabela = cursor.execute(' SELECT * FROM alunos WHERE Curso = "Engenharia" ORDER BY nome')
for usuario in tabela:
      print(usuario)

tabela= cursor.execute(' SELECT COUNT(*) FROM alunos ')
for usuario in tabela:
    print(usuario)

#4.Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
#b) Remova um aluno pelo seu ID.

tabela= cursor.execute( 'UPDATE alunos SET idade = 18 WHERE idade = 17')
for usuario in tabela:
    print(usuario)

tabela = cursor.execute('DELETE FROM alunos where id=3')
for usuario in tabela:
    print(usuario)


#5.Criar uma Tabela e Inserir Dados Crie uma tabela chamada "clientes" com os campos:id(chaveprimária),nome(texto),idade(inteiro) e saldo(float).Insira alguns registros de clientes na tabela

cursor.execute('CREATE TABLE clientes (id INTEGER, Nome TEXT, Idade INTEGER, saldo FLOAT);')

cursor.execute('INSERT INTO clientes(id, Nome,Idade,Saldo) VALUES (1, "Joaquina",37,"9343")')
cursor.execute('INSERT INTO clientes(id, Nome,Idade,Saldo) VALUES (2, "Guilhermina",17,"530")')
cursor.execute('INSERT INTO clientes(id, Nome,Idade,Saldo) VALUES (3, "Marina",27,"730.33")')
cursor.execute('INSERT INTO clientes(id, Nome,Idade,Saldo) VALUES (4, "Joana",33,"5.530")')
cursor.execute('INSERT INTO clientes(id, Nome,Idade,Saldo) VALUES (5, "Talita",32,"33.90")')

#tabela02 =cursor.execute('SELECT * FROM clientes')
#for usuario in tabela02:
 #    print(usuario)


#6.Consultas e Funções Agregadas Escreva consultas SQL para realizar as seguintes tarefas:
#a)Selecione o nome e a idade dos clientes com idade superior a 30 anos.
# b)Calcule o saldo médio dos clientes.
# c)Encontre o cliente como saldo máximo.
# d)Conte quantos clientes têm saldo acima de 1000

tabela02 = cursor.execute('SELECT Nome, Idade FROM clientes WHERE idade>30')
for usuario in tabela02:
    print(usuario)

tabela02 = cursor.execute('SELECT AVG(saldo) AS saldo_mediO FROM clientes')
for usuario in tabela02:
    print(usuario)

tabela02 = cursor.execute('SELECT MAX(saldo) AS saldo_maximo FROM clientes')
for usuario in tabela02:
     print(usuario)

tabela02 = cursor.execute('SELECT COUNT(*) AS saldo_acima_1000 FROM clientes WHERE saldo>1000')
for usuario in tabela02:
     print(usuario)

#7.Atualização e Remoção com Condições 
# a)Atualize o saldo de um cliente específico.
# b)Remova um cliente pelo seu ID.

tabela02=cursor.execute('UPDATE clientes SET saldo = 1330 WHERE saldo = 730.33')
for usuario in tabela02:
    print(usuario)

tabela02=cursor.execute('DELETE FROM clientes WHERE id =1')
for usuario in tabela02:
    print(usuario)


#8.Junção de Tabelas Crie uma segunda tabela chamada "compras" com os campos:id(chaveprimária),cliente_id(chave estrangeira referenciando o id databela "clientes"), produto(texto) e valor(real).
# Insira algumas compras as sociadas a clientes existentes na tabela "clientes".
# Escreva uma consulta para exibir o nome do cliente,o produto e o valor de cada compra.

cursor.execute('CREATE TABLE compras (id INTEGER PRIMARY KEY, clientes_id INTEGER, produto TEXT,valor REAL,FOREIGN KEY (clientes_id) REFERENCES clientes(id));')

tabela03 = cursor.execute('SELECT * FROM compras')
for usuario in tabela03:
    print(usuario)


cursor.execute('INSERT INTO compras (id,clientes_id, produto, valor) VALUES(1,5,"sofá-cama",2399.00)')
cursor.execute('INSERT INTO compras (id, clientes_id, produto, valor) VALUES(2,3,"televisao",1399.00)')
cursor.execute('INSERT INTO compras (id, clientes_id, produto, valor) VALUES(3,2,"micoondas",299.00)')

tabela03 = cursor.execute('SELECT * FROM compras')
for usuario in tabela03:
  print(usuario)

tabela03= cursor.execute(' SELECT * FROM clientes INNER JOIN compras ON clientes.id = compras.clientes_id')
for usuario in tabela03:
    print(usuario)


conexao.commit()
conexao.close()