import socket
import winsound

sound_file_path = 'C:\\Users\\user\\Music\\meme\\fart.wav'

# Настройки клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.207', 1488))  # Укажите IP-адрес сервера

while True:
    data = client_socket.recv(1024)
    if data == b'play_sound1-2' or data == b'play_soundALL':
        winsound.PlaySound(sound_file_path, winsound.SND_FILENAME)
