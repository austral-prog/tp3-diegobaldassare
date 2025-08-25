def slice_advanced():
    # Código a implementar utilizando input.

    # Ingresar un texto usando input e imprimir en pantalla el resultado de obtener los valores saltando de a 2 caracteres, pero sólo a partir del quinto carácter ( incluído )
    texto = input("Ingresa un texto: ")
    print(texto[4::2].lower())

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_advanced_test.py` o `python tp3_slice_advanced_test.py`