import calendar
from datetime import *
import time


# Celso, seguinte:
# 1- Na classe Atendimento, na def "editarData", ta quase tudo completo, o que tá quebrando é a questão
# da verificação, e eu precisava ver isso com mais calma contigo.
#
# 2- Uma observação sobre o "consultar atendimento", tanto do professor, tanto do aluno; assim como a gnt fez
# no login, registrando cada atributo de usuário, a gnt vai ter que fazer isso para o Atendimento também.
# Aí, vai criar um novo objeto, sla, "atendimentoCelso = Atendimento(bla bla bla)"... aí na hora da consulta,
# só faria o link né, entre o professor e o aluno (já que um atendimento é o atedimento do outro), só faz o
# print desse objeto.
#
# 3 - Cada pessoa (aluno, adm, professor), tem que ter uma interface diferente no menu. tipo, dps do login
# o aluno pode: fazer o atendimento e consultar o que eles tem; o professor não pode marcar, só consultar.
# tendeu?

class PessoaIFRO:  # mãe
    def __init__(self, nome: str, idade: int, cpf: int, email: str, telefone: str):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__pcd = None

    def getNome(self):
        return self.__nome

    def getPcd(self):
        return self.__pcd

    def getTelefone(self):
        return self.__telefone

    def setTelefone(self):
        print("Defina um novo telefone.")
        novotelefone = input("Telefone: ")
        self.__telefone = novotelefone

    def getIdade(self):
        return self.__idade

    def setIdade(self, idade):
        if idade > 10:
            self.__idade = idade

    def getCpf(self):
        return self.__cpf

    def getEmail(self):
        return self.__email

    def setEmail(self):
        print("Defina um novo email.")
        novoemail = input("Email: ")
        self.__email = novoemail

    def definindoPcd(self, pcd):
        self.__pcd = pcd

    def exibir(self):
        print(
            f"Meu nome: {self.__nome}\nIdade: {self.__idade}\nCPF: {self.__cpf}\nEmail: {self.__email}."
        )
class Prof(PessoaIFRO): #prof
    def __init__(self, nome: str, idade: int, cpf: int, email: str, telefone: str, curso: str, materia: str):
        self.__curso = curso
        self.__materia = materia    
        self.__atendimentos = []
        super().__init__(nome, idade, cpf, email,telefone)

    def adicionarAtendimentos(self,atendimento):
        self.__atendimentos.append(atendimento)

    def exibir(self):
        super().exibir()
        print(f"\n\nCurso: {self.__curso}.")

    def consultarAtendimento(self):
        print("Seu atendimento está [AQUI TEM QUE SER O OBJETO DA CLASE ATENDIMENTO OU ALGO ASSIM]...")

    def registrarHorario(self):
        print("continua ou descontinua")

    def getcurso(self):
        return self.__curso

    def getmateria(self):
        return self.__materia
        
class Adm(PessoaIFRO): #adm
    def __init__(self, nome: str, idade: int, cpf: int, email: str, telefone: str):
        super().__init__(nome, idade, cpf, email, telefone)

    def exibir(self):
        super().exibir()

class Aluno(PessoaIFRO): #aluno
    def __init__(self, nome: str, idade: int, cpf: int, email: str, telefone: str, matricula: str, curso: str):
        super().__init__(nome, idade, cpf, email, telefone)
        self.__matricula = matricula
        self.__curso = curso
        self.__atendimentos = []
        

    def adicionarAtendimentos(self,atendimento):
        self.__atendimentos.append(atendimento)
        
    def getmatricula(self):
        return self.__matricula

    def getcurso(self):
        return self.__curso

    def exibir(self):
        super().exibir()
        print("\nMatrícula: {self.__matricula}")


class Atendimento():
    def __init__(self, curso: str, materia: str, horario: str, data: str, professor, aluno):
        self.__curso = curso
        self.__materia = materia
        self.__horario = horario
        self.__data = data
        # Na linha abaixo está acontecendo a relação `trigger digger, skibidi n...`
        self.__professor = professor
        self.__aluno = aluno

    def getdata(self):
        return self.__data

    def editarHorario(self):
        print(f"Horário atual: {self.__horario}")
        print("\nEscolha seu novo horário:")
        print("1- 16h")
        print("2- 17h")
        print("3- 18h")
        print("4- 19h")
        novohorario = input("Escolha de 1-4: ")

        if novohorario == "1":
            return "16h"
        elif novohorario == "2":
            return "17h"
        elif novohorario == "3":
            return "18h"
        elif novohorario == "4":
            return "19h"
        else:
            print("Insira uma opção válida")

    def editarData(self):
        dias = []
        dias1 = []

        edtdata = input(
            "Você deseja editar a data do seu atendimento? Responda com `sim` ou `não`: "
        ).upper()

        if edtdata == "SIM":
            print("Ok. Escolha a data desejada.\n")
            while True:
                try:
                    dia, mes, ano = input("Digite a data no formato dd/mm/aaaa: ").split("/")
                    dia = int(dia)
                    mes = int(mes)
                    ano = int(ano)
                    dia1 = date(ano, mes, dia)
                    dia1_str = f"{dia}/{mes}/{ano}"

                    for data in dias:  # verificação do dia
                        if data["data"] == dia1_str:
                            print("A data informada já está agendada.")

                    else:
                        break

                except:
                    print("Insira uma data válida.")

            var = calendar.day_name[dia1.weekday()]

            if var == "Monday":
                print(f"Nova data marcada para: Segunda-Feira, {dia1_str}")
                dias.append({"dia": dia, "mes": mes, "ano": ano, "data": dia1_str})
                print(dias)

            elif var == "Tuesday":
                print(f"Nova data marcada para: Terça-Feira, {dia1_str}")
                dias.append({"dia": dia, "mes": mes, "ano": ano, "data": dia1_str})
                print(dias)

            elif var == "Wednesday":
                print(f"Nova data marcada para: Quarta-Feira, {dia1_str}")
                dias.append({"dia": dia, "mes": mes, "ano": ano, "data": dia1_str})
                print(dias)

            elif var == "Thursday":
                print(f"Nova data marcada para: Quinta-Feira, {dia1_str}")
                dias.append({"dia": dia, "mes": mes, "ano": ano, "data": dia1_str})
                print(dias)

            elif var == "Friday":
                print(f"Nova data marcada para: Sexta-Feira, {dia1_str}")
                dias.append({"dia": dia, "mes": mes, "ano": ano, "data": dia1_str})
                print(dias)

            elif var == "Saturday":
                print(f"Nova data marcada para: Sábado, {dia1_str}")
                dias.append({"dia": dia, "mes": mes, "ano": ano, "data": dia1_str})
                print(dias)

            elif var == "Sunday":
                print(f"Nova data marcada para: Domingo, {dia1_str}")
                dias.append({"dia": dia, "mes": mes, "ano": ano, "data": dia1_str})
                print(dias)

        elif edtdata == "NÃO" or edtdata == "NAO":
            print("Retornando ao menu...")
            time.sleep(0.5)
            print(".")

    def cancelarAtendimento(self):
        x = input("Você deseja cancelar seu atendimento? Responda com sim ou não: ").upper()
        if x == "SIM":
            print("Atendimento cancelado.")
        elif x == "NÃO" or x == "NAO":
            print("Cancelamento cancelado, retornando ao menu...")