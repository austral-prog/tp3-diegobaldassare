def slice_simple():
    texto = "Awesome"
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.


    # Obtener los siguientes datos del texto de ejemplo e imprimirlos en pantalla:
    #
    # Primeras 3 letras del texto ( usando índices positivos )
    # Las 3 letras en medio del texto ( usando índices positivos )
    # De la primera a la cuarta letra ( incluída ) y de la antepenúltima hasta la última ( incluída )
    # Es necesario que todos los caracteres se impriman en minúscula
    print(texto[:3].lower())
    print(texto[2:5].lower())
    print(texto[:4].lower() + texto[-3:].lower())

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
