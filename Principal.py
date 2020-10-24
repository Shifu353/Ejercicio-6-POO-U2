from Clase_Fecha import FechaHora
if __name__ == '__main__':
    def op1 (horario):
        nuevo_horario=int(input("Ingrese hora a sumar "))
        Actualizado=horario+nuevo_horario
        horario.Mostrar()
    
    def op2 (horario):
        restar=int(input("Ingrese la cantidad de horas a Restar: "))
        resta=horario-restar
        horario.Mostrar()
    def op3 (horario):
        mayor=int(input("Ingrese hora para calcular el mayor: "))
        if(horario > mayor):
            print("La hora ingresada es menor")
        else:
            print("La hora ingresada es mayor")
    def op4 ():
        print("Gracias por usar el programa")
        print("Saliendo del Programa")

    d=int(input("Ingrese Dia: "))

    mes=int(input("Ingrese Mes: "))

    a=int(input("Ingrese Año: "))

    h=int(input("Ingrese Hora: "))

    m=int(input("Ingrese Minutos: "))

    s=int(input("Ingrese Segundos: "))

    horario = FechaHora(d,mes,a,h,m,s)
    diccionario={1:op1,2:op2,3:op3,4:op4}
    opcion=None
    while opcion!=4:
        print("|--------------------Menu de Opciones--------------------|")
        print("|Ingrese 1 para sumar hora                               |")
        print("|Ingrese 2 para restar hora                              |")
        print("|Ingrese 3 para destinguir entre dos horas cual es mayor |")
        print("|Ingrese 4 para Salir                                    |")
        print("|--------------------------------------------------------|")
        opcion=int(input("Ingrese Opcion: "))
        op=diccionario.get(opcion,lambda: print("Error vuelva a introducir una opcion"))
        if(op!=4):
            op(horario)
        else:
            op()
