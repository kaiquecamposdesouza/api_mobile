import psycopg2
    
class Seleciona():

    def start(self):
        con = psycopg2.connect(host='ec2-107-22-83-3.compute-1.amazonaws.com', database='d6ror24c3d0r04',
                       user='grszehrcqoeofv', password='fe7ee4089879623a5b959fdd204a174f84e18d2af1c35133cc6d0502eb6c5399')
        return con 
    
    def selec_agendamento_banho_tosa(self, con):
        dados=[]
        Cursor_seleciona = con.cursor()
        Cursor_seleciona.execute("""select
                                    bt.id,
                                    Pet.nome,
                                    P.nome,
                                    bt.data,
                                    bt.horario,
                                    F.nome,
                                    bt.servico
                                    from agenda_banho_tosa as bt
                                    inner join Proprietario as P
                                    on bt.proprietario = P.id 
                                    inner join Pet 
                                    on bt.pet = Pet.numero_ficha
                                    inner join Funcionarios as F
                                    on bt.funcionario = F.cpf""")
        for item in Cursor_seleciona:
            dados.append(item)
        con.close()

        return dados
    
    def selec_usuarios(self, con):
        dados=[]
        Cursor_seleciona = con.cursor()
        Cursor_seleciona.execute("SELECT * FROM Usuarios")
        for item in Cursor_seleciona:
            dados.append(item)
        con.close()

        return dados
        