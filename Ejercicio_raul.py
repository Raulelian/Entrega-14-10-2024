carta = {
"aperitivo": "cilantro, cebolla, chile, ajo, tomates, aguacate, limón, sal",
"1º plato": "huevos, palitos cangrejo, atún, mayonesa, pimientos piquillo, pimiento verde, pimiento rojo, cebolla, vinagre de vino, sal, aceite de oliva",
"2º plato": "aceite de oliva, ajo, solomillo cerdo, cebolla, manzana, tomate, calabacín, brandy, vino de oporto, ciruelas, orejones de albaricoque, mostaza, piñones",
"postre": "chocolate amargo, mantequilla, azucar, huevo, sal, harina de trigo, nueces",
}


def crear_lista_compra (carta):
    resultado = []
    for elements in carta:
        ingredientes = carta[elements]
        resultado.append(ingredientes)
    return resultado

 
print(crear_lista_compra(carta))


