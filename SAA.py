from classes import *  #importante nossas classes
import time #utilizando a biblioteca time, para usar o método sleep
from exceptCPF import *
usuarios = [] #coleção 1 
dias = [] #coleção 2 
dados_usuario = {} #coleção 3

# Home
def home():
    while True:
        try:
            option = int(input("\n1- Login | 2- Registrar | 0- Sair\nR: "))
            if option == 1:
                acesso()
            elif option == 2:
                registrar()
            elif option == 0:
                print("Saindo... Até a próxima!")
                exit()
            elif option < 0 or option > 2:
                raise ValueError
        except ValueError:
            print("\nDigite apenas *números* inteiros de 0 a 2.")
       
    
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
    time.sleep(0.5)
    opcao = input("Escolha de 1-4: ")
    time.sleep(0.5)
    if opcao == "1":
        return "Informática"
    elif opcao == "2":
        return "Química"
    elif opcao == "3":
        return "Eletrotécnica"
    elif opcao == "4":
        return "Edificações"
    else:
        print("Insira uma opção válida")
        return escolher_curso()


def marcarAtendimento(aluno, professor,profouAluno): 
    curso = aluno.getcurso()
    materia = input("Qual a matéria relacionada ao atendimento?\nR:")
    sair = False
    while True:
        if sair == True:
            break
        try:
            atendimentomarcar = int(input("Você quer marcar um atendimento?\n 1 - Sim \n 0 - Não\n R: "))

            if atendimentomarcar == 0:
                print("Saindo...")
                sair = True
            elif atendimentomarcar == 1:
                dia, mes, ano = input("Quer marcar seu atendimento para qual dia?\nModelo: 00/00/0000\nR: ").split("/")
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
                dia1 = date(ano, mes, dia)
                data = f"{dia}/{mes}/{ano}"
                var = calendar.day_name[dia1.weekday()]

                if verificacaoDIA(data) == True:
                    print("Dia já cadastrado")
                    print("Veja os dias já cadastrados")
                    for datas in dias:
                        print(f"================= {datas} =================")

                else:
                    dias.append(data)
                    if var == "Monday":
                        print(f"Nova data marcada para: Segunda-Feira, {data}")
                       

                    elif var == "Tuesday":
                        print(f"Nova data marcada para: Terça-Feira, {data}")


                    elif var == "Wednesday":
                        print(f"Nova data marcada para: Quarta-Feira, {data}")


                    elif var == "Thursday":
                        print(f"Nova data marcada para: Quinta-Feira {data}")

                    elif var == "Friday":
                        print(f"Nova data marcada para: Sexta-Feira, {data}")
                  

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
    if profouAluno == True:
        aluno.adicionarAtendimentos(atendimento)
    elif profouAluno == False:
        professor.adicionarAtendimentos(atendimento)
    
def verMyAtendimentos(pessoa):
    pessoa.consultarAtendimentos()

# Registro
def registrar():
    print("\nVocê é: 1- Aluno | 2- Professor | 3- Administrador | 0- Voltar")
    try:
        tipo = int(input("Escolha uma opção: "))
        if tipo != 1 and tipo != 2 and tipo != 3 and tipo != 0:
            print("Valor inválido. Escolha de 0-3.")
            registrar()
        elif tipo == 0:
            home()
    except (ValueError,TypeError):
        print("Você digitou não digitou um inteiro de 0 a 3.")
        registrar()
# Nome 
    while True:
        temnumero = False
        try:
            nome = input("Digite seu nome: ")
            for carac in nome:
                if carac.isnumeric():
                    temnumero = True
            if temnumero == True:
                s_n = int(input("Seu nome possui alguns números. Certeza que  o digitou corretamente?  \n1- Sim 2- Não\nR:"))
                time.sleep(0.5)
                if s_n == 1:
                    print("Ok, salvando seu nome...")
                    time.sleep(0.5)
                elif s_n == 2:
                    print("Ok, digite novamente.")
                    time.sleep(0.5)
            elif len(nome) < 5:
                s_n = int(input("Seu nome é pequeno. Certeza que o digitou corretamente? \n1- Sim 2- Não \nR:"))
                time.sleep(0.5)
                if s_n == 1:
                    print("Ok, salvando seu nome...")
                    time.sleep(0.5)
                elif s_n == 2:
                    print("Ok, digite novamente.")
                    time.sleep(0.5)
                else:
                    raise ValueError
            else:
                break
        except:
            print("Digite 1 para Não e 2 para Sim.") 
            time.sleep(0.5)


# Idade
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            time.sleep(0.5)
            if idade <= 14 or idade >= 75:
                print("\nInsira um número válido (Maior que 14 e menor que 75)\n")

            else:
                break

        except:
            print("Insira um número!")

# CPF
    while True:
        try:
            cpf = input("Digite seu CPF: ")
            time.sleep(0.5)
            if validandoCpf(cpf) != True:
                raise ExcecaoCPFInvalido
            if verificacaoCPF(cpf):
                print("\nCPF já registrado. Tente novamente.\n")
                continue
            else:
                break
        except ExcecaoCPFInvalido:
            print("\nCPF Invalido\n")
# Email
    while True:
        email = input("Digite seu email: ")
        time.sleep(0.5)
        if verificacaoEMAIL(email):
            print("\nEmail já registrado. Tente novamente.\n")
            continue

        else:
            break

# Telefone
    while True:
        telefone = input("Digite seu telefone: ")
        time.sleep(0.5)
        if verificacaoTELEFONE(telefone):
            print("\nTelefone já registrado. Tente novamente.\n")
            continue

        else:
            break

# PCD
    while True:
        try:
            pcdAsk = int(input("\nVocê é uma Pessoa com Deficiência?\n1- Sim\n2- Não\nR: "))
            time.sleep(0.5)
            if pcdAsk == 1:
                qualpcd = input("\nQual sua deficiência?\nSiga o exemplo: 'Possuo deficiência <deficiência>'\nR: ")
                pcd = qualpcd.split("Possuo ")
                pcd = pcd[1]
                pcd = "Possui " + pcd
                dados_usuario["PCD"] = pcd
                break
            elif pcdAsk == 2:
                break

            else:
                print("Opção incorreta!")

        except:
            print("insira uma Opcção!")

# Usuário
#deixar digitar qualquer user ja q nao ta usando db, focar mais na senha
    while True: 
        try:
            usuario = input("\nDigite seu usuário: ")
            for user in usuarios:
                if user["usuario"] == usuario:
                    print("O usuário informado já existe. Tente novamente.")
                    time.sleep(0.5)
            if len(usuario) <= 5:
                raise ValueError
            else:
                break
        except ValueError:
            print("Seu usuário é muito pequeno.\nDigite-o novamente.")
            time.sleep(0.5)
        except:
            print("Tivemso algum problema, tente digitar seu usuário novamente.")
            time.sleep(0.5)
        finally:
            print("Lembre-se: mais importante que o usuário, somente a senha. \nCuide do seu usuário -_-")
            time.sleep(0.5)

        
    
    

# Senha
    while True:
        try:
            senha = input("Digite sua senha: ")
            time.sleep(0.5)
            if len(senha) >= 6:
                break        
            else:
                print("A senha deve conter no mínimo 6 caracteres. Tente novamente.")
                raise ValueError
        except ValueError:
            print("Digite um valor válido")
        finally:
            print("Lembre-se: uma boa senha não possui sequências fáceis e não é pequena. \nE não se esqueça de anotar sua senha.\n")

# Confirmando senha
    while True:
        senha1 = input("Confirme sua senha: ")
        time.sleep(0.5)
        if senha != senha1:
            print("As senhas não coincidem. Tente novamente.")
            time.sleep(0.5)

        else:
            print("As senhas coincidem... Continuando.")
            time.sleep(0.5)
            break

# Aluno
    if tipo == 1:
        while True:
            try:
                # Matricula
                matricula = int(input("Digite sua matrícula: "))
                time.sleep(0.5)
                if verificar_matricula(matricula):
                    print("Matrícula já registrada. Tente novamente.")
                    continue

                else:
                    break

            except:
                print("Insira um número!")

        curso = escolher_curso()
        novo_usuario = Aluno(nome, idade, cpf, email, telefone, matricula, curso)
        if pcdAsk == 1: novo_usuario.definindoPcd(pcd)
# Professor
    elif tipo == 2:
        curso = escolher_curso()  # definindo o curso
        novo_usuario = Prof(nome, idade, cpf, email, telefone, curso)
        if pcdAsk == 1: novo_usuario.definindoPcd(pcd)

# Adiministrador
    elif tipo == 3:
        novo_usuario = Adm(nome, idade, cpf, email, telefone)
        if pcdAsk == 1: novo_usuario.definindoPcd(pcd)

    else:
        print("Opção inválida. Tente novamente.")
        registrar()

    usuarios.append({"usuario": usuario, "senha": senha, "tipo": tipo, "objeto": novo_usuario})
    print("Registro realizado com sucesso.\n")
    time.sleep(0.5)
    print("Redirecionando para o login...\n")
    time.sleep(1)
    acesso()


# Acesso
def acesso():
    if len(usuarios) <= 0:
        time.sleep(1)
        print("Antes de fazer o login, é necessário fazer seu registro.")
        time.sleep(0.5)
        print("Indo para tela de resgitro...")
        registrar()
    time.sleep(0.5)
    print("(digite 0 se quiser retornar ao menu)")
    time.sleep(0.5)
    usuario = input("Digite seu usuário: ")
    time.sleep(0.5)
    rsp = "usuário encontrado."
    if usuario == "0":
        home()
    for user in usuarios:
        if user["usuario"] != usuario:
            rsp = "O usuário informado não existe. Tente novamente."   
    if rsp != "usuário encontrado.":
        print(rsp)
        acesso()
    senha = input("Digite sua senha: ")
    for user in usuarios:
        if user["usuario"] == usuario and user["senha"] == senha:
            dados_usuario = user
            break
        else:
            print("senha inválida ou usuário inválidos. Deseja digitar novamente?")
            dgtarNov = input("1-Sim 2- Não\nR:")
            if dgtarNov == "1":
                print("Ok.\nVoltando...")
                time.sleep(0.5)
                acesso()
            elif dgtarNov == "2":
                print("Ok, saindo então.")
                time.sleep(0.5)
                exit()
            else:
                print("Da próxima digite um dos valores solicitados! '-'")
                time.sleep(0.5)
                print("Saindo...")
                time.sleep(0.5)
                exit()

# Acesso Aluno 
    if dados_usuario["tipo"] == 1:
            nome_pessoa = dados_usuario["objeto"].getNome()
            print("Login realizado!\n")
            time.sleep(0.7)
            print(f"Olá, {nome_pessoa}\nBem-Vindo. ")
            time.sleep(0.5)
            while True:
                menu = int(input("1- Exibir dados do perfil\n2- Marcar atendimento\n3- Consultar Atendimentos \n4- Logout\n5- Sair\nR: "))
                time.sleep(0.5)
                if menu == 1:
                    print(f"\n{dados_usuario}\n")
                    time.sleep(0.5)
                elif menu == 2:
                    professor = input("Qual o nome do professor relacionado ao atendimento?\nR:")
                    marcarAtendimento(dados_usuario["objeto"],professor,True)
                elif menu == 3:
                    print()
                    time.sleep(0.5)
                    verMyAtendimentos(dados_usuario["objeto"])
                    print()
                    time.sleep(0.5)
                elif menu == 4:
                    print("deslogando...")
                    home()
                elif menu == 3:
                    print("saindo...")
                    exit()
# Acesso Professor
    elif dados_usuario["tipo"] == 2:
            nome_pessoa = dados_usuario["objeto"].getNome()
            print("Login realizado!\n")
            time.sleep(0.7)
            print(f"Olá, {nome_pessoa} ")
            time.sleep(0.5)
            while True:
                menu = input("1- Exibir dados do perfil\n2- Marcar atendimento\n3- Consultar atendimentos\n4- Logout\n5- Sair\nR: ")
                time.sleep(0.5)
                if menu == "1":
                    print(dados_usuario)
                elif menu == "2":
                    aluno = input("Qual o nome do aluno relacionado ao atendimento?")
                    marcarAtendimento(aluno,dados_usuario["objeto"],False)
                elif  menu == "3":
                    verMyAtendimentos(dados_usuario["objeto"])
                    
                elif menu == "4":
                    print("deslogando...")
                    home()
                elif menu == "5":
                    print("saindo...")
                    exit()

# Acesso Administrador
    elif dados_usuario["tipo"] == 3:
            nome_pessoa = dados_usuario["objeto"].getNome()
            print("Login realizado!\n")
            print(f"Olá, {nome_pessoa} ")
            time.sleep(0.5)
            while True:
                menu = int(input("1 - Exibir Dados do Perfil \n2- Logout\n3- Sair\nR: "))
                time.sleep(0.5)
                if menu == "1":
                    print(dados_usuario)
                    pass
                elif menu == "2":
                    print("deslogando...")
                    home()
                elif menu == "3":
                    print("saindo...")
                    exit()
    else:
        print("\nUsuário ou senha incorretos.")
        acesso()

print("Bem-vindo ao SAA - Sistema de Atendimento ao Aluno\nIFRO Campus Calama - Técnico Integrado")
home()