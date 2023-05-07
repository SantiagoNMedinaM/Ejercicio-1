class Email:
    __idCuenta= ""
    __dominio=""
    __tipoDom=""
    __contrasena=''
    def __init__(self,idCuenta = "",dominio = "",tipoDom = "",contrasena = ""):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDom = tipoDom
        self.__contrasena = contrasena
    def retornamail(self):
        return(str(self.__idCuenta + "@" + self.__dominio + "." + self.__tipoDom))
    def getDominio(self):
        return (self.__dominio)
    def crearcuenta(self, direccion):
       partes = direccion.split("@")
       self.__idCuenta=partes[0]
       parte2=partes[1].split(".")
       self.__dominio=parte2[0]
       self.__tipoDom=parte2[1]
       self.__contrasena= str(input("Ingrese contraseña deseada "))
    def cambiarcontrasena (self):
        contra1=str(input("Ingrese contraseña actual "))
        if self.__contrasena==contra1:
           self.__contrasena=str(input("Ingresar nueva contraseña ")) 
        else:
           print("La contraseña ingresada es incorrecta")
 