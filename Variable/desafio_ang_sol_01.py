#Notei que o código anterior esta desnecessaariamente complicado e bagunçado 😅. Essa aq é uma versão mais simplificada

class Momen_Sol:
    def __init__(self, horas,minutos):
        self.minutos= minutos
        self.horas= horas
#Nessa resolvi criar uma etapa de verificação simples
#Pro caso do usuário resolver pôr uma hora acima de 23 e minuto acima de 59
    def valid_tempo(self):
        match(self.horas, self.minutos):
         case(h, m) if h > 23 or m > 59:
           print("Forneça um horário válido por favor")
#basicamente para o loop se a condição(implementada qaundo chamo a funçaõ) for falsa
#se verdeiro, continua. 
#Serve pra não iniciar a funçaõ seguinte pro caso do usuário digitar algo como h=60 m=120 e bugar o terminal
           return False
        return True
    def eh_noite(self):
        match(self.horas):
           case (h) if h <6 or h >= 18:
             print('Não vejo o sol')
#Repetindo o inverso da lógica do bloco anterior. Trava o código nesse bloco, 
#sendo noite n faz sentido calcular o angulo do sol sem sol
             return True
        return False
    def zenite(self):
         match(self.horas, self.minutos):
            case (h, m) if h == 12 and m == 0:
             print("meio-dia, zênite")        
         return True
    def calc(self):
#Ao invés de criar uma lista e adicionar as horas válidas a partir de um contador
#A solução mais simples seria apenas subtrair 6. Isso atende aos requisitos e n é complicado
       return print(f"São {self.horas:02d}:{self.minutos:02d} \nSoma total de minutos a partir do nascimento do sol: {(self.horas-6) *60 + self.minutos}\nÂngulo do sol acima do horizonte:{((self.horas-6) *60 + self.minutos) * 0.25}°")
    
momento = Momen_Sol(12,30)
if momento.valid_tempo(): 
 if not momento.eh_noite():
  momento.zenite()
  momento.calc()
    