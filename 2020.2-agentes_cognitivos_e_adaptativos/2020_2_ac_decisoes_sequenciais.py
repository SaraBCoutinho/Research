# -*- coding: utf-8 -*-
"""2020.2-AC_Decisoes_sequenciais.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oaibViROqNIHtS8mp6Tymvdd2aH3KeZL

# Exercicio - Decisoes Sequenciais

Exercicio feito com base no exemplo demonstrado durante a aula de Agentes Cognitivos e Adaptativos sobre decisoes sequenciais.
"""

# Commented out IPython magic to ensure Python compatibility.
# Preparando o ambiente para usar R no colab
# %load_ext rpy2.ipython

# Commented out IPython magic to ensure Python compatibility.
# %%R
# # definição das matrizes de transição T(s,a,s')
# T_up = matrix(0,12,12)

# Commented out IPython magic to ensure Python compatibility.
# # Probabilidades da ação UP ao ser aplicada de um estado para outro 
# %%R
# T_up[1,4] = 0.1
# T_up[1,1] = 0.1
# T_up[1,2] = 0.8
# T_up[2,2] = 0.1
# T_up[2,3] = 0.8
# T_up[2,5] = 0.1
# T_up[3,6] = 0.1
# T_up[3,3] = 0.9
# T_up[4,7] = 0.1
# T_up[4,5] = 0.8
# T_up[4,1] = 0.1 
# T_up[6,9] = 0.1
# T_up[6,3] = 0.1 
# T_up[6,6] = 0.8
# T_up[7,10] = 0.1
# T_up[7,7] = 0.1 
# T_up[7,8] = 0.8 
# T_up[8,11] = 0.1
# T_up[8,5] = 0.1 
# T_up[8,8] = 0.8 
# T_up[9,12] = 0.1
# T_up[9,6] = 0.1
# T_up[9,9] = 0.8
#

# Commented out IPython magic to ensure Python compatibility.
# # Probabilidades da ação DOWN ao ser aplicada de um estado para outro 
# %%R
# T_down = matrix(0,12,12) 
# T_down[1,1] = 0.9 
# T_down[1,4] = 0.1 
# T_down[2,1] = 0.8 
# T_down[2,2] = 0.1
# T_down[2,5] = 0.1
# T_down[3,2] = 0.8 
# T_down[3,3] = 0.1 
# T_down[3,6] = 0.1 
# T_down[4,1] = 0.1 
# T_down[4,7] = 0.1 
# T_down[4,4] = 0.8 
# T_down[6,5] = 0.8 
# T_down[6,3] = 0.1
# T_down[6,9] = 0.1
# T_down[7,7] = 0.8
# T_down[7,4] = 0.1
# T_down[7,10] = 0.1
# T_down[8,7] = 0.8
# T_down[8,5] = 0.1
# T_down[8,11] = 0.1
# T_down[9,8] = 0.8
# T_down[9,6] = 0.1
# T_down[9,12] = 0.1
#

# Commented out IPython magic to ensure Python compatibility.
# # Probabilidades da ação LEFT ao ser aplicada de um estado para outro 
# %%R
# T_left = matrix(0,12,12) 
# T_left[1,1] = 0.9
# T_left[1,2] = 0.1
# T_left[2,1] = 0.1
# T_left[2,3] = 0.1
# T_left[2,2] = 0.8
# T_left[3,3] = 0.9
# T_left[3,2] = 0.1
# T_left[4,1] = 0.8
# T_left[4,4] = 0.1
# T_left[4,5] = 0.1
# T_left[6,3] = 0.8
# T_left[6,5] = 0.1
# T_left[6,6] = 0.1
# T_left[7,4] = 0.8
# T_left[7,7] = 0.1
# T_left[7,8] = 0.1
# T_left[8,5] = 0.8
# T_left[8,9] = 0.1
# T_left[8,7] = 0.1
# T_left[9,6] = 0.8
# T_left[9,9] = 0.1
# T_left[9,8] = 0.1

# Commented out IPython magic to ensure Python compatibility.
# # Probabilidades da ação RIGHT ao ser aplicada de um estado para outro 
# %%R
# T_right = matrix(0,12,12) 
# T_right[1,4] = 0.8
# T_right[1,1] = 0.1
# T_right[1,2] = 0.1
# T_right[2,5] = 0.8
# T_right[2,1] = 0.1
# T_right[2,3] = 0.1
# T_right[3,6] = 0.8
# T_right[3,3] = 0.1
# T_right[3,2] = 0.1
# T_right[4,7] = 0.8
# T_right[4,5] = 0.1
# T_right[4,4] = 0.1
# T_right[6,9] = 0.8
# T_right[6,6] = 0.1
# T_right[6,5] = 0.1
# T_right[7,7] = 0.1
# T_right[7,10] = 0.8
# T_right[7,8] = 0.1
# T_right[8,11] = 0.8
# T_right[8,7] = 0.1
# T_right[8,9] = 0.1
# T_right[9,12] =0.8
# T_right[9,9] = 0.1
# T_right[9,8] = 0.1

# Commented out IPython magic to ensure Python compatibility.
# %%R
# # Função construida a fim de atualizar a cada iteraçao os valores da função de utilidade dos estados 
# update_value <- function(T_up,T_down,T_right,T_left,rw,value){
# # Para o INPUT:
#   # T_up,T_down,T_right,T_left: sao as matrizes de transição de estados para cada ação
#   # rw: vetor de recompensas para cada estado. 
#   # value: vetor de utilidades dos estados atual (12 posições) 
# # Para o OUTPUT: 
#   # value_aux: vetor de utilidade atualizada a partir das equaçoes de Bellman  
#   value_aux = matrix(0,1,12)
#   # para cada um dos estados aplicaçao da equação de Bellman 
#   for (s in 1:12){
#     # calculo da utilidade associação a cada ação considerado o estado s
#     v_up = T_up[s,] %*% t(value)   
#     v_down = T_down[s,] %*% t(value)
#     v_left = T_left[s,] %*% t(value)
#     v_right = T_right[s,] %*% t(value)
#     # equação de Bellman aplicada ao estado s
#     value_aux[1,s] = rw[1,s] + max(c(v_up,v_down,v_left,v_right)) 
#   }
#   value = value_aux
#   
#   # aqui eh uma funcao para imprimir as utilidades de uma grade
#   aux = matrix(0,3,4)
#   aux[1,] = c(value[3],value[6],value[9],value[12])
#   aux[2,] = c(value[2],value[5],value[8],value[11])
#   aux[3,] = c(value[1],value[4],value[7],value[10])
#   print(aux)
#   return(value_aux)
# }
# 
# # função para calcular a política a partir das utilidades 
# return_policy <- function(T_up,T_down,T_right,T_left,value){
#   policy = cbind()
#   # obs.: somente 8 estados porque não ha ação aplicada nos dois estados terminais
#   for (s in c(1:4,6:9)){
#     # calculando a utildade de cada ação ao estado s  
#     v_up = T_up[s,] %*% t(value)   
#     v_down = T_down[s,] %*% t(value)
#     v_left = T_left[s,] %*% t(value)
#     v_right = T_right[s,] %*% t(value)
#     # escolhendo para o estado s a ação com maxima utilidade esperada
#     policy = cbind(policy,which.max(c(v_up,v_down,v_left,v_right)))}
#   
#   # função para imprimir a política em uma grade
#   actions = c("UP","DW","LF","RG")
#   s1 = paste(actions[policy[3]],actions[policy[5]],actions[policy[8]],"+1")
#   s2 = paste(actions[policy[2]],"-0.5",actions[policy[7]],"-1")
#   s3 = paste(actions[policy[1]],actions[policy[4]],actions[policy[6]],"+0.2")
#   cat("\n",s1,"\n",s2,"\n",s3)
#   return(policy)
# }    
# # EXECUÇÃO - INICIALIzAÇÃO DAS RECOMPENSAS
# rw = matrix(-0.4,1,12)
# rw[1,5] =-0.5
# rw[1,10] = 0.2
# rw[1,11] = -1
# rw[1,12] = 1
# # INICIALIZADO OS VALORES DE UTILIDADE COM ZERO - PODEM SER?VALORES ALEATORIOS
# value = matrix(0,1,12)
# # aplicando as equações de Bellman durante 10 iterações 
# for(i in 1:10){
#   value = update_value(T_up,T_down,T_right,T_left,rw,value)
# }
# # retornando a politica final
# policy = return_policy(T_up,T_down,T_right,T_left,value)
#