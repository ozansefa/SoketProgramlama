import socket
import threading

HEADER = 64
PORT = 5555
SERVER = socket.gethostbyname(socket.gethostname())  #private ip adresini alır
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!quit'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #ipV4 ve TCP  
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'[YENI BAGLANTI] {addr} KURULDU')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            sonuc = islemYap(msg)
            print(f"[{ADDR}] {sonuc}")
            sonuc = str(sonuc).encode(FORMAT)
            conn.send(sonuc)
    conn.close()

def islemYap(msg):
    x = msg.split('#')

    sayi1 =   x[0]
    isaret =  x[1]
    sayi2 =   x[2]

    if(isaret == '+'):
        sonuc = int(sayi1) + int(sayi2)

    elif(isaret == '-'):
        sonuc = int(sayi1) - int(sayi2)

    elif(isaret == '*'):
        sonuc = int(sayi1) * int(sayi2)

    elif(isaret == '/'):
        sonuc = float(sayi1) / float(sayi2)

    else:
        print("(+,-,*,/) Islemlerinden birini secin!")

    return sonuc

def start():
    server.listen()
    print(f"[DINLENIYOR] {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[BAGLANTI SAYISI] {threading.activeCount() - 1}')

print("[BASLIYOR] SERVER BASLATILIYOR ...")
start()