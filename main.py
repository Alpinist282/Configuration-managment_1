from config_reader import read_config
from virtual_fs import VirtualFileSystem
from shellgui import ShellGUI

if __name__ == "__main__":
    # Чтение конфигурационного файла
    user_name, computer_name, zip_path, script_path = read_config(r"C:/Users/kepel/Desktop/Configuration-managment_1/Configuration-managment_1/config.xml")
    
    # Создание виртуальной файловой системы
    vfs = VirtualFileSystem(zip_path)
    
    # Запуск графического интерфейса
    app = ShellGUI(user_name, computer_name, vfs)
    app.mainloop()