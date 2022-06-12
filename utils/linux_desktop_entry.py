import os

BASE_FILE ="""
[Desktop Entry]
Type=Application
Name={} Scheme Handler
Exec={} %u
StartupNotify=false
MimeType=x-scheme-handler/{};
"""

def add_protocol_handler_linux(name_of_handler: str, path_to_exe: str) -> int or Exception:
    """Add a new protocol handler to the local applications folder"""
    try:
        # Create the file
        with open(f"{os.getenv('HOME')}/.local/share/applications/{name_of_handler}.desktop", "w") as f:
            f.write(BASE_FILE.format(name_of_handler, path_to_exe, name_of_handler))
        # Run the command to tell xdg-mime to update the mime type
        # This is not necessary for the program to work, but it is necessary for the user to see the new protocol handler

        os.system(f"xdg-mime default {name_of_handler}.desktop x-scheme-handler/{name_of_handler}")    
        
        # Return 0; the operation was successful
        return 0
    except Exception as e:
        # Return the error message
        raise e

def delete_protocol_handler_linux(name_of_handler: str) -> int or Exception:
    """Delete a protocol handler from the local applications folder"""
    try:
        # Delete the file
        os.remove(f"{os.getenv('HOME')}/.local/share/applications/{name_of_handler}.desktop")

        # Return 0; the operation was successful
        return 0
    except Exception as e:
        # Return the error message
        raise e