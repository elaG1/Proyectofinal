from lifestore_file import lifestore_products,lifestore_sales,lifestore_searches

if __name__=="__main__":
    usuario="Ilse"
    contraseña= "Taec2"

# En esta parte se usa el bucle while para que si el usuario introduce el usuario incorrecto 
# imprima "usuario incorrecto" y vuelva a preguntar hasta que sea correcto, y una vez que lo sea,
# pregunte la contraseña; si esta es incorrecta imprime "contraseña incorrecta" y se coloca
# continue para que vuelva a preguntar el usuario, es decir, comenzar de nuevo, pero si la contraseña es correcta,
# imprime "Bienvenid@" y el nombre del usuario y procede a mostrar el reporte

while True:
    login_de_usuario=input("Introduce to login de usuario: ")
    if login_de_usuario == usuario:
        password=input("Introduce tu contraseña: ")
        if password == contraseña:
            print("Bienvenid@", usuario)
        else:
            print("Contraseña incorrecta")
            continue
    else:
        print("Usuario incorrecto")
        continue
 
    # El reporte comienza mostrando una lista de las categorías que hay en LifeStore
    # Primero se crea una lista llamada categorias para agregar cada categoria que se encuentre en la tienda
    # Se crea un bucle for en el que se itera sobre la lista de productos y si la categoría de cada producto
    # aún no se encuentra en nuestra lista de categorias, se agrega

    print("-------------------------------------REPORTE 2020-------------------------------------","\n")
    print("* Este reporte se encuentra dividido en cuatro secciones: ventas, búsquedas, reseñas e ingresos *","\n")
    categorias=list()
    for producto in lifestore_products:
        categoria=producto[3]
        if categoria not in categorias:
            categorias.append(categoria)
    print("LAS CATEGORÍAS QUE HAY EN LIFESTORE SON: ",categorias,"\n")

    # Esta función servirá más adelante, para que al momento de mostrar resultados, en vez de imprimir el número
    # de mes, imprima su nombre, así que lo único que se hace después es llamar a la función para no tener que
    # escribir lo mismo cada que se necesite
    def nombre(mes):
        if mes == "01":
            print("Enero")
        elif mes == "02":
            print("Febrero")
        elif mes == "03":
            print("Marzo")
        elif mes == "04":
            print("Abril")
        elif mes == "05":
            print("Mayo")
        elif mes == "06":
            print("Junio")
        elif mes == "07":
            print("Julio")
        elif mes == "08":
            print("Agosto")
        elif mes == "09":
            print("Septiembre")
        elif mes == "10":
            print("Octubre")
        elif mes == "11":
            print("Noviembre")
        elif mes == "12":
            print("Diciembre")

    # En este parte, se crea una lista de los  meses, para que más adelante la información se pueda obtener
    # para cada mes. Con un bucle for, se itera sobre la lista de ventas (lifestore_sales), se usan índices 
    # para extraer el mes y se agrega a la lista meses si es que no estaba agregado; al final se ordena de menor a mayor
    meses=list()
    for fecha in lifestore_sales:
        mes=fecha[3][3:5]
        if mes not in meses:
            meses.append(mes)
    meses=sorted(meses,reverse=False) # False ordena de menor a mayor y True de mayor a menor

    # Esto también se usa más adelante. Se están calculando las ventas totales. Lo que hace es que
    # se itera sobre la lista de ventas (lifestore_sales) y suma 1 cada vez que lo hace
    ventas_totales=0 # Es un contador
    for sale in lifestore_sales:
        estado_devolución=sale[4]
        if estado_devolución==1:
            continue
        ventas_totales+=1

    # Se calculan las búsquedas totales. Se itera sobre la lista de búsquedas y se suma 1 cada vez
    busquedas_totales=0
    for search in lifestore_searches:
        busquedas_totales+=1

    print("---------------------------VENTAS------------------------------","\n")

    print("PARTE 1: PRODUCTOS MÁS VENDIDOS Y PRODUCTOS REZAGADOS","\n")
    print("- PRODUCTOS CON MAYORES Y MENORES VENTAS POR MES","\n")

    # En esta parte se usa la lista de meses anteriormente mencionada para obtener los 5 productos más vendidos y 
    # los 5 productos menos vendidos por mes. Se creó un diccionario para poder agregar el producto y su valor
    # asociado de ventas. Se comienza iterando sobre la lista meses, y para cada mes se itera sobre la lista de ventas.
    # Si el mes asociado a esa venta (mes_venta) es igual al mes en la lista de meses (mes) y el producto vendido
    # no se ha agregado al diccionario de ventas, entonces se agrega y su valor asociado va a ser 1 (una venta).
    # Si por el contrario, el producto ya estaba agregado, simplemente se le suma uno, esto para tener el conteo de
    # las veces que se encuentra en la lista de ventas cada producto, es decir el número de veces que se vendió
    # Posteriormente se crea una lista (ventas_list) en la que se agrega cada producto junto con su número de ventas
    # y se ordena del producto con mayores ventas al producto con menores ventas
    for mes in meses:
        ventas=dict()
        for sale in lifestore_sales:
            mes_venta = sale[3][3:5]
            estado_devolución=sale[4]
            producto_vendido=sale[1]
            if mes_venta == mes:
                if estado_devolución==1:
                    continue
                if producto_vendido not in ventas:
                    ventas[producto_vendido]=1
                else:
                    ventas[producto_vendido]+=1
                    continue
        ventas_list=list()
        for producto,ventas in ventas.items():
            ventas_list.append((ventas,producto))
        ventas_list=sorted(ventas_list,reverse=True)
        nombre(mes) # Se llama a la función que se creó al principio para que nos imprima el nombre del mes, en vez del
        # número de mes (que es como estan guardados los meses en la lista meses)
        print("Los 5 productos más vendidos (# de ventas, producto):",ventas_list[:5])
        print("Los 5 productos menos vendidos (# de ventas, producto):",ventas_list[-5:],"\n")


    print("-PRODUCTOS CON MAYORES Y MENORES VENTAS, ANUAL""\n")
    # El proceso es el mismo que el anterior solo que en este caso no se usa la lista de meses, ya que
    # lo que se pretende mostrar son los 5 productos más vendidos y los 5 productos menos vendidos en el año
    # así que se itera sobre la lista de ventas (lifestore_sales) para contar las veces que se vendió cada 
    # producto sin diferenciar entre meses
    ventas=dict()
    for sale in lifestore_sales:
        producto_vendido=sale[1]
        estado_devolución=sale[4]
        if estado_devolución==1:
            continue
        if producto_vendido not in ventas:
            ventas[producto_vendido]=1
        else:
            ventas[producto_vendido]+=1
            continue
    ventas_list=list()
    for producto,ventas in ventas.items():
        ventas_list.append((ventas,producto))
    ventas_list=sorted(ventas_list,reverse=True)
    print("Los 5 productos más vendidos (# de ventas, producto):",ventas_list[:5])
    print("Los 5 productos menos vendidos (# de ventas, producto):",ventas_list[-5:],"\n")
    

    print("-PRODUCTOS VENDIDOS POR CATEGORÍA, ANUAL""\n")
    # 1. Lo que se busca obtener son los productos que contiene cada categoría
    # Se itera sobre la lista de categorias (la que se obtuvo al principio) y para cada categoría se itera sobre
    # la lista de productos (lifestore_products). Si la categoria de un producto en la lista de productos 
    # es igual a la categoría en la lista de categorias, entonces agregamos dicho producto a una lista que se creó 
    # (productos_por_categoria), esto para obtener los productos pertenecientes a cada categoría
    for categoria in categorias:
        print(categoria)
        productos_por_categoria=list()
        ventas_por_categoria=dict()
        for producto in lifestore_products:
            categoria_en_lifestoreprod=producto[3]
            if categoria_en_lifestoreprod == categoria:
                idproducto=producto[0]
                productos_por_categoria.append(idproducto)
                # 2. A partir de aquí buscamos obtener los productos que se vendieron por categoría
                # Lo anterior nos dio una lista para cada categoria con sus productos. Se itera sobre esta lista 
                # (productos_por_categoria) y se crea un contador. Posteriormente se itera sobre la lista de ventas 
                # (lifestore_sales). Es decir, para cada producto en la lista de productos de cada categoria se itera 
                # sobre la lista de ventas. Si el producto en la lista de ventas es igual al producto en la lista de 
                # productos por categoría se suma 1 y se agrega el producto y su número de ventas al diccionario 
                # igualmente creado al principio (ventas_por_categoria), si no es igual se coloca continue para que
                # pase al siguiente producto. Después se agrega cada uno de los elementos del diccionario a una lista 
                # (ventas_categoria) y se ordena para mostrar los productos vendidos de cada categoría junto con su 
                # número de ventas de mayor a menor
                for producto_categoria in productos_por_categoria:
                    count=0
                    for sale in lifestore_sales:
                        producto_vendido=sale[1]
                        estado_devolución=sale[4]
                        if producto_vendido == producto_categoria:
                            if estado_devolución==1:
                                continue
                            count+=1
                            ventas_por_categoria[producto_categoria]=count
                        else:
                            continue
                    ventas_categoria=list()
                    for producto,ventas in ventas_por_categoria.items():
                        ventas_categoria.append((ventas,producto))
                    ventas_categoria=sorted(ventas_categoria,reverse=True)
                # 3. A partir de aquí lo que se busca obtener es el stock para cada producto de cada categoria
                # Se itera sobre la lista de productos_por_categoría y se agregan dichos productos a una lista llamada 
                # stock_productos_categoria. Se itera sobre esa lista y para cada producto en dicha lista se itera 
                # sobre la lista de productos (lifestore_products), si el producto en la lista stock_productos_categoria 
                # es igual al producto en lifestore_productos (idproducto), se agrega dicho producto al diccionario creado al 
                # principio (stock) junto con su valor de stock. Esto para tener el stock de los productos que pertenecen
                # a la categoría en turno. Posteriormente se crea una lista (stock_categoria) en la que se agregan los 
                # productos por categoria y su stock y se ordena de mayor a menor. 
                stock=dict()
                stock_productos_categoria=list()
                for producto in productos_por_categoria:
                    stock_productos_categoria.append(producto)
                    for producto in stock_productos_categoria:
                        for productols in lifestore_products:
                            idproducto = productols[0]
                            stockp=productols[4]
                            if producto == idproducto:
                                stock[producto]= stockp
                stock_categoria=list()
                for producto,stock in stock.items():
                    stock_categoria.append((stock,producto))
                stock_categoria=sorted(stock_categoria,reverse=True)
        print("Productos que contiene la categoría",categoria,":",productos_por_categoria)
        print("Productos vendidos (# de ventas, producto):",ventas_categoria)
        print("Productos más vendidos de la categoría (# de ventas, producto):",ventas_categoria[:5])
        print("Productos menos vendidos de la categoría (# de ventas, producto):",ventas_categoria[-5:])
        print("Stock por producto (stock, producto):",stock_categoria)
        # En esta parte se busca obtener las ventas totales por categoría y el porcentaje de ventas que cada
        # categoría representa como parte del total
        # Se crea un contador llamado count para contar el número de veces que los productos pertenecientes a cada
        # categoría aparecen en la lista lifestore_sales, es decir, cuántas ventas hubo del total de productos de 
        # cada categoría. Para esto se utiliza un bucle for que itera sobre la lista productos_por categoria
        # y si el producto de la categoria es igual al producto vendido, se suma uno al contador y se coloca continue
        # para que si no lo es pase al siguiente producto. Posteriormente se divide dicho conteo entre las ventas 
        # totales (ventas_totales), las cuales se calcularon al principio del programa, esto para obtener el porcentaje
        # que representan las ventas de determinada categoria sobre el total
        count=0
        for producto in productos_por_categoria:
            for sale in lifestore_sales:
                producto_vendido=sale[1]
                estado_devolución=sale[4]
                if producto == producto_vendido:
                    if estado_devolución==1:
                        continue
                    count+=1
                else:
                    continue
        print("Ventas totales por categoría: ",count)
        print("Porcentaje del total de ventas: ","{:.0%}".format(count/ventas_totales))

    # Productos devueltos en 2020
    # Se itera sobre la lista de ventas y si el estado de devolución es 1, se agrega el producto a la lista
    # productos_devueltos
    productos_devueltos=list()
    for sale in lifestore_sales:
        estado_devolución=sale[4]
        if sale[3][6:10]=="2020":
            if estado_devolución==1:
                productos_devueltos.append(sale[1])
    print("Productos devueltos en 2020: ",productos_devueltos,"\n")


    print("---------------------------BÚSQUEDAS---------------------------","\n")

    print("-PRODUCTOS CON MAYORES Y MENORES BÚSQUEDAS, ANUAL""\n")
    # Se itera sobre la lista de búsqueda (lifestore_searches) y si el producto no se ha agregado al diccionario
    # previamente creado (busquedas) se agrega y se le da un valor de 1 (una búsqueda), si por el contrario, el producto
    # ya estaba en el diccionario, se le suma 1, esto para tener el número total de búsquedas por producto. 
    # Posteriormente, se crea una lista (busquedas_list) y se le agregan los productos y su número de busquedas 
    # que estaban en el diccionario y se ordena de mayor a menor por búsqueda
    busquedas=dict()
    for producto in lifestore_searches:
        producto=producto[1]
        if producto not in busquedas:
            busquedas[producto]=1
        else:
            busquedas[producto]+=1
            continue
    busquedas_list=list()
    for producto,busqueda in busquedas.items():
        busquedas_list.append((busqueda,producto))
    busquedas_list=sorted(busquedas_list,reverse=True)
    print("Productos más buscados (# de búsquedas, producto):",busquedas_list[:10])
    print("Productos menos buscados (# de búsquedas, producto):",busquedas_list[-10:],"\n")

    # Se itera sobre la lista categorías y para cada categoría se itera sobre la lista de productos (lifestore_products)
    # Si la categoria de un producto en la lista de productos es igual a la categoria en la lista de categorías, 
    # se agrega el producto a una lista creada llamada productos_por_categoria. Esto para tener los productos 
    # pertenecientes a cada categoría. Posteriormente, se itera sobre dicha lista y se crea un contador y para cada 
    # producto de la categoria, se itera sobre la lista de búsquedas (lifestore_searches). Si el producto buscado 
    # (el que aparece en la lista de búsquedas) es igual al producto en la categoría se suma 1, esto para ver si el 
    # producto en la categoría se buscó y si es así, cuántas veces. Posteriormente, el producto se agrega a un 
    # diccionario si no estaba agregado, junto con su conteo (count). Después se crea una lista en la que se agregan
    # ambos valores y se ordena de mayor a menor para ver los productos más y menos buscados junto con su # de búsquedas
    print("-BÚSQUEDAS DE PRODUCTOS POR CATEGORÍA, ANUAL""\n")
    for categoria in categorias:
        productos_por_categoria=list()
        busquedas_diccionario=dict()
        print(categoria)
        for producto in lifestore_products:
            categoria_en_lifestoreprod=producto[3]
            if categoria_en_lifestoreprod == categoria:
                idproducto=producto[0]
                productos_por_categoria.append(idproducto)
                for producto_categoria in productos_por_categoria:
                    count=0
                    for producto in lifestore_searches:
                        producto_buscado=producto[1]
                        if producto_buscado == producto_categoria:
                            count+=1
                            busquedas_diccionario[producto_categoria]=count
                        else:
                            continue
                    busquedas=list()
                    sum=0
                    for producto,busqueda in busquedas_diccionario.items():
                        sum+=busqueda
                        busquedas.append((busqueda,producto))
                    busquedas=sorted(busquedas,reverse=True)
        print("Total de búsquedas por categoría:",sum)
        print("Busquedas como porcentaje del total:","{:.0%}".format(sum/busquedas_totales))
        print("Productos más buscados (# de búsquedas, producto):",busquedas[:5])
        print("Productos menos buscados (# de búsquedas, producto):",busquedas[-5:],"\n")

    print("----------------------------------------------------------------------------------------","\n")

    print("-----------------------------RESEÑAS----------------------------------","\n")
    print("PARTE 2: PRODUCTOS POR RESEÑA EN EL SERVICIO""\n")

    # Se usa de nuevo la lista de meses y con un bucle for se itera sobre dicha lista. De nuevo se usa la función
    # para imprimir el nombre de los meses. Para cada mes se itera sobre la lista de ventas (lifestore_sales). Si el
    # mes es igual al mes de venta y si el producto no se ha agregado a la lista (score) se añade y se cuenta 1 por 
    # cada vez que aparezca (count), esto para saber el número de ventas por mes que es lo mismo que el número de reseñas,
    # ya que todo producto vendido tiene reseña. Sum es para ir sumando el score cada vez que se encuentre el producto
    # en cada mes y average es para dividir la suma entre el conteo y tener el score promedio para cada producto en cada
    # mes
    print("-PRODUCTOS CON MEJORES Y PEORES RESEÑAS POR MES""\n")
    for mes in meses:
        nombre(mes)
        score=list()
        producto_score=dict()
        for producto in lifestore_sales:
            mes_venta=producto[3][3:5]
            if mes_venta == mes:
                producto_vendido=producto[1]
                if producto_vendido not in score:
                    sum=0
                    count=0
                    average=0
                    score.append(producto_vendido)
                    sum=sum+producto[2] #producto[2] es el score
                    count+=1
                    average=sum/count
                    producto_score[producto_vendido]=round(average,3)
                else:
                    sum=sum+producto[2]
                    count+=1
                    average=sum/count
                    producto_score[producto_vendido]=round(average,3)

        average_score_producto=list()
        for producto,score in producto_score.items():
            average_score_producto.append((score,producto))
        average_score_producto=sorted(average_score_producto,reverse=True)
        print("Productos con mejores reseñas (score promedio, producto):",average_score_producto[:5])
        print("Productos con peores reseñas (score promedio, producto):",average_score_producto[-5:],"\n")
        
    # Se realiza el mismo proceso que el anterior, pero sin iterar sobre la lista de meses, ya que 
    # lo que se pretende obtener son los productos y sus reseñas sin diferenciar entre meses
    print("-PRODUCTOS CON MEJORES Y PEORES RESEÑAS, ANUAL""\n")
    score=list()
    producto_score=dict()
    for producto in lifestore_sales:
        if producto[1] not in score:
            sum=0
            count=0
            average=0
            score.append(producto[1])
            sum=sum+producto[2]
            count+=1
            average=sum/count
            producto_score[producto[1]]=round(average,3)
        else:
            sum=sum+producto[2]
            count+=1
            average=sum/count
            producto_score[producto[1]]=round(average,3)

    average_score_producto=list()
    for producto,score in producto_score.items():
        average_score_producto.append((score,producto))
    average_score_producto=sorted(average_score_producto,reverse=True)
    print("Productos con mejores reseñas (score promedio, producto):",average_score_producto[:5])
    print("Productos con peores reseñas (score promedio, producto):",average_score_producto[-5:],"\n")

     # Score por categoría y por mes
     # Se realiza el mismo proceso que el anterior, solo que se itera sobre la lista de meses y sobre la lista de
     # categorías para obtener el score promedio por categoría y por mes
    print("-RESEÑAS PROMEDIO POR CATEGORÍA Y POR MES""\n")
    for mes in meses:
        nombre(mes)
        score=list()
        producto_score=dict()
        for categoria in categorias:
            sum=0
            count=0
            productos_por_categoria=list()
            ventas_por_categoria=dict()
            for producto in lifestore_products:
                categoria_en_lifestoreprod=producto[3]
                if categoria_en_lifestoreprod == categoria:
                    idproducto=producto[0]
                    productos_por_categoria.append(idproducto)
            for producto_categoria in productos_por_categoria:
                for sale in lifestore_sales:
                    reseña=sale[2]
                    mes_venta=sale[3][3:5]
                    producto_vendido=sale[1]
                    if sale[3][6:10]!="2020":
                        continue
                    if mes==mes_venta:
                        if producto_categoria==producto_vendido:
                            if categoria not in producto_score:
                                sum+=reseña
                                count+=1
                                average=sum/count
                                producto_score[categoria]=round(average,3)
                            else:
                                sum+=reseña
                                count+=1
                                average=sum/count
                                producto_score[categoria]=round(average,3)
        average_score_producto=list()
        for categoria,score in producto_score.items():
            average_score_producto.append((score,categoria))
        average_score_producto=sorted(average_score_producto,reverse=True)                     
        print(average_score_producto,"\n")

    print("----------------------------------------------------------------------------------------","\n")
    print("-----------------------------INGRESOS-------------------------------","\n")
    print("PARTE 3: TOTAL DE INGRESOS Y VENTAS PROMEDIO MENSUALES, TOTAL ANUAL Y MESES CON MÁS VENTAS AL AÑO","\n")

    # Se itera sobre la lista de ventas (lifestore_sales) y se agrega a la lista productos_vendidos cada uno de los 
    # productos, esto para obtener los productos que se vendieron. Después, se itera sobre esta última lista 
    # y para cada uno de dichos productos vendidos, se itera sobre la lista lifestore_products. Si el producto 
    # vendido es igual al producto en lifestore_products entonces agregamos al diccionario ingresos dicho producto 
    # y le asignamos el valor de su precio multiplicado por el número de veces que se vendió el producto, esto para 
    # tener al final el producto y el ingreso total que se obtuvo de todas sus ventas
    productos_vendidos=list()
    ingreso=dict()
    sum=0
    for producto in lifestore_sales:
        id_producto_vendido=producto[1]
        estado_devolución=producto[4]
        if estado_devolución ==1:
            continue
        productos_vendidos.append(id_producto_vendido)
        for producto_vendido in productos_vendidos:
            for producto in lifestore_products:
                idproducto=producto[0]
                if producto_vendido == idproducto:
                    precio=producto[2]
                    ingreso[producto_vendido]=precio*(productos_vendidos.count(producto_vendido))

    # Se crea una lista y en ella se agrega el ingreso total de cada producto del diccionario 
    # Se itera sobre dicha lista y con un bucle for se van sumando todos los ingresos para obtener el ingreso total
    # de la venta de todos los productos 
    ingreso_list=list()
    sum=0
    for (producto,ingreso) in ingreso.items():
        ingreso_list.append((ingreso))
    for valor in ingreso_list:
        sum=sum+valor
    print("Ingreso total: ",sum)
    print("Ingreso promedio mensual: ",round(sum/12,2),"\n")

    # Ingreso por mes
    # Se realiza el mismo proceso que el anterior pero se itera sobre la lista meses para tener el ingreso por mes
    print("-INGRESO POR MES, 2020:")
    for mes in meses:
        nombre(mes)
        productos_vendidos=list()
        ingreso=dict()
        sum=0
        for sale in lifestore_sales:
                if sale[3][3:5]==mes:
                    if sale[4]==1:
                        continue
                    else:
                        productos_vendidos.append(sale[1])
                        for producto_vendido in productos_vendidos:
                            for producto in lifestore_products:
                                idproducto=producto[0]
                                if producto_vendido == idproducto:
                                    precio=producto[2]
                                    ingreso[sale[1]]=precio*(productos_vendidos.count(sale[1]))

        ingreso_list=list()
        sum=0
        for (producto,ingreso) in ingreso.items():
            ingreso_list.append((ingreso))
        for valor in ingreso_list:
            sum=sum+valor
        print("Ingreso mensual:",sum,"\n")

    # Se dividen las ventas totales calculadas al principio y se divide entre doce meses. Se usa round para redondear
    # y despues del 12 se pone el número 2 para especificar que se quieren dos decimales
    print("Ventas promedio mensuales:", round(ventas_totales/12,2),"\n")

    # Meses con más ventas
    # Se itera sobre lifestore_sales y se agregan los meses en que ocurrieron las ventas a la lista lista_de_meses
    # Se itera sobre dicha lista y si el mes no está aún en el diccionario ventas_por_mes se agrega y se le 
    # asigna un valor de uno, si sí está, se le suma 1, esto para tener las ventas totales por mes
    # Después se agregan los meses y sus respectivas ventas totales a la lista top_ventas_mes y se ordena de 
    # mayor a menor
    ventas_por_mes=dict()
    lista_de_meses=list()
    for sale in lifestore_sales:
        estado_devolución=sale[4]
        if estado_devolución==1:
            continue
        lista_de_meses.append(sale[3][3:5])
    for mes in lista_de_meses:
        if mes not in ventas_por_mes:
            ventas_por_mes[mes]=1
        else:
            ventas_por_mes[mes]=ventas_por_mes[mes]+1
    top_ventas_mes=list()
    for mes,ventas in ventas_por_mes.items():
        top_ventas_mes.append((ventas,mes))
    top_ventas_mes=sorted(top_ventas_mes,reverse=True)
    print("Ventas por mes (mayor a menor):",top_ventas_mes,"\n")
    print("Mes con más ventas (# de ventas/mes):",top_ventas_mes[:1],"\n")
    print("Mes con menos ventas (# de ventas/mes):",top_ventas_mes[-1:],"\n")
    break # Se coloca break ya que al principio del programa empezamos con un bucle while, así que se pone
    # para que no vuelva a preguntar el login de usuario
    
