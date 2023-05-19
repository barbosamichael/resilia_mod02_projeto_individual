#!/usr/bin/env python
# coding: utf-8

# ### Criar lista que armazena valores do desempenho dos candidatos
# 

# eX= entrevista
# 	tX = teorico
# 	pX= pratico
# 	sX = soft

# In[ ]:


amostra = [["candidato01",0,0,0,0],["canditado02",1,2,3,4],["candidato03",3,5,4,6],
           ["pedro",2,3,4,5],["maria",1,3,5,7],["antonio",3,5,7,8],["joaquim",6,7,8,9],
           ["francisca",7,8,8,9],["aristarco",9,8,7,6],["flavia",9,8,8,7],
           ["ferdinando",3,4,7,7],["andreia",7,6,8,9],["antonieta",10,10,10,10]]


# In[ ]:


def formatacao(candidato,e,t,p,s):
    print("{0}: e{1}_t{2}_p{3}_s{4}".format(candidato,e,t,p,s))


# In[ ]:


def busca_candidatos2(amostra,e,t,p,s):
    temp = []
    # tamanho da matriz amostra pode ser mutável
    for i in range(len(amostra)):       
        count=0
        #print(count)
        if e <= amostra[i][1]:
            #print("teste1",amostra[i][1])  # print teste            
            if t <= amostra[i][2]:               
                #print("teste2",amostra[i][2])   # print teste                
                if p <= amostra[i][3]:
                    #print("teste3",amostra[i][3])  # print teste                    
                    if s <= amostra[i][4]:
                        temp.append(amostra[i][:])
                        #print("teste4",amostra[i][4])  # print teste
                        count= count+1
                        formatacao(amostra[i][0],amostra[i][1],amostra[i][2],amostra[i][3],amostra[i][4])
    #print(temp)    
    return temp


# In[ ]:


def prints_tela_inicial():
    print("\nBem vindo ao sistema RH Consulta")
    print("\nSelecione uma opção:")
    print("\n1 - Cadastrar usuário")
    print("2 - Consultar notas")
    print("3 - Encerrar atendimento")
    entrada_inicial=int(input("Selecione uma opção: "))
    return entrada_inicial


# In[ ]:


def main():    
    # armazena a escolha uma variável
    entrada_inicial = prints_tela_inicial()
    user_option=0
    
    if entrada_inicial == 3:
        print("Obrigado e volte sempre!")
        return 

    while entrada_inicial == 1 and user_option != 3:
        if entrada_inicial == 1:
            print("Digite  as informações pediddas abaixo")
            nome=str(input("Nome: "))
            e=int(input("Entrevista: "))
            t=int(input("Teórico: "))
            p=int(input("Prático: "))
            s=int(input("Soft Skills: "))
            # adicionar novo usuário a variável amostra
            amostra.append([nome,e,t,p,s])
            print("\nCadastrado(a) com sucesso!!!")
        print("\n3 - Encerrar")
        print("5 - Para retornar ao menu inicial")
        user_option = int(input("Digite uma opção: "))
        if user_option == 5:
        # volta para o inicio chamando main()
        # funciona bem hehehe
            entrada_inicial=0
            user_option=3
            main()                
    #consultar notas            
    if entrada_inicial == 2:
        print("\nDigite o valor de corte das notas ;)")
        e=int(input("Entrevista: "))
        t=int(input("Teórico: "))
        p=int(input("Prático: "))
        s=int(input("Soft Skills: "))
        print("*"*10,"Resultados obtidos","*"*10)
        busca_candidatos2(amostra,e,t,p,s)
        main()
        


# In[ ]:


main()


# In[ ]:





# In[ ]:




