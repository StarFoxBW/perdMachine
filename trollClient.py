import socket
import winsound
import time

sound_file_path = 'C:\\Users\\user\\Music\\meme\\fart.wav'

while True:
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('192.168.1.207', 1488))
        print("Подключение успешно!")
        
        while True:
            data = client_socket.recv(1024)
            if data == b'play_sound1-2' or data == b'play_soundALL':
                winsound.PlaySound(sound_file_path, winsound.SND_FILENAME)

    except socket.error:
        print("Не удалось подключиться, пробую снова через 5 секунд...")
        time.sleep(5)
