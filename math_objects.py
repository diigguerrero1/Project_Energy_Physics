# Este modulo nos permite abrir un archivo Yaml donde tendremos
# los facores de conversion de km/h a m/s
from open_dict import dict_medidas



# Esta clase recibe como parametro una velocidad y la convierte de km/h a m/s

class Conversion_kmh_a_ms:

    def __init__(self, velocidad, medida='km/h'):
        self.velocidad = velocidad
        self.medida = medida
        
        self.valor_convertido = self.conversion()

    def conversion(self):  
        if self.medida == dict_medidas()['dict_medidas']['km/h'][0]:
            km_a_m = dict_medidas()['dict_medidas']['km/h'][1]['conversion_m']
            h_a_s = dict_medidas()['dict_medidas']['km/h'][2]['conversion_s']
            valor_en_ms = self.velocidad * km_a_m / h_a_s
        else:
            print("No se puede generar la conversión")

        return valor_en_ms



# Esta clase recibe como parametros la velocidad en km/h y la masa en kg
# y nos devuelve la energia cinectica

class Energia_cinetica:

    def __init__(self, velociadad, masa):
        self.velocidad = velociadad
        self.masa = masa

        self.velocidad_convertida = self.convertir()

        self.energia_cinetica = self.energia_cinetica()

    def convertir(self):
        velocidad_convertida = Conversion_kmh_a_ms(self.velocidad)
        return velocidad_convertida.valor_convertido

    def energia_cinetica(self):
        energia_cinetica = 0.5 * self.masa * self.velocidad_convertida**2
        return energia_cinetica



# Esta clase recibe como parametros la energia en Julios y la masa en kg y nos regresa
# la altura a la que caeriamos con la energia cinetica dada.

class Altura_sacada_de_energia_potencial:

    def __init__(self, energia, masa, gravedad=9.8):
        self.energia = energia
        self.masa = masa
        self.gravedad = gravedad

        self.altura = self.sacar_altura()

    def sacar_altura(self):
        masa_por_gravedad = self.masa * self.gravedad
        altura = self.energia / masa_por_gravedad
        return round(altura, 2)
