import random

def obtener_eleccion_computadora():
    opciones = ['piedra', 'papel', 'tijera']
    return random.choice(opciones)

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == 'piedra' and computadora == 'tijera') or \
         (usuario == 'papel' and computadora == 'piedra') or \
         (usuario == 'tijera' and computadora == 'papel'):
        return "¡Tú ganas!"
    else:
        return "¡La computadora gana!"

def juego_piedra_papel_tijera():
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    usuario = input("Elige piedra, papel o tijera: ").lower()
    while usuario not in ['piedra', 'papel', 'tijera']:
        usuario = input("Entrada inválida. Elige piedra, papel o tijera: ").lower()
    
    computadora = obtener_eleccion_computadora()
    print(f"La computadora eligió: {computadora}")
    
    resultado = determinar_ganador(usuario, computadora)
    print(resultado)

if __name__ == "__main__":
    juego_piedra_papel_tijera()
