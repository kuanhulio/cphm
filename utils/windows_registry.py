import winreg, os

HKEY_ROOT_PATH = winreg.HKEY_CLASSES_ROOT

def check_if_exe_exists(path_to_exe: str) -> bool:
    # Check if the executable exists
    if os.path.exists(path_to_exe):
        return True
    else:
        return False
    
def check_if_procotol_handler_exists(name_of_handler: str) -> bool:
    # Check if the protocol handler exists
    try:
        # Open the key
        key = winreg.OpenKey(HKEY_ROOT_PATH, f"{name_of_handler}", 0, winreg.KEY_READ)
        # Check if the key exists
        if key:
            return True
        else:
            return False
    except FileNotFoundError:
        return False

def add_protocol_handler(name_of_handler: str, path_to_exe: str) -> int or Exception:
    # Add a new protocol handler to the registry
    if not check_if_exe_exists(path_to_exe):
        raise Exception("The executable does not exist.")
    if check_if_procotol_handler_exists(name_of_handler):
        raise Exception("The protocol handler already exists.")
    try:
        # Create the key if it doesn't exist
        winreg.CreateKey(HKEY_ROOT_PATH, f"{name_of_handler}\\shell\\open\\command")
        key = winreg.OpenKey(HKEY_ROOT_PATH, f"{name_of_handler}", 0, winreg.KEY_WRITE)
        # Set the value of the key
        winreg.SetValueEx(key, "URL Protocol", 0, winreg.REG_SZ, "")
        winreg.CloseKey(key)
        # Open the key again to write the value
        new_key = winreg.OpenKey(HKEY_ROOT_PATH, f"{name_of_handler}\\shell\\open\\command", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(new_key, "", 0, winreg.REG_SZ, f'"{path_to_exe}"' + ' "%1"')
        winreg.CloseKey(new_key)
        # Return 0; the operation was successful
        return 0
    except Exception as e:
        # Return the error message
        raise e

def delete_protocol_handler(name_of_handler: str) -> int or Exception:
    # Delete a protocol handler from the registry
    if not check_if_procotol_handler_exists(name_of_handler):
        raise Exception("The protocol handler does not exist.")
    try:
        # Delete the key
        # This is recursive because winreg.DeleteKey() doesn't work for subkeys
        winreg.DeleteKey(HKEY_ROOT_PATH, f"{name_of_handler}\\shell\\open\\command")
        winreg.DeleteKey(HKEY_ROOT_PATH, f"{name_of_handler}\\shell\\open")
        winreg.DeleteKey(HKEY_ROOT_PATH, f"{name_of_handler}\\shell")
        winreg.DeleteKey(HKEY_ROOT_PATH, f"{name_of_handler}")
        # Return 0; the operation was successful
        return 0
    except Exception as e:
        # Return the error message
        raise e

