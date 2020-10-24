class FechaHora:
    __dia = 0
    __mes = 0
    __anno = 0
    __hora = 0
    __minutos = 0
    __segundos = 0

    def __init__ (self, dia=1, mes=1,year=2020,hora=0,minutos=0,segundos=0):
        if((hora<24 and hora>-1)and (minutos<60 and minutos>-1) and(segundos<60 and segundos>-1) and (mes>0 and mes<13)):
            if((year%400==0)or(year%100!=0 and year%4==0)):
                listames=[31,29,31,30,31,30,31,31,30,31,30,31]
            else:
                listames=[31,28,31,30,31,30,31,31,30,31,30,31]
            if(dia<=listames[mes-1] and dia > 0):
                self.__dia = dia
                self.__mes = mes
                self.__anno = year
                self.__hora = hora
                self.__minutos = minutos
                self.__segundos = segundos
            else:
                print("El dia esta fuera de rango")
        else:
            print("Hubo un error, verifique hora,minuto,segundos y mes")
    
    def Mostrar (self):
        print("{}/{}/{} {}:{}:{}".format(self.__dia,self.__mes,self.__anno,self.__hora,self.__minutos,self.__segundos))

    def __add__ (self,horas):
        if((horas>0) and (horas<24)):
            self.__hora=self.__hora + horas
            if((self.__anno%400==0)and(self.__anno%100!=0 and self.__anno%4==0)):
                listames=[31,29,31,30,31,30,31,31,30,31,30,31]
            else:
                listames=[31,28,31,30,31,30,31,31,30,31,30,31]
            
            if(self.__hora>23):
                self.__hora -= 24
                self.__dia += 1
            if(self.__dia > listames[self.__mes-1]):
                self.__dia -= listames[self.__mes-1]
                self.__mes += 1
            if(self.__mes > 12):
                self.__mes -=12
                self.__anno += 1
    def __sub__ (self,h):
        if((h>0)and(h<24)):
            self.__hora=self.__hora-h
            if((self.__anno%400==0)and(self.__anno%100!=0 and self.__anno%4==0)):
                listames=[31,29,31,30,31,30,31,31,30,31,30,31]
            else:
                listames=[31,28,31,30,31,30,31,31,30,31,30,31]
            
            if(self.__hora<0):
                self.__hora += 24
                self.__dia -= 1
            if self.__dia == 0:
                if(self.__mes)==1:
                    self.__dia=listames[11]
                    self.__mes=12
                    self.__anno-=1
                else:
                    self.__mes -=1
                    self.__dia=listames[self.__mes-1]
    
    def __gt__ (self,ho):
        return self.__hora > ho
