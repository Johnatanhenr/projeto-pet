import mysql.connector

conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='040515Thais.'
    )

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS petshop;")

cursor.execute("CREATE DATABASE petshop;")

cursor.execute("USE petshop")

# criando tabelas
TABLES={}

TABLES['cliente'] = ('''
    CREATE TABLE `petshop`.`cliente` (      
      `nome` VARCHAR(50) NOT NULL,
      `email` VARCHAR(10) NOT NULL,
      `cpf` VARCHAR(100) NOT NULL,
      PRIMARY KEY (`nickname`))
    ENGINE = InnoDB
    DEFAULT CHARACTER SET = utf8
    COLLATE = utf8_bin;  ''')


# inserindo cliente
cliente_sql = 'INSERT INTO cliente (nome, email, cpf) values (%s,%s,%s)'

cliente = [
    ("Tetris", "Puzzle@", "000000000000"),
    ("God of War", "Hack and Slash@", "11111111111"),
    ("Mortal Kombat I", "Luta@", "2222222222"),
    ("Need for Speed", "HCorrida@", "33333333333333"),
]

cursor.executemany(cliente_sql,cliente)

cursor.execute('select * from petshop.cliente')
print('---------------- cliente ----------------')
for cliente in cursor.fetchall():
    print(cliente[1])

# commitando pra gravar no banco
conn.commit()

cursor.close()
conn.close()