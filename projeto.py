#Autoria: Lucas Alves da Cruz Lira & David Robert de Lima Gomes & Joermeson Matheus
#Instituição: Uniesp - Centro Universitário
#Disciplina: Estrutura de dados - P3
#João Pessoa - Paraíba
#Curso: Sistemas de informação

#Tipos de estruturas utilizadas: Listas e dicionários

#Txt utilizados no programa:
#areasEspeciais,estacionamento,ocorrencia,eventos,relatorios e cadastros

import time

#Cores do terminal
white = '\033[1;30m'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
purple = '\033[1;35m'
lightblue = '\033[1;36m'
gray = '\033[1;37m'
stopcolor = '\033[m'

#cadastrosFuncionarios
dados = dict()

#logins
usuario = ["LUCAS"]
senha = [123]

#estacionamento
veiculos = dict()
eventos_estaciona = []

#permissões areas especiais
permissao = dict()
area_especial = dict()



def gestor():
    opcao = 1
    cont = 1
    opcao2 = 1
    areasEspeciais = open("areasEspeciais.txt","a")
    print(f"{lightblue}=-=" * 12)
    print(f"{green}  Gestão de Estacionamento Uniesp")
    print(f"{lightblue}=-=" * 12)
    nome = input(f"{green}Nome: {stopcolor}")
    print(f"{red}Para ter acesso, entre com seu login:{stopcolor}")
    email = input(f"{green}Usuário: ").strip().upper()
    password = int(input(f"Senha: {stopcolor}").strip())
    while email not in usuario or password not in senha:
        cont = cont+1
        print(f"{red}Usuário ou senha incorretos! Por favor tente novamente.{stopcolor}")
        email = input(f"{green}Usuário: ").strip().upper()
        password = int(input(f"Senha: {stopcolor}").strip())
        if cont >= 3:
            print(f"{lightblue}=-={stopcolor}" * 20)
            print("Você alcançou o número máximo de tentativas de login.")
            time.sleep(1)
            menuPrincipal()
    if email in usuario and password in senha:
        print(f"{lightblue}=-={stopcolor}" * 12)
        print(f"{white}Carregando...{stopcolor}")
        time.sleep(1)
        print(f"{white}.{stopcolor}")
        time.sleep(1)
        print(f"{white}.{stopcolor}")
        time.sleep(1)
        print(f"{white}.{stopcolor}")
        time.sleep(0.5)
        print(f"{lightblue}=-={stopcolor}" * 12)
        print(f"{green}         Bem vindo, {nome.capitalize()}!{stopcolor}")
        print(f"{lightblue}=-={stopcolor}" * 12)
        print(f"{red}Opções para a Gestão do estacionamento: {stopcolor}")
        while (opcao!=5):
            print("\n[1º] - Monitorar Estacionamento")
            print("[2º] - Visualizar relatórios")
            print("[3º] - Criar áreas especiais do sistema")
            print("[4º] - Cadastrar eventos no estacionamento")
            print("[5º] - Sair do sistema")
            opcao = int(input("\nInforme uma opção: "))
            if opcao == 1:
                while opcao != 3:
                    print("-=-=-=-=-= Monitorar estacionamento -=-=-=-=-=-=")
                    print("[1º] - Exibir todos veículos no estacionamento")
                    print("[2º] - Localizar veículo no estacionamento")
                    print("[3º] - Sair")
                    opcao = int(input("\nO que deseja: "))
                    if opcao == 1:
                        print(veiculos)
                    elif opcao == 2:
                        nome = input("Nome do Proprietário: ")
                        for buscar in veiculos.keys():
                            if (buscar == nome.lower()):
                                print(veiculos[buscar])
            elif opcao == 2:
                print("-="*12)
                print("Visualização de relatórios")
                print("-="*12)
                print("\nPara visualizar o relatório do dia pesquise por (Relatorio) no seu computador")
            elif opcao == 3:
                print("-="*12)
                print("Áreas especiais no estacionamento")
                print("-="*12)
                while (opcao2!=5):
                    print("[1º] - Visualizar permissões concedidas pelo RH")
                    print("[2º] - Cadastrar em áreas especiais")
                    print("[3º] - Remover veículo")
                    print("[4º] - Localizar veículo")
                    print("[5º] - Voltar ao menu")
                    opcao2 = int(input("Informe uma opção: "))
                    if opcao2 ==1:
                        print("\nPermissões concedidas: ")
                        print(permissao)
                    elif opcao2 ==2:
                        nome = input("\nNome: ")
                        areasEspeciais.write("Nome: "+nome+"\n")
                        funcao = input("Função na instituição: ")
                        areasEspeciais.write("Função na instituição: "+funcao+"\n")
                        cpf_cnpj = input("CPF/CNPJ: ")
                        areasEspeciais.write("CPF/CNPJ: "+cpf_cnpj+"\n")
                        telefone = input("Telefone: ")
                        areasEspeciais.write("Telefone: "+telefone+"\n")
                        carro_modelo = input("Modelo do carro: ")
                        areasEspeciais.write("Modelo do carro: "+carro_modelo+"\n")
                        placa = input("Placa do carro: ")
                        areasEspeciais.write("Placa do carro: "+placa+"\n")
                        cor = input("Cor do carro: ")
                        areasEspeciais.write("Cor do carro: "+cor+"\n")
                        ano = input("Ano do carro: ")
                        areasEspeciais.write("Ano do carro: "+ano+"\n")
                        areasEspeciais.write("----------------------------" + "\n")
                        area_especial[nome.lower()] = [nome.lower(), funcao, cpf_cnpj, telefone, carro_modelo, placa, cor,
                                                   ano]
                        print("\nCadastrado com sucesso!")
                    elif opcao2 ==3:
                        print("-=-=-=-=-=-=- Remoção de veículos -=-=-=-=-=-=-=-")
                        for excluir in area_especial.keys():
                            print(excluir)
                        delete = input("\nInforme nome do proprietário: ")
                        area_especial.pop(delete.lower())
                        print("\nVeículo Removido com sucesso!!!")
                    elif opcao2 == 4:
                        opcao = 1
                        while opcao != 3:
                            print("-=-=-=-=-= Monitorar Estacionamento de áreas especiais -=-=-=-=-=-=")
                            print("[1º] - Exibir todos veículos no estacionamento")
                            print("[2º] - Localizar veículo no estacionamento")
                            print("[3º] - Sair")
                            opcao = int(input("\nO que deseja: "))
                            if opcao == 1:
                                print(area_especial)
                            elif opcao == 2:
                                nome = input("Nome do Proprietário: ")
                                for buscar in area_especial.keys():
                                    if (buscar == nome.lower()):
                                        print(area_especial[buscar])




            elif opcao == 4:
                print("-=" * 12)
                print("Pré cadastro de eventos")
                print("-=" * 12)
                eventos_estaciona.append(input("Nome do evento: "))
                print("Evento pré cadastrado com sucesso!")




def funcionarioEstacio():
    estacionamento = open("Estacionamento.txt","a")
    ocorrencia = open("Ocorrencia.txt","a")
    relatorios = open("relatorios.txt", "a")
    eventos = open("eventos.txt","a")
    cont = 1
    op = 1
    op2 = 1
    print(f"{lightblue}=-=" * 12)
    print(f"{green}  Estacionamento Uniesp")
    print(f"{lightblue}=-=" * 12)
    nome = input(f"{green}Nome: {stopcolor}")
    print(f"{red}Para ter acesso, entre com seu login:{stopcolor}")
    email = input(f"{green}Usuário: ").strip().upper()
    password = int(input(f"Senha: {stopcolor}").strip())
    while email not in usuario or password not in senha:
        cont = cont + 1
        print(f"{red}Usuário ou senha incorretos! Por favor tente novamente.{stopcolor}")
        email = input(f"{green}Usuário: ").strip().upper()
        password = int(input(f"Senha: {stopcolor}").strip())
        if cont >= 3:
            print(f"{lightblue}=-={stopcolor}" * 20)
            print("Você alcançou o número máximo de tentativas de login.")
            time.sleep(1)
            menuPrincipal()
    if email in usuario and password in senha:
        print(f"{lightblue}=-={stopcolor}" * 12)
        print(f"{white}Carregando...{stopcolor}")
        time.sleep(1)
        print(f"{white}.{stopcolor}")
        time.sleep(1)
        print(f"{white}.{stopcolor}")
        time.sleep(1)
        print(f"{white}.{stopcolor}")
        time.sleep(0.5)
        print(f"{lightblue}=-={stopcolor}" * 12)
        print(f"{green}         Bem vindo, {nome.capitalize()}!{stopcolor}")
        print(f"{lightblue}=-={stopcolor}" * 12)
        print(f"{red}Opções para o Estacionamento Uniesp: {stopcolor}")
        while op !=7:
            print("\n[1º] - Cadastrar novos veículos")
            print("[2º] - Remover veículos")
            print("[3º] - Monitorar Estacionamento")
            print("[4º] - Cadastrar ocorrências no estacionamento")
            print("[5º] - Cadastrar Eventos no estacionamento")
            print("[6º] - Gerar um relatório do dia")
            print("[7º] - Sair do sistema")
            op = int(input("\nDigite uma opção: "))
            if op == 1:
                print("-=-=-=-=-=-=-=-= Cadastro de veículos-=-=-=-=-=-=-=-=-=")
                op1 = int(input("Informe a quantidade de veículos que deseja cadastrar: "))
                for i in range(0,op1):
                    proprietario = input("Proprietário: ").upper().strip()
                    estacionamento.write("Proprietário: "+proprietario+"\n")
                    cor = input("Cor do veículo: ").upper().strip()
                    estacionamento.write("Cor: "+cor+"\n")
                    placa = input("Placa do Veículo: ").upper().strip()
                    estacionamento.write("Placa: "+placa+"\n")
                    ano = input("Ano do Veículo: ").upper().strip()
                    estacionamento.write("Ano: "+ano+"\n")
                    marca = input("Marca do Carro: ").upper().strip()
                    estacionamento.write("Marca: "+marca+"\n")
                    funcao = input("Aluno/Professor/Coordenador: ").upper().strip()
                    estacionamento.write("Função: "+funcao+"\n")
                    matricula = input("Matricula: ").upper().strip()
                    estacionamento.write("Matricula: "+matricula+"\n")
                    estacionamento.write("----------------------------" + "\n")
                    print("\nVeículo Cadastrado com Sucesso!!")
                    veiculos[proprietario.lower()] = [proprietario.lower(),cor,placa,ano,marca,funcao,matricula]

            elif op == 2:
                print("-=-=-=-=-=-=- Remoção de veículos -=-=-=-=-=-=-=-")
                for excluir in veiculos.keys():
                    print(excluir)
                delete = input("\nInforme nome do proprietário: ")
                veiculos.pop(delete.lower())
                print("\nVeículo Removido com sucesso!!!")

            elif op == 3:
                opcao = 1
                while opcao != 3:
                    print("-=-=-=-=-= Monitorar Estacionamento -=-=-=-=-=-=")
                    print("[1º] - Exibir todos veículos no estacionamento")
                    print("[2º] - Localizar veículo no estacionamento")
                    print("[3º] - Sair")
                    opcao = int(input("\nO que deseja: "))
                    if opcao == 1:
                        print(veiculos)
                    elif opcao == 2:
                        nome = input("Nome do Proprietário: ")
                        for buscar in veiculos.keys():
                            if (buscar == nome.lower()):
                                print(veiculos[buscar])

            elif op == 4:
                print("-="*12)
                print("Ocorrências no Estacionamento")
                print("-=" * 12)
                print("Informe a gravidade da ocorrência: Leve/Mediana/Grave")
                ocorr = input("Informe a ocorrência resumidamente: ").upper().strip()
                ocorrencia.write("Ocorrência: "+ocorr+"\n")
                ocorrencia.write("-----------------------------"+"\n")
            elif op == 5:
                print("-=" * 12)
                print("Cadastro de Eventos")
                print("-=" * 12)
                while (op2!=3):
                    print("[1º] - Exibir Eventos pré cadastrados")
                    print("[2º] - Cadastrar Evento")
                    print("[3º] - Voltar ao menu")
                    op2 = int(input("Opção: "))
                    if op2 == 1:
                        print("\nEventos: ")
                        print(eventos_estaciona)
                    elif op2 ==2:
                        print("-=" * 12)
                        print("Cadastro de eventos")
                        print("-=" * 12)
                        nome_evento = input("Nome do evento: ")
                        eventos.write("Nome do evento: "+nome_evento+"\n")
                        data_evento = input("Data do evento: ")
                        eventos.write("Data do evento: "+data_evento+"\n")
                        local_evento = input("Local do evento: ")
                        eventos.write("Local do evento: "+local_evento+"\n")
                        hora = input("Hora do evento: ")
                        eventos.write("Hora do evento: "+hora+"\n")
                        dias_semana = input("Dias na semana: ")
                        eventos.write("Dias na semana: "+dias_semana+"\n")
                        reserva_local = input("Reservar local: ")
                        eventos.write("Reservar local: "+reserva_local+"\n")
                        hora_termino = input("Hora do termino: ")
                        eventos.write("Hora do termino: "+hora_termino+"\n")
                        responsavel = input("Responsável pela realização: ")
                        eventos.write("Responsável pela realização: "+responsavel+"\n")
                        cpf_cnpj = input("CPF/CNPJ do responsável: ")
                        eventos.write("CPF/CNPJ do responsável: "+cpf_cnpj+"\n")
                        eventos.write("------------------------------------------------" + "\n")
                        print("\nEvento cadastrado com sucesso!")

            elif op == 6:
                print("-=" * 12)
                print("Relatório do dia no estacionamento")
                print("-=" * 12)
                data = input("\nData: ")
                relatorios.write("Data: "+data+"\n")
                nome_Funcionario = input("Nome do funcionário: ")
                relatorios.write("Nome do funcionário: "+nome_Funcionario+"\n")
                matricula_funcionario = input("Mátricula: ")
                relatorios.write("Mátricula do funcionário: "+matricula_funcionario+"\n")
                numero_ocorrencia = input("Número de ocorrências: ")
                relatorios.write("Número de ocorrências: "+numero_ocorrencia+"\n")
                placa_veiculos = input("Placa dos veículos na ocorrência: ")
                relatorios.write("Placa dos veículos na ocorrência: "+placa_veiculos+"\n")
                nomes_dos_envolvidos = input("Nomes dos envolvidos na ocorrência: ")
                relatorios.write("Nomes dos envolvidos na ocorrência: "+nomes_dos_envolvidos+"\n")
                carros_cadastrados = input("Número de carros cadastrados no dia: ")
                relatorios.write("Número de carros cadastrados no dia: "+carros_cadastrados+"\n")
                eventos_cadastrados = input("Eventos cadastrados: ")
                relatorios.write("Eventos cadastrados: "+eventos_cadastrados+"\n")
                erro_cadastro = input("Erro no cadastro de veículo: ")
                relatorios.write("Erro no cadastro de veículo: "+erro_cadastro+"\n")
                pedidos_gestor = input("Pedidos ao gestor: ")
                relatorios.write("Pedidos ao gestor: "+pedidos_gestor+"\n")
                veiculos_removidos = input("Número de veículos removidos: ")
                relatorios.write("Número de veículos removidos: "+veiculos_removidos+"\n")
                problemas_sistema = input("Problemas com o sistema (Resumidamente): ")
                relatorios.write("Problemas com o sistema (Resumidamente): "+problemas_sistema+"\n")
                observacao = input("Observação para o gestor: ")
                relatorios.write("Observação para o gestor: "+observacao+"\n")
                print("\nRelatório gerado com sucesso!")
                relatorios.write("------------------------------------------------" + "\n")

def rhUniesp():
    cadastros = open("Cadastros.txt", "a")
    cont = 1
    opcao = 0
    op1 = 1
    arquivo = open("arquivo.txt", "w")
    print(f"{lightblue}=-=" * 12)
    print(f"{green}  Setor de Recursos Humanos Uniesp")
    print(f"{lightblue}=-=" * 12)
    nome = input(f"{green}Nome: {stopcolor}")
    print(f"{red}Para ter acesso, entre com seu login:{stopcolor}")
    email = input(f"{green}Usuário: ").strip().upper()
    password = int(input(f"Senha: {stopcolor}").strip())

    #Repetir o laço até que o usuario e senha estejam corretos
    while email not in usuario or password not in senha:
        cont = cont+1
        print(f"{red}Usuário ou senha incorretos! Por favor tente novamente.{stopcolor}")
        email = input(f"{green}Usuário: ").strip().upper()
        password = int(input(f"Senha: {stopcolor}").strip())

        #Contador de tentativas de login no sistema
        if cont>=3:
            print(f"{lightblue}=-={stopcolor}" * 20)
            print("Você alcançou o número máximo de tentativas de login.")
            time.sleep(1)
            menuPrincipal()
    if email in usuario and password in senha:
        print(f"{lightblue}=-={stopcolor}" * 12)
        print(f"{white}Carregando...{stopcolor}")
        time.sleep(1)
        print(f"{white}.{stopcolor}")
        time.sleep(1)
        print(f"{white}.{stopcolor}")
        time.sleep(1)
        print(f"{white}.{stopcolor}")
        time.sleep(0.5)
        print(f"{lightblue}=-={stopcolor}" * 12)
        print(f"{green}         Bem vindo, {nome.capitalize()}!{stopcolor}")
        print(f"{lightblue}=-={stopcolor}" * 12)
        print(f"{red}Opções para o RH:{stopcolor}")

        while opcao!=4:
            print(f"{green}          [1º] - Cadastrar novos funcionários")
            print("          [2º] - Remover login de funcionário")
            print("          [3º] - Conceder permissão para áreas especiais do estacionamento")
            print(f"          [4º] - Sair do Sistema{stopcolor}")

            opcao = int(input(f"{white}Informe uma opção acima: {stopcolor}"))
            if opcao == 1:
                print(f"{lightblue}=-={stopcolor}" * 12)
                print(f"{green}      Cadastro de funcionários")
                print(f"{lightblue}=-={stopcolor}" * 12)
                print(f"{red}Opções: {stopcolor}")
                while op1!=4:
                    print(f"{green}          [1º] - Cadastrar funcionário do RH")
                    print(f"          [2º] - Cadastrar Gestor")
                    print(f"          [3º] - Cadastrar funcionário do estacionamento")
                    print(f"          [4º] - Retornar ao Menu{stopcolor}")
                    op1 = int(input(f"{white}Informe uma opção: {stopcolor}"))
                    if op1 == 1:
                        print("-=-=-=-=-=-=-= Cadastramento RH -=-=-=-=-=-=-=-=-")

                        nome = input("Nome Completo: ").upper().strip()
                        cadastros.write("Nome: "+nome+"\n")
                        nascimento = input("Data de Nascimento: ").upper().strip()
                        cadastros.write("Nascimento: "+nascimento+"\n")
                        cpf = input("CPF: ").upper().strip()
                        cadastros.write("CPF: "+cpf+"\n")
                        telefone = input("Telefone: ").upper().strip()
                        cadastros.write("Telefone: "+telefone+"\n")
                        endereco = input("Endereço: ").upper().strip()
                        cadastros.write("Endereço: "+endereco+"\n")
                        funcao = input("Função: ").upper().strip()
                        cadastros.write("Função: "+funcao+"\n")
                        cadastros.write("----------------------------" + "\n")
                        print(f"\n{red}Dica: Usuário deve conter nome do funcionário e nome da instituição")
                        print(f"Dica: Senha com apenas números{stopcolor}")

                        usuario.append(input("\nUsuário para login: ").upper().strip())
                        senha.append(int(input("Senha para login: ").strip()))

                        print(f"\n{red}Usuário cadastrado com sucesso!{stopcolor}")

                        dados[nome.lower()] = [nome.lower(), nascimento, cpf,telefone,endereco,funcao]

                    if op1 == 2:
                        print("-=-=-=-=-=-=-= Cadastramento de Gestor -=-=-=-=-=-=-=-=-")
                        nome1 = input("Nome Completo: ").upper().strip()
                        cadastros.write("Nome: "+nome1 + "\n")
                        nascimento = input("Data de Nascimento: ").upper().strip()
                        cadastros.write("Nascimento: "+nascimento + "\n")
                        cpf = input("CPF: ").upper().strip()
                        cadastros.write("CPF: "+cpf + "\n")
                        telefone = input("Telefone: ").upper().strip()
                        cadastros.write("Telefone: "+telefone + "\n")
                        endereco = input("Endereço: ").upper().strip()
                        cadastros.write("Endereço: "+endereco + "\n")
                        funcao = input("Função: ").upper().strip()
                        cadastros.write("Função: "+funcao + "\n")
                        cadastros.write("----------------------------" + "\n")
                        print(f"\n{red}Dica: Usuário deve conter nome do funcionário e nome da instituição")
                        print(f"Dica: Senha com apenas números{stopcolor}")

                        usuario.append(input("\nUsuário para login: ").upper().strip())
                        senha.append(int(input("Senha para login: ").strip()))

                        print(f"\n{red}Usuário cadastrado com sucesso!{stopcolor}")

                        dados[nome1.lower()] = [nome1.lower(), nascimento, cpf, telefone, endereco, funcao]

                    if op1 == 3:
                        print("-=-=-=-=-=-=-= Cadastro dos funcionários do estacionamento -=-=-=-=-=-=-=-=-")
                        nome2 = input("Nome Completo: ").upper().strip()
                        cadastros.write("Nome: "+nome2 + "\n")
                        nascimento = input("Data de Nascimento: ").upper().strip()
                        cadastros.write("Nascimento: "+nascimento + "\n")
                        cpf = input("CPF: ").upper().strip()
                        cadastros.write("CPF: "+cpf + "\n")
                        telefone = input("Telefone: ").upper().strip()
                        cadastros.write("Telefone: "+telefone + "\n")
                        endereco = input("Endereço: ").upper().strip()
                        cadastros.write("Endereço: "+endereco + "\n")
                        funcao = input("Função: ").upper().strip()
                        cadastros.write("Função: "+funcao + "\n")
                        cadastros.write("----------------------------" + "\n")
                        print(f"\n{red}Dica: Usuário deve conter nome do funcionário e nome da instituição")
                        print(f"Dica: Senha com apenas números{stopcolor}")

                        usuario.append(input("\nUsuário para login: ").upper().strip())
                        senha.append(int(input("Senha para login: ").strip()))

                        print(f"\n{red}Usuário cadastrado com sucesso!{stopcolor}")

                        dados[nome2.lower()] = [nome2.lower(), nascimento, cpf, telefone, endereco, funcao]

            elif opcao == 2:
                print("-=-=-=-=-=-=-=-= REMOÇÃO DE LOGIN DE DE FUNCIONÁRIO -=-=-=-=-=-=-=-=")
                print(f"{red}Dica: Para remover o login, informe o usuario do funcionário{stopcolor}")
                op2 = input("Login do funcionário: ").upper().strip()
                if op2 in usuario:
                    usuario.remove(op2)
            elif opcao == 3:
                print("-="*12)
                print("Permissões")
                print("-=" * 12)
                nome = input("\nNome: ")
                funcao = input("Função na instituição: ")
                cpf_cnpj = input("CPF/CNPJ: ")
                telefone = input("Telefone: ")
                carro_modelo = input("Modelo do carro: ")
                placa = input("Placa do carro: ")
                cor = input("Cor do carro: ")
                ano = input("Ano do carro: ")
                permissao[nome.lower()] = [nome.lower(), funcao, cpf_cnpj, telefone, carro_modelo, placa,cor,ano]
                print("\nPermissão concedida com sucesso!")
                print("Em até 24h será liberada a área especial")


def menuPrincipal():
    print(f"{lightblue}=-="*20)
    print(f"{red}     Sistema de Estacionamento - Uniesp    ")
    print(f"{lightblue}=-=" * 20)
    print(f"{white}             Morais Parking!   ")
    print(f"{white}=-="*20)
    opcao = 0

    while opcao!=4:
        print(f"{red}Opções do Sistema: ")
        print(f"{red}        [1º] - RH Uniesp")
        print(f"{red}        [2º] - Funcionário do Estacionamento Uniesp")
        print(f"{red}        [3º] - Gestor do Estacionamento")
        print(f"{red}        [4º] - Sair do Sistema")
        opcao = int(input(f"{white}Informe uma opção acima: "))
        if opcao == 1:
            rhUniesp()
        elif opcao == 2:
            funcionarioEstacio()
        elif opcao == 3:
            gestor()
        elif opcao == 4:
            print(f"{red}\nFinalizando sistema...")
            time.sleep(1.5)
            print(f"{green}Sistemas Uniesp - Centro universitário")
            print("Sistema Encerrado!")

menuPrincipal()



