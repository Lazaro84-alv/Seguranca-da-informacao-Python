import time
from threading import Thread

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto+=velocidade
        time.sleep(0.5)
        print('Piloto: {} Km: {} \n'.format(piloto, trajeto))


t_carro1 = Thread(target=carro, args=[1, 'Alves'])
t_carro2 = Thread(target=carro, args=[2, 'Python'])

t_carro1.start()
t_carro2.start()