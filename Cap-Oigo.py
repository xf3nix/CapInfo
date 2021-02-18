import subprocess
import socket
import time

def connect():

    while True:

        # Creando TCP/IP socket
        cont = 0
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind en socket para el puerto
        server_address = ('0.0.0.0', 1604)
        print('Escuchando en {} puerto {}'.format(*server_address))
        sock.bind(server_address)

        # Escuchando
        sock.listen(1)

        # Esperando conexion
        print('Esperando conexion')
        connection, client_address = sock.accept()
        cont += 1
        named_tuple = time.localtime() # Obteniendo time
        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
        date = (time_string)

        try:

            B = 0
            
            print('Conexion de ', client_address)

            while True:

                # Recibiendo datos en pequeños chunks y retransmitiendo                
                data = connection.recv(160)
                print('recibido {!r}'.format(data), voz)                

                if data and B == 0:               
                    data = []
                    paches = b'Conexion' + client_address, date
                    print('-------------------------------------------\n', time_string)
                    connection.sendall(paches)                 
                    B = 1  
                    time.sleep(8)
                else:                    
                    return False               

        finally:

            # Cierra la conexion
            guardar(connection, client_address, data, date)
            print("Conexion cerrada, reiniciando")
            connection.close()
            sock.close()            
           


def guardar(connection, client_address, data, date):
    # Guardando en Log
    
    f = open('log', 'a')
    f.write(str(client_address))
    time.sleep(0.5)
    f.write(str(data))
    time.sleep(0.5)
    f.write(str(connection))
    time.sleep(0.5)
    f.write(str(date))
    f.write('\n')
    f.close()

def main():
    subprocess.call('clear', shell=True)
    connect()

main()
