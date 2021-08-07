# Simulador de dado
# Simula o uso de um dado, gerando um valor de 1 até 6
import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um valor para o dado?'
    
    def Iniciar(self):
        reposta = input(self.mensagem)
        try:    
            if reposta == 'sim':
                self.GerarValorDoDado()
            elif resposta == 'não' or resposta == 'n':
                print('Agradecemos a sua participação')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao recever sua resposta')

    def GerarValorDoDado(self):
        print(random.randint( self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()