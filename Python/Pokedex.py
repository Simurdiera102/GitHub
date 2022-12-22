# Construccion de una Pokedex

# Se construira un programa en el cual el usuario podra ingresar el nombre de un pokemon del cual quiera saber sus
# caracteristicas principales y su imagen, el programa contara con 3 opciones en las que el usuario podra agregar un Pokemon
# nuevo a la coleccion o podra ver los Pokemones que ya se hayan agregado anteriormente.
# Asi mismo, el usuario podra salir del programa cuando lo desee.

############################################################################################################################

# En este primer bloque del programa se importaran las librerias necesarias para realizar las tareas y funciones
# de la Pokedex

from urllib.request import urlopen
from PIL import Image
import matplotlib.pyplot as plt
import requests

# Se inicia estableciendo un ciclo while para asegurar que el prgrama va a funcionar hasta que el usuario lo decida.

while True:

    # En esta primera seccion del ciclo se le pregunta al usuario lo que desea hacer en el programa

    print("""
            ¿Que desea hacer?
            1. Agregar un nuevo Pokemon.
            2. Ver pokemones y caracteristicas que han sido agregados a la Pokedex.
            3. Salir de la Pokedex. 
            """)

    opcion = input(
        'Por favor ingrese una opcion: ')

# Luego, dependiendo de la opcion elegida por el usuario, se inicia con la accion que el usuario ha elegido.

    if opcion == '1':

        # Para la primera opcion se inicia creando las listas vacias necesarias para el manejo de la informacion,
        # fue necesario crear una lista para cada dato que contenia mas de 1 elemento ya que si se guardaba directamente
        # en los datos del pokemon solo se guardaba el primer dato.

        pokemones = []
        datos_pokemon = []
        lista_mov = []
        lista_hab = []
        lista_tip = []

# Se le pide al usuario que ingrese el nombre de un pokemon que conozca o quiera conocer.

        pokemon = input('Ingresa el nombre de un pokemon: ')

# Este es la url de la API de donde obtendremos los datos del programa.

        url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon

# Se incluye un manejo de excepciones respecto al tiempo de espera para que el programa finalice
# si los datos no son obtenidos desde la API en un tiempo igual o menor a 12 segundos

        try:
            respuesta = requests.get(url, timeout=12)
        except requests.Timeout:
            print('Error: tiempo de espera ha finalizado')

# En esta seccion se verifica que la respuesta sea la adecuada y que los datos sean obtenidos correctamente

        if respuesta.status_code != 200:
            print('Pokemon no encontrado')
            print('Vuelva a intentarlo')
            continue

# Se hace la conversion de los datos de respuesta a json para que python los pueda interpretar de manera correcta

        datos = respuesta.json()

# Se realiza un manejo de excepciones para verificar que el Pokemon ingresado si tenga una imagen relacionada en la API
# En caso de no tener ninguna imagen relacionada, el programa finalizara.
        try:
            url_imagen = datos['sprites']['front_default']
            imagen = Image.open(urlopen(url_imagen))
        except:
            print('El pokemon no tiene imagen')
            exit()

# En esta seccion del programa, se obtendran todos los datos del Pokemon que ha ingresado el usuario

        peso = datos['weight']
        datos_pokemon.append(peso)

        tamaño = datos['height']
        datos_pokemon.append(tamaño)

# Fue necesario crear ciclos for para obtener los datos de las secciones que tenian mas de 1 elemento.

        movimiento = datos['moves']
        for i in range(int(len(movimiento))):
            movimientos = movimiento[i]['move']['name']
            lista_mov.append(movimientos)
        datos_pokemon.append(lista_mov)

        habilidad = datos['abilities']
        for i in range(int(len(habilidad))):
            habilidades = habilidad[i]['ability']['name']
            lista_hab.append(habilidades)
        datos_pokemon.append(lista_hab)

        tipos = datos['types']
        for i in range(int(len(tipos))):
            tipo = tipos[i]['type']['name']
            lista_tip.append(tipo)
        datos_pokemon.append(lista_tip)

# Se realiza la consolidacion de todos los datos en la lista vacia de Pokemones

        pokemones.append(pokemon)

# En esta seccion se muestran los datos del pokemon ingresado.

        lista_datos = (
            f' Nombre: {pokemon} , Peso: {datos_pokemon[0]}\t  Tamaño: {datos_pokemon[1]}\t --- Movimientos: {lista_mov}\t --- Habilidades: {lista_hab}\t --- Tipo: {lista_tip}\t imagen: {url_imagen}\n')

        print('''Los datos del Pokemon son: 
            ''')
        print(lista_datos)

# Se abre un archivo de texto llamado Pokedex.txt el cual contendra toda la informaciond e los Pokemones que se consulten

        with open('Pokedex.txt', 'a') as f_Pokedex:
            for i in pokemones:
                f_Pokedex.write(f'{lista_datos} \n')
        f_Pokedex.close()
        print(f'Se ha agregado a {pokemon} a la Pokedex')
        print('Datos del Pokemon guardados en la Pokedex')

# Esta seccion muestra la imagen del Pokemon.

        plt.title(datos['name'])
        imgplot = plt.imshow(imagen)
        plt.show()

# En esta seccion se muestran los datos de todos los Pokemon que han sido agregados a la Pokedex.

    elif opcion == '2':

        with open('Pokedex.txt', 'r') as f_lectura:
            numero_pokemones = 0
            for i in f_lectura:
                numero_pokemones += 1
                print(f'Pokemon {numero_pokemones}: {i}')
        f_lectura.close()
        exit()

# Esta seccion es cuando el usuario desea salir de una forma segura de la Pokedex.

    elif opcion == 3:
        print('La pokedex se ha cerrado correctamente. Hasta pronto.')
        exit()

# Esta seccion contiene dos mensajes que se le mostraran al usuario cuando no ingrese ninguna de las 3 opciones.

    else:
        print('Opcion invalida')
        print('Volver a intentar')


# FIN DEL PROGRAMA
