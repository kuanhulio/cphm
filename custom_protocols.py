import ctypes, sys, os
import click
from utils.linux_desktop_entry import add_protocol_handler_linux, delete_protocol_handler_linux

def is_admin():
    is_root = False

    if os.name == "nt" and ctypes.windll.shell32.IsUserAnAdmin() == 1:
        is_root = True
    elif os.name == "posix" and os.getuid() == 0:
        is_root = True
    else:
        is_root = False
    
    return is_root

def is_windows():
    return os.name == "nt"

@click.group()
def cli():
    pass

@click.command()
@click.option('--name', prompt='Name of the protocol handler', help='Name of the protocol handler')
@click.option('--path', prompt='Path to the executable', help='Path to the executable')
def add(name, path):
    """Add a new protocol handler to the registry"""
    if is_admin():
        if is_windows():
            from utils.windows_registry import add_protocol_handler
            add_protocol_handler(f"{name}", f"{path}")
            click.echo(f"Added {name} to the registry.")
        else:
            add_protocol_handler_linux(f"{name}", f"{path}")
            click.echo(f"Added {name} to the local applications folder.")
    else:
        print("You must run this program as an administrator or root.")
        sys.exit(1)
    
@click.command()
@click.option('--name', prompt='Name of the protocol handler', help='Name of the protocol handler')
def delete(name):
    """Delete a protocol handler from the registry"""
    if is_admin():
        if is_windows():
            from utils.windows_registry import delete_protocol_handler
            delete_protocol_handler(f"{name}")
            click.echo(f"Deleted {name} from the registry.")
        else:
            delete_protocol_handler_linux(f"{name}")
            click.echo(f"Deleted {name} from the local applications folder.")
    else:
        print("You must run this program as an administrator or root.")
        sys.exit(1)

if __name__ == "__main__":
    cli.add_command(add)
    cli.add_command(delete)
    cli()