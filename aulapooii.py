'''class Elevador:
    def __init__(self):
        self.andar = 1
    
    def subir(self, num):
        if num >= 20:
            return 'Elevador está no ultimo andar!'
        else:
            andar_atual = num - 1
            self.andar += andar_atual
            return f'Elevador subindo - Andar {self.andar}'
    
    def descer(self, num):
        if num <= 1:
            return 'Elevador está no primeiro andar!'
        else:
            andar_atual = num - 1
            self.andar -= andar_atual
            return f'Elevador descendo - Andar {self.andar}'
        

elevador = Elevador()

escolha_andar = int(input('Escolha um andar: '))

print(elevador.subir(num=escolha_andar))

========================================================== HERANÇA COM POO =====================================
#HERANÇA SIMPLES
class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco


class Fisica(Pessoa):
    def __init__(self, nome, endereco, cpf):
        super().__init__(nome, endereco)
        self.cpf = cpf

class Juridico(Pessoa):
    def __init__(self, nome, endereco, cnpj):
        super().__init__(nome, endereco)
        self.cnpj = cnpj


pessoa_juridica = Juridico(nome='Diego', endereco='Rua XXXX',cnpj='000000000/0001-00')
pessoa_fisica = Fisica(nome='Carlos', endereco='Rua XXXX', cpf='000.000.000-00')

HERANÇA MULTIPLA:

class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco


class Fisica(Pessoa):
    def __init__(self, nome, endereco, cpf):
        super().__init__(nome, endereco)
        self.cpf = cpf

class Filhos(Fisica):
    def __init__(self, nome, endereco, cpf, carteira_vacina):
        super().__init__(nome, endereco, cpf)
        self.carteira_vacina = carteira_vacina'''
        
        
        
        
#Crie uma hierarquia de classes representando formas geométricas. Comece com uma classe base chamada
#"Forma"e, em seguida, crie classes derivadas como "Círculo" e "Retângulo" que herdem da classe base. 
#Adicione métodos para calcular área e perímetro emcada classe derivada.

'''class Forma:
    def __init__(self):
        pass

    def calcular_area(self):
        pass 

    def calcular_perimetro(self):
        pass 


class Retangulo(Forma):
    def __init__(self):
        super().__init__()
    
    def calcular_area(self, base, altura):
        area = base * altura
        return area
    
    def calcular_perimetro(self, base, altura):
        perimetro = (base + altura) * 2
        return perimetro
    
class Circulo(Forma):
    def __init__(self):
        super().__init__()

    def calcular_perimetro(self, raio):
        perimetro = (math.pi * raio) * 2
        return perimetro
    
    def calcular_area(self, raio):
        area = (math.pi * raio) ** 2
        return area
    

retangulo = Retangulo()
circulo = Circulo()

print(retangulo.calcular_area(base=4, altura=2))
print(retangulo.calcular_perimetro(base=4, altura=2))

print(round(circulo.calcular_area(raio=5),2))
print(f'{circulo.calcular_perimetro(raio=5):.2f}')'''

============================================================================================

Atividade 02:

class Veiculo:
    def __init__(self):
        self.cor = ''
        self.modelo = ''
    #Setter - Responsavel por apenas mandar informações e trocar os dados
    def mudar_cor(self, nova_cor):
        self.cor = nova_cor
    #Setter
    def mudar_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    # Getter - Responsavel por mostrar dados e nunca mudar
    def mostrar_cor(self):
        return self.cor
    
    def mostrar_modelo(self):
        return self.modelo
    
class Carro(Veiculo):
    def __init__(self):
        super().__init__()
    
    def mudar_cor(self, nova_cor):
        return super().mudar_cor(nova_cor)
    
    def mudar_modelo(self, novo_modelo):
        return super().mudar_modelo(novo_modelo)
    
    def mostrar_cor(self):
        return super().mostrar_cor()
    
    def mostrar_modelo(self):
        return super().mostrar_modelo()
    

carro = Carro()

print(carro.mudar_cor(nova_cor='Preto'))
print(carro.mudar_modelo(novo_modelo='Argo'))

print(carro.mostrar_cor())
print(carro.mostrar_modelo())

'''Sistema de gerenciamento de contas bancárias

em Python

Crie um sistema de gerenciamento de contas bancárias
em Python usando herança e polimorfismo. O sistema
deve incluir as seguintes classes:'''
        
        
        