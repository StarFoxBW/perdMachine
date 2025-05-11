import socket
import telebot

bot = telebot.TeleBot('7972988083:AAFoKwlCJGppE3wAmxe1vCdDGZgVcIvDsk8')


# Настройки сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.1.207', 1488))
server_socket.listen(12)

@bot.message_handler(content_types=['text'])
def troll(message):
    if '1-1' in message.text.lower():
        for client in clients:
            client.sendall(b'play_sound1-1')
    
    if '1-2' in message.text.lower():
        for client in clients:
            client.sendall(b'play_sound1-2')
    
    if '2-1' in message.text.lower():
        for client in clients:
            client.sendall(b'play_sound2-1')

    if '2-2' in message.text.lower():
        for client in clients:
            client.sendall(b'play_sound2-2')
    
    if '2-3' in message.text.lower():
        for client in clients:
            client.sendall(b'play_sound2-3')
    
    if '3-1' in message.text.lower():
        for client in clients:
            client.sendall(b'play_sound3-1')
    
    if '3-2' in message.text.lower():
        for client in clients:
            client.sendall(b'play_sound3-2')
    
    if '3-3' in message.text.lower():
        for client in clients:
            client.sendall(b'play_sound3-3')

    if '4-1' in message.text.lower():
        for client in clients:
            client.sendall(b'play_sound4-1')
    
    if '4-2' in message.text.lower():
        for client in clients:
            client.sendall(b'play_sound4-2')

    if '4-3' in message.text.lower():
        for client in clients:
            client.sendall(b'play_sound4-3')
    
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
