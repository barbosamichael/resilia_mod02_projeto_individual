#!/usr/bin/env python
# coding: utf-8

# ### Criar lista que armazena valores do desempenho dos candidatos

# eX= entrevista
# 	tX = teorico
# 	pX= pratico
# 	sX = soft

# In[1]:


amostra = [["candidato01",0,0,0,0],["canditado02",1,2,3,4],["candidato03",3,5,4,6]]


# In[2]:


print(range(len(amostra)))


# In[3]:


amostra[2][1]


# In[4]:


def busca_candidatos(amostra,x,t,p,s):
    
    temporaria = []
    # tamanho da matriz amostra pode ser mutável
    for i in range(len(amostra)):
        # o j sempre é fixo pq temos 5 colunas sempre; nome,x,t,p e s.
        for j in range(1,5): # começar em 1 até 4
            # começa a varrer a matriz 
            print("matrizes",amostra[i][j]) # print teste
            if x>= amostra[i][j]:
                print("valores_x",amostra[i][j]) # print teste
                continue
            else:
                break
                if t>= amostra[i][j]:
                    print("valores_t",amostra[i][j]) # print teste
                    continue
                else:
                    break
                    if p>= amostra[i][j]:
                        print("valores_p",amostra[i][j]) # print teste
                        continue
                    else:
                        break
                        print("valores_s",amostra[i][j]) # print teste
                        if s>= amostra[i][j]:
                            # chegando até aqui adiciona a posição correspondente da lista
                            # na lista temporaria 
                            temporaria.append(amostra[i])
                            print(amostra[i])
                            # resultado da busca eh um subconjunto dos dados da matriz amostra
                            return temporaria
                        else:
                            break
            #else:
            #   print("Para os valores digitados não temos correspondência.")
    


# In[5]:


amostra = [["candidato01",0,0,0,0],["canditado02",1,2,3,4],["candidato03",3,5,4,6]]


# In[11]:


temp02=[[1,2,3],[9,8,5]]


# In[19]:


def busca_candidatos2(amostra,x,t,p,s):
    
    temp = []
    # tamanho da matriz amostra pode ser mutável
    for i in range(len(amostra)):       
        count=0
        print(count)
        if x <= amostra[i][1]:
            print("teste1",amostra[i][1])  # print teste
            
            if t <= amostra[i][2]:               
                print("teste2",amostra[i][2])   # print teste
                
                if p <= amostra[i][3]:
                    print("teste3",amostra[i][3])  # print teste
                    
                    if s <= amostra[i][4]:
                        
                        temp.append(amostra[i][:])
                        print("teste4",amostra[i][4])  # print teste
                        count= count+1
    print(temp)
    return temp


# In[20]:


busca_candidatos2(amostra,1,2,3,4)


# In[ ]:





# In[13]:



def formatacao(candidato,x,t,p,s):
    print("{0}: e{1}_t{2}_p{3}_s{4}".format(candidato,x,t,p,s))


# In[14]:


formatacao(amostra[0][0],1,2,3,4)


# In[ ]:





# In[ ]:





# In[ ]:




