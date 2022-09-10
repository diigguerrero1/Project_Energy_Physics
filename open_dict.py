import yaml


__config = None


# Con esta funcion podemos leer nuestro archivo Yaml donde tendremos
# la configuración de los factores de conversion de km/h a m/s.


def dict_medidas():
    global __config
    if not __config:
        with open('dict_medidas.yaml', mode='r') as f:
            __config = yaml.full_load(f)

    return __config
