import socket
import telebot

bot = telebot.TeleBot('7921650268:AAE3UHiJqcOfQaWBHOl1nTph0sZ5M-J6oJI')


# Настройки сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.1.207', 1488))  # Слушаем на всех интерфейсах
server_socket.listen(5)

@bot.message_handler(content_types=['text'])
def troll(message):
    if '1-1' in message.text.lower():
        for client in clients:
            client.sendall(b'play_sound1-1')
    
    if '1-2' in message.text.lower():
        for client in clients:
            client.sendall(b'play_sound1-2')
    
    if 'all' in message.text.lower():
        for client in clients:
            client.sendall(b'play_soundALL')

clients = []

def accept_connections():
    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        print(f'Подключен: {addr}')

if __name__ == "__main__":
    import threading
    threading.Thread(target=accept_connections).start()
    bot.infinity_polling()
