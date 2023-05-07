from email import Email
import csv
def test():
    nombre = str(input("Ingrese nombre "))
    id = str(input("Ingrese ID de la cuenta "))
    dom = str(input("Ingrese dominio de la cuenta "))
    tdom = str(input("Ingrese tipo de dominio de la cuenta "))
    contra = str(input("Ingrese la contraseña "))
    mail1 = Email(id,dom,tdom,contra)
    print("Estimado: "+ nombre +", te enviaremos tus mensajes a la direccion "+ mail1.retornamail())
    mail1.cambiarcontrasena()
    direccion = str(input("Ingrese Direccion de correo "))
    mail2 = Email()
    mail2.crearcuenta(direccion)
    print(mail2.retornamail())

def archivomails():
    mailvalidos = []
    archivo = open('Libro1.csv')
    reader = csv.reader(archivo)
    for fila in reader:
        if '@' in fila[0] and '.' in fila[0]:
            emails = Email()
            print("Para {}".format(fila))
            emails.crearcuenta(fila[0])
            mailvalidos.append(emails)
        else:
            print("El mail {} es invalido" .format(fila[0]))
    dominio = str(input("Ingrese dominio a buscar "))
    c=0
    for emails in mailvalidos:
        if dominio == emails.getDominio():
            c+=1
    print("Hay {} direcciones de email con el dominio {}" .format(c,dominio))
    return mailvalidos
          
        
        
if __name__ == '__main__':
    test()
    archivomails()
    

    

    


