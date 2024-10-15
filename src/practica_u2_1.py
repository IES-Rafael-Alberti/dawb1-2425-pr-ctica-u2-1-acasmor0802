
COMANDOS = ["compra", "venta", "saldo", "reset", "fin"]
MENSAJE_ERROR = "*ERROR* Entrada inválida"


def comprobar_importe(valor: str) -> bool:
    try:
        float(valor)
        return True
    except ValueError:
        return False

def comprobar_comando(comando: str) -> bool:
    return comando in COMANDOS


def mostrar_mensaje_error():
    print("*ERROR* Entrada inválida")


def procesar_compra(saldo: float, importe: float) -> float:
    saldo = saldo - importe
    return saldo


def procesar_venta(saldo: float, importe: float) -> float:
    saldo = saldo + importe
    return saldo


def mostrar_saldo(saldo: float, cont_compras: int, cont_ventas: int):
    print(f"{saldo} ({cont_compras} compras y {cont_ventas} ventas)")


def resetear_saldo(saldo: float, cont_compras: int, cont_ventas: int) -> tuple[float, int, int]:
    print(f"{saldo} ({cont_compras} compras y {cont_ventas} ventas)")
    saldo = 0
    cont_compras = 0
    cont_ventas = 0
    return saldo,cont_compras,cont_ventas

def recuperar_comando_e_importe(linea: str) -> tuple[str, str]:
    lista_palabras = linea.split()

    if len(lista_palabras) == 1:
        return lista_palabras[0], None
    elif len(lista_palabras) == 2:
        return lista_palabras[0], lista_palabras[1]
    else:
        return None, None


def main():
    cont_compras = 0
    cont_ventas = 0
    saldo = 0
    encuentra_fin = False
    linea = []
    while not encuentra_fin:
        linea = (input("> "))
        comando, importe = recuperar_comando_e_importe(linea)

        if comando is None or not comprobar_comando(comando):
            mostrar_mensaje_error()

        elif comando in ("saldo", "reset", "fin") and importe is not None:
            mostrar_mensaje_error()
        
        elif comando == "saldo":
            mostrar_saldo(saldo)            
   
        elif comando == "reset":
            saldo, cont_compras,cont_ventas = resetear_saldo(saldo,cont_compras,cont_ventas)

        elif comando == "fin":
            break
            
        elif importe is None or not comprobar_importe(importe):
            pass
            
        else:

            if comando == "compra":
                procesar_compra(saldo,importe)
                cont_compras += 1

            elif comando == "venta":
                procesar_venta(saldo,importe)
                cont_ventas += 1


            
if __name__ == "__main__":
    main()