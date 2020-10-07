import random
import re
from Decrypt import Decrypt_c

exit = False
carac_min = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z,'
carac_may = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z,'
carac_esp = '!,@,#,$,%,^,&,*,),(,-,_,+,=,'
carac_num = '0,1,2,3,4,5,6,7,8,9,0'

caracteres = carac_min + carac_may + carac_esp + carac_num + ' '

char_lst = caracteres.split(',')

random.shuffle(char_lst)

rand_num = random.randint(0,10)

codificacion=''.join(char_lst)

#print(codificacion)
#print(rand_num)

while exit == False:

    def encriptar(msj):
        encriptacion = ''
        for i in msj:
            indice = codificacion.find(i)
            n_indice = (indice+rand_num)%len(codificacion)
            encriptacion += codificacion[n_indice]
        print (f'El mensaje encriptado es: {encriptacion}\n')

    def desencriptar(msj):
        dec_msj = Decrypt_c(msj,rand_num, codificacion).desencripta_mensaje()
        print(f'El mensaje desencriptado es: {dec_msj}\n')

    try:
        opcion = input('Escoge una opción:\n1. Encriptar Mensaje\n2. Desencriptar Mensaje\n3. Salir\n')

    except:
        print('Debes introducir un número')

    if len(re.findall('[a-zA-Z\s]', opcion)) > 0:
        print('\nDebes introducir un número')

    if opcion == '1': #ENCRIPTAR
        mensaje = input('Introduzca un mensaje: ')
        print ('')
        encriptar(mensaje)
    elif opcion == '2': #DESENCRIPTAR
        mensaje = input('Introduzca el mensaje: ')
        print ('')
        desencriptar(mensaje)
    elif opcion == '3': #SALIR
        exit = True
    else:
        print('Opción no valida, intente de nuevo ...\n')
