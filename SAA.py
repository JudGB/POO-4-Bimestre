from classes import *
from exceptions import *
import time
import string
import sys

# 2º Ano B Vespertino Informática
# Alunos:
# André Luís Bento Ferreira
# Celso Hector Silva Sales
# Luiz Felipe Macedo Alencar de Menezes
# Judson Gabriel Ferreira dos Santos

usuarios = []
dias = []
albtMai = list(string.ascii_uppercase + " ÁÃÂÉÊÔÕÍ")
albtMin = list(string.ascii_lowercase + " áãâéêôõí")
DDDs = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "21", "22", "24", "27", "28", "31", "32", "33", "34", "35", "37", "38", "41", "42", "43", "44", "45", "46", "47", "48", "49", "51", "53", "54", "55", "61", "62", "64", "65", "66", "67", "68", "69", "71", "73", "74", "75", "77", "79", "81", "82", "83", "84", "85", "86", "87", "88", "89", "91", "92", "93", "94", "95", "96", "97", "98", "99"]

# Home
def home():
    option = int(input("\n1- Login | 2- Registrar | 0- Sair: "))
    if option == 1:
        acesso()
    elif option == 2:
        registrar()
    elif option == 0:
        print("Saindo... Até a próxima!")
        sys.exit()
    else:
        print("Escolha uma opção válida.")
        home()

# Função de verificão do dia
def verificacaoDIA(data):
    for datas in dias:
        if datas == data:
            return True
    return False

# Função de verificação do email
def verificacaoEMAIL(email):
    for user in usuarios:
        if user["objeto"].getEmail() == email:
            return True
    return False


# Função de verificação do telefone
def verificacaoTELEFONE(telefone):
    for user in usuarios:
        if user["objeto"].getTelefone() == telefone:
            return True
    return False


# Função de verificação do cpf
def verificacaoCPF(cpf):
    for user in usuarios:
        if user["objeto"].getCpf() == cpf:
            return True
    return False


# Função de verificação da matrícula
def verificar_matricula(matricula):
    for user in usuarios:
        if user["tipo"] == "1" and user["objeto"].getmatricula() == matricula:
            return True
    return False


# Escolha de Curso
def escolher_curso():
    print("\nEscolha seu curso técnico integrado:")
    print("1- Informática")
    print("2- Química")
    print("3- Eletrotécnica")
    print("4- Edificações")
    while True:
        try:
            opcao = int(input("Escolha de 1-4: "))
            if opcao == 1:
                return "Informática"
                
            elif opcao == 2:
                return "Química"

            elif opcao == 3:
                return "Eletrotécnica"

            elif opcao == 4:
                return "Edificações"

            else:
                print("Insira uma opção válida")

        except:
            print("Insira um valor válido")


def marcarAtendimento(aluno, professor):  # vai ter q receber o professor e o aluno como parametro aqui
    if aluno.getcurso() != professor.getcurso():
        curso = input("Qual o curso que vai estar relacionado ao atendimento marcado?")
    else:
        curso = aluno.getcurso()

    materia = professor.getmateria()
    print(f"{materia}")

    sair = False
    while True:
        if sair == True:
            break
        try:
            atendimentomarcar = int(input("Você quer marcar um atendimento?\n 1 - Sim \n 0 - Não\n R: "))

            if atendimentomarcar == 0:
                print("Saindo...")
                sair = True
                break

            elif atendimentomarcar == 1:
                dia, mes, ano = input("Quer marcar seu atendimento para qual dia? ").split("/")
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
                dia1 = date(ano, mes, dia)
                data = f"{dia}/{mes}/{ano}"
                print(dia1, data)
                var = calendar.day_name[dia1.weekday()]

                if verificacaoDIA(data):
                    print("Dia já cadastrado")
                    print("Veja os dias já cadastrados")
                    for datas in dias:
                        print(f"================= {datas} =================")

                else:
                    dias.append(data)
                    if var == "Monday":
                        print(f"Nova data marcada para: Segunda-Feira, {data}")
                        print(dias)

                    elif var == "Tuesday":
                        print(f"Nova data marcada para: Segunda-Feira, {data}")
                        print(dias)

                    elif var == "Wednesday":
                        print(f"Nova data marcada para: Segunda-Feira, {data}")
                        print(dias)

                    elif var == "Thursday":
                        print(f"Nova data marcada para: Segunda-Feira, {data}")
                        print(dias)

                    elif var == "Friday":
                        print(f"Nova data marcada para: Segunda-Feira, {data}")
                        print(dias)

        except:
            print("Insira um valor válido.")

    while True:
        try:
            horario = int(input(f"Escolha o horário desejado (9h-12h / 14h-19h) - escreva apenas o número: "))
            if 9 <= horario <= 12:
                print(f"Horário marcado para às {horario}h.")
                break
            elif 14 <= horario <= 19:
                print(f"Horário marcado para às {horario}h.")
                break

            elif horario == 13:
                print("Horário de almoço.\n")
                continue

            else:
                print("Horário inválido.\n")
                continue


        except:
            print("Insira números!\n")

    atendimento = Atendimento(curso, materia, horario, data, professor, aluno)
    professor.adicionarAtendimentos(atendimento)
    aluno.adicionarAtendimentos(atendimento)

# Registro
def registrar():
    print("\nVocê é: 1- Aluno | 2- Professor | 3- Administrador | 0- Voltar")
    tipo = input("Escolha uma opção: ")

    if tipo == "0":
        home()

    if tipo != "1" and tipo != "2" and tipo != "3":
        print("Valor inválido. Escolha de 1-3.")
        registrar()

# Nome
    while True:
        try:
            nome = str(input("Digite seu nome: "))
            nome = nome.strip()
            if not all(carac in albtMin or carac in albtMai for carac in nome):
                raise ValueError

            elif nome == "":
                raise NomeEspacoError

            else:
                break

        except ValueError:
            print ("Nome inválido (Deve-se usar apenas letras)")

        except NomeEspacoError:
            print ("O nome não pode ser apenas um espaço")

        except:
            print ("Ocorreu um erro")

# Idade
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if tipo == "1":
                if idade <= 14 or idade >= 21:
                    print("\nInsira uma idade válida (Maior que 14 e menor que 21)\n")
                
                else: 
                    break
            
            elif tipo == "2" or tipo == "3":
                if idade <= 18 or idade >= 75:
                    print("\nInsira uma idade válida (Maior que 18 e menor que 75)\n")

                else: 
                    break
        except:
            print("Insira um número!")

# CPF
    while True:
        try:
            cpf = str(input("Digite seu CPF: (no formato XXX.XXX.XXX-XX): "))
            cpfNums = cpf.replace(".", "").replace("-", "")
            if verificacaoCPF(cpf):
                print("\nCPF já registrado. Tente novamente.\n")
                continue

            if not cpfNums.isdigit():
                raise ValueError
            
            if len(cpfNums) != 11:
                raise TamanhoError

            if not (cpf[3] == "." and cpf[7] == "." and cpf[11] == "-"):
                raise FormatacaoError

            else:  
                break

        except TamanhoError:
            print ("Cpf deve conter 11 números")

        except ValueError:
            print ("O Cpf deve conter apenas números.")

        except FormatacaoError:
            print ("Digite o Cpf no formato (XXX.XXX.XXX-XX)")

        except:
            print ("Ocorreu um erro")

# Email
    while True:
        try:
            email = input("Digite seu email: ")
            email = email.strip()
            if verificacaoEMAIL(email):
                print("\nEmail já registrado. Tente novamente.\n")
                continue
            
            elif "@" not in email or "." not in email:
                raise FormatacaoError

            elif email.index("@") == 0:
                raise EmailSemUsuarioError

            else:
                break
        
        except FormatacaoError:
            print ("O email deve conter '@' e '.'")

        except EmailSemUsuarioError:
            print ("Seu email deve conter um usuário")

# Telefone
    while True:
        try:
            telefone = input("Digite seu telefone (no formato (XX)XXXXX-XXXX)): ")
            if verificacaoTELEFONE(telefone):
                print("\nTelefone já registrado. Tente novamente.\n")
                continue
            
            telNums = telefone.replace("(", "").replace(")", "").replace("-", "")
            ddd = telNums[0] + telNums[1]
            if not telNums.isdigit():
                raise ValueError

            if not (telefone[0] == "(" and telefone[3] == ")" and telefone[9] == "-"):
                raise FormatacaoError
                        
            elif len(telNums) != 11:
                raise TamanhoError

            elif ddd not in DDDs:
                raise DddError

            else:  
                break

        except TamanhoError:
            print ("O telefone deve conter 11 números")

        except ValueError:
            print ("O telefone deve conter apenas números (Sem espaços).")

        except FormatacaoError:
            print ("Digite o telefone no formato (XXX.XXX.XXX-XX)")

        except DddError:
            print ("DDD Inválido")

        except:
            print ("Ocorreu um erro")

# PCD
    while True:
        try:
            pcdAsk = int(input("\nVocê é uma Pessoa com Deficiência?\n1- Sim\n2- Não\nR: "))
            if pcdAsk == 1:
                while True:         
                    try: 
                        qualpcd = input("\nQual sua deficiência?\nSiga o exemplo: 'Possuo deficiência <deficiência>'\nR: ")
                        pcd = qualpcd.split("Possuo ")
                        pcd = pcd[1]
                        pcd = "Possui " + pcd
                        break

                    except:
                        print ("Ocorreu um erro, tente novamente.")

            elif pcdAsk == 2:
                break

            else:
                print("Opção incorreta!")

            break
        except:
            print("insira uma Opcção!")

# Usuário
    usuario = input("\nDigite seu usuário: ")
    for user in usuarios:
        if user["usuario"] == usuario:
            print("O usuário informado já existe. Tente novamente.")
            registrar()

# Senha
    while True:
        senha = input("Digite sua senha: ")
        if len(senha) < 6:
            print("A senha deve conter no mínimo 6 caracteres. Tente novamente.")

        else:
            break

# Confirmando senha
    while True:
        senha1 = input("Confirme sua senha: ")
        time.sleep(0.5)
        if senha != senha1:
            print("As senhas não coincidem. Tente novamente.")

        else:
            break

# Aluno
    if tipo == "1":
        while True:
            try:
                # Matricula
                matricula = int(input("Digite sua matrícula: "))
                if verificar_matricula(matricula):
                    print("Matrícula já registrada. Tente novamente.")
                    continue

                else:
                    break

            except:
                print("Insira um número!")

        curso = escolher_curso()
        novo_usuario = Aluno(nome, idade, cpf, email, telefone, matricula, curso)

# Professor
    elif tipo == "2":
        curso = escolher_curso()  # definindo o curso
        try:
            novo_usuario = Prof(nome, idade, cpf, email, telefone, curso)

        except:
            print ("\nOcorreu um erro\n")

        finally:
            print ("Trabalho em processo (Talvez Eternamente) ;()") 
            sys.exit()

# Adiministrador
    elif tipo == "3":
        novo_usuario = Adm(nome, idade, cpf, email, telefone)

    else:
        print("Opção inválida. Tente novamente.")
        registrar()

    try:
        usuarios.append({"usuario": usuario, "senha": senha, "tipo": tipo, "objeto": novo_usuario})
        print("Registro realizado com sucesso.\n")
        time.sleep(0.5)
        print("Redirecionando para o login...\n")
        time.sleep(1)
        acesso()

    except:
        acesso()

    finally:
        print ("\nTrabalho em processo (Talvez Eternamente) ;)\n")

# Acesso
def acesso():
    time.sleep(0.5)
    print("(digite 0 se quiser retornar ao menu)")
    time.sleep(0.5)
    usuario = input("Digite seu usuário: ")
    if usuario == "0":
        home()

    senha = input("Digite sua senha: ")

    dados_usuario = None  # definindo os dados do usuario no login // felipe
    for user in usuarios:
        if user["usuario"] == usuario and user["senha"] == senha:
            dados_usuario = user
            break

# Acesso Aluno
    if dados_usuario:
        tipo_usuario = "Aluno" if dados_usuario["tipo"] == "1" else "Professor" if dados_usuario["tipo"] == "2" else "Administrador"
        if dados_usuario["tipo"] == "1":
            nome_pessoa = dados_usuario["objeto"].getNome()
            idade_pessoa = dados_usuario["objeto"].getIdade()
            cpf_pessoa = dados_usuario["objeto"].getCpf()
            email_pessoa = dados_usuario["objeto"].getEmail()
            telefone_pessoa = dados_usuario["objeto"].getTelefone()
            print("Login realizado!\n")
            time.sleep(0.7)
            print(f"Olá, {tipo_usuario} {nome_pessoa} ")
            time.sleep(0.5)
            while True:
                try:
                    menu = int(input("1- Exibir dados gerais do perfil\n2- Marcar atendimento\n3- Consultar atendimentos\n4- Logout\n5- Sair\nR: "))
                    if menu == 1:
                        time.sleep(0.7)
                        print ("\n--- Aluno ---")
                        print (f"Nome: {nome_pessoa}")
                        print (f"Idade: {idade_pessoa}")
                        print (f"Cpf: {cpf_pessoa}")
                        print (f"Email: {email_pessoa}")
                        print (f"Telefone: {telefone_pessoa}\n")
                        time.sleep(0.7)

                    if menu == 2:
                        raise EmProcessoError
                        marcarAtendimento()

                    if menu == 3:
                        raise EmProcessoError

                    if menu == 4:
                        raise EmProcessoError

                    if menu == 5:
                        sys.exit()

                except EmProcessoError:
                    time.sleep(0.7)
                    print ("\nTrabalho em processo (Talvez Eternamente) ;)\n")
                    time.sleep(0.7)

# Acesso Professor
        elif dados_usuario["tipo"] == "2":
            nome_pessoa = dados_usuario["objeto"].getNome()
            idade_pessoa = dados_usuario["objeto"].getIdade()
            cpf_pessoa = dados_usuario["objeto"].getCpf()
            email_pessoa = dados_usuario["objeto"].getEmail()
            telefone_pessoa = dados_usuario["objeto"].getTelefone()
            print("Login realizado!\n")
            time.sleep(0.7)
            print(f"Olá, {tipo_usuario} {nome_pessoa} ")
            time.sleep(0.5)
            while True:
                try:
                    menu = int(input("1- Exibir dados gerais do perfil\n2- Marcar atendimento\n3- Consultar atendimentos\n4- Logout\n5- Sair\nR: "))
                    if menu == 1:
                        time.sleep(0.7)
                        print ("\n--- Professor ---")
                        print (f"Nome: {nome_pessoa}")
                        print (f"Idade: {idade_pessoa}")
                        print (f"Cpf: {cpf_pessoa}")
                        print (f"Email: {email_pessoa}")
                        print (f"Telefone: {telefone_pessoa}\n")
                        time.sleep(0.7)

                    if menu == 2:
                        raise EmProcessoError
                        marcarAtendimento()
                    
                    if menu == 3:
                        raise EmProcessoError
                    
                    if menu == 4:
                        raise EmProcessoError
                    
                    if menu == 5:
                        sys.exit()
                
                except EmProcessoError:
                    time.sleep(0.7)
                    print ("\nTrabalho em processo (Talvez Eternamente) ;)\n")
                    time.sleep(0.7)

# Acesso Administrador
        elif dados_usuario["tipo"] == "3":
            nome_pessoa = dados_usuario["objeto"].getNome()
            idade_pessoa = dados_usuario["objeto"].getIdade()
            cpf_pessoa = dados_usuario["objeto"].getCpf()
            email_pessoa = dados_usuario["objeto"].getEmail()
            telefone_pessoa = dados_usuario["objeto"].getTelefone()
            print("Login realizado!\n")
            print(f"Olá, {tipo_usuario} {nome_pessoa} ")
            time.sleep(0.5)
            while True:
                try:
                    menu = int(input("1- Exibir dados gerais do perfil\n2- Marcar atendimento\n3- Consultar atendimentos\n4- Logout\n5- Sair\nR: "))
                    if menu == 1:
                        time.sleep(0.7)
                        print ("\n--- Administrador ---")
                        print (f"Nome: {nome_pessoa}")
                        print (f"Idade: {idade_pessoa}")
                        print (f"Cpf: {cpf_pessoa}")
                        print (f"Email: {email_pessoa}")
                        print (f"Telefone: {telefone_pessoa}\n")
                        time.sleep(0.7)

                    if menu == 2:
                        raise EmProcessoError
                        marcarAtendimento()
                    
                    if menu == 3:
                        raise EmProcessoError
                    
                    if menu == 4:
                        raise EmProcessoError
                    
                    if menu == 5:
                        sys.exit()
                
                except EmProcessoError:
                    time.sleep(0.7)
                    print ("\nTrabalho em processo (Talvez Eternamente) ;)\n")
                    time.sleep(0.7)

    else:
        print("\nUsuário ou senha incorretos.")
        acesso()

# Saída
def saida():
    print("\nDigite 0 para sair ou 1 para voltar ao menu principal.")
    escolha = int(input("Escolha uma opção: "))
    try:
        if escolha == 1:
            home()
        elif escolha == 0:
            print("Saindo... Até a próxima!")
            sys.exit()

    except:
        print("Escolha uma opção válida.")
        saida()

    finally:
        print("Finalizando saída.")


print("Bem-vindo ao SAA - Sistema de Atendimento ao Aluno\nIFRO Campus Calama - Técnico Integrado")
home()