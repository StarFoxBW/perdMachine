import socket
import winsound
import time

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


sound_file_path = 'C:\\Users\\user\\Music\\meme\\fart.wav'

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

while True:
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('192.168.1.207', 1488))
        print("Подключение успешно!")
        
        while True:
            data = client_socket.recv(1024)
            if data == b'play_sound1-2' or data == b'play_soundALL':
                backVol = volume.GetMasterVolumeLevel()
                winsound.PlaySound(sound_file_path, winsound.SND_FILENAME)
                volume.SetMasterVolumeLevel(-1.0, None)
                
                time.sleep(2)
                volume.SetMasterVolumeLevel(backVol, None)

    except socket.error:
        print("Не удалось подключиться, пробую снова через 5 секунд...")
        time.sleep(5)
