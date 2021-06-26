import socket
import time

HEADER = 64
PORT = 5555
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!quit'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
connected = True

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def dosyayaYaz(sonuc):
    with open("sonuc.txt", "w") as f:
        f.write(str(sonuc))
    
while connected:
    msg = input("Mesaj (Format: 2#+#2) => ")
    if msg.lower() == DISCONNECT_MESSAGE:  #Bağlantıyı sonlandırmak icin !quit yazmanız yeterlidir.
        print("BAGLANTI SONLANDIRILIYOR")
        connected = False
    else:
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        baslangic_zamani  = int(round(time.time() * 1000))
        client.send(send_length)
        client.send(message)
        sonuc = client.recv(2048).decode(FORMAT)
        bitis_zamani  = int(round(time.time() * 1000))
        gecen_sure = str(bitis_zamani - baslangic_zamani)
        print(sonuc)
        print(f"RTT {gecen_sure} ms")
        dosyayaYaz(sonuc)


