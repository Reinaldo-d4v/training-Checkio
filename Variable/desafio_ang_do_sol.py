#Sua tarefa é encontrar o ângulo do sol acima do horizonte, 
#sabendo a hora do dia. Dados de entrada: 
#o sol nasce pelo leste às 06:00, o que corresponde ao ângulo de 0 graus.
# Às 12:00 o sol atinge seu zênite, o que significa que o ângulo é igual a 90 graus. 
#18:00 é a hora do pôr do sol, então o ângulo é de 180 graus. 
#Se a entrada for a hora da noite (antes das 6:00 ou depois das 18:00),
# sua função deve retornar - "Não vejo o sol!".

#Confesso que repensei sobre oq estou fazendo da minha vida fazendo esse desáfio
class MomentoSol:
    def __init__(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto
        self.soma_de_minutos = None

    def tempo(self):

        match (self.hora, self.minuto):
            case (h, m) if h >= 24 or m > 59:
                print("Forneça um horário compatível por favor")
            case (h, m) if h < 6 or h >= 18:
                print('Não vejo o sol')

            case (h, m) if 6 <= h < 18 and 0 <= m <= 59:
                if h == 12 and m ==0:
                    print('meio-dia, zênite')
#Bem, pra contar apenas o número de horas válidas resolvi criar uma lista vázia
#e adcionar n termos a partir da hora fornecida (7-17)

                Qhoras=[] 
                for i in range(7,18):
#o contador só conta efetivamente a partir o 6 termo até h+1
                    if i > 6 and i<h+1:
                        Qhoras.append(i)
#Aqui jás o pulo do gato, 'h' deixa de ser o numero q eu usaria e dá espaço a len(Qhoras)
#que irá me dar apenas o numero de horas válidas a partir do contador(i) pra conversão de tudo pra minutos                    
                self.soma_de_minutos = len(Qhoras) * 60 + m
                print(f"Soma de minutos: {self.soma_de_minutos}")
            case _:
                print("Horário inválido")
    def calc_do_ang(self):
        print(f"São {self.hora:02d}:{self.minuto:02d}. O sol esta com inclinação de {self.soma_de_minutos * 0.25}° acima do horizonte")
momento = MomentoSol(60, 90)
momento.tempo()
momento.calc_do_ang()

        
