from loteria import Loteria

def mega_sena(aposta):

 sorteio = 0

 while aposta != Loteria.resultado:
   Loteria.sorteio()
   sorteio += 1
   if sorteio == 100000:
     break
 if aposta  == Loteria.resultado:
   print(f'os números da sua aposta foram sorteados após {sorteio} sorteio(s)')

 else:
   print(f'Após {sorteio} sorteios os números de sua conta ainda não foram sorteados. Os  últios números que sairam foram {Loteria.resultado}')

mega_sena([7, 47, 37, 8, 77, 12])

