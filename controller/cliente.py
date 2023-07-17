#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir( nomecliente, sexocliente, cpf, endereço, telefone, especiedeanimal, raçamultaçãoanimal, idadedoanimal, sexoanimal):
    db.cur.execute("""
                   INSERT into public.tbclinica_petshop (nomecliente, sexocliente, cpf, endereço, telefone, especiedeanimal, raçamultaçãoanimal, idadedoanimal, sexoanimal)
                   VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')
                   """ % (nomecliente, sexocliente, cpf, endereço, telefone, especiedeanimal, raçamultaçãoanimal, idadedoanimal, sexoanimal
                ))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM tbclinica_petshop
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows
#função para excluir registro no banco de dados
def excluir(nomecliente):
    db.cur.execute("""
                   DELETE FROM tbclinica_petshop WHERE nomeCliente = '%s'
                   """ % (nomecliente))
    db.con.commit()