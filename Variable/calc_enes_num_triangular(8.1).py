#No exemplo anterior acabei notando uma lacuna de conhecimento
#Essa resolução é mais pra desencargo de consciência
def calc_enes_num_triangular(N : int):
   #lista que guardara n termos
   trian = []
   #loop que nos dará os n termos
   for i in range (1,N+1):
        trian.append(i*(i+1)//2)
    #N termos por ordem e mostrando o numero triangular
   return f'{trian} O enesimo numero triangular é: {sum(trian)}' 
print(calc_enes_num_triangular(6))

    