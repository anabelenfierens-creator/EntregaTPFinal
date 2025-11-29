productos ={
    "010QC":{"nombre":"queso crema", "fecha vencimiento":"11 de ago 2025", "Lote":"45285"},
    "025DL":{"nombre":"dulce de leche", "fecha vencimiento":"10 de ene 2027", "Lote":"45548"},
    "056HL":{"nombre":"harina leudante", "fecha vencimiento":"11 de ago 2029", "Lote":"48791"},
    "003PO":{"nombre":"polenta", "fecha vencimiento":"13 de feb 2026", "Lote":"98745"},
    "000VI":{"nombre":"vitina", "fecha vencimiento":"11 de ago 2025", "Lote":"12365"},
}
codigo=input("Ingrese el codigo del producto a consultar: ")
def consultarProducto(codigoProducto, listaProducto):
    if codigoProducto in listaProducto:
        print(listaProducto[codigoProducto])
    else:
        print("Sin stock")
consultarProducto(codigo, productos) 