# Custom Protocol Handler Maker

This tool allows you to create custom protocol handlers, such as `vscode://` and `steam://`.

The way this works is dependent on your operating system.

For Windows, this tool will modify the registry by adding (or deleting) protocol handlers from `HKEY_CLASSES_ROOT`.

For Linux, this tool will add a file to `~/.local/share/applications` and set `xdg-mime` to open the executable linked.

Mac OS is currently not supported, although the tool might work, no guarantee.

## Usage

This tool requires admin privileges to run (an elevated terminal for Windows or `sudo` for Linux users). As such, this sort of program should be treated with the utmost care.

Currently, there is no Linux binary yet. However, you can just download the source code, and invoke it with Python via

```bash
python3 custom_protocols.py --help
```

For Windows users, go to the releases section, download the exe and you can run
`custom_protocols.exe --help` in either PowerShell or Command Prompt to get started.

## A note for Linux users

Through my testing, the browser (Firefox Snap) did not register in the browser. I had to use `xdg-open {protocol_handler}` in the terminal to get it to work.

## Precautions

This tool holds no precautions. It trusts you as a person to know what protocols you have made. As such, if you slip up and accidentally run something like:

```powershell

custom_protocols.exe delete http
```

That handler (which handles opening your browser and going to different sites) will be gone. The good news is that it'll only remove protocol handlers. However, keep the precaution high.

## FAQ

1. Why doesn't the tool automatically ask to escalate?

Python doesn't work very well when doing that and plus, it's a potential security risk.
2. What other features do you plan on implementing?

* A list of all available protocol handlers.

3. Why Python?
It was way easier than any other tool out there. PyInstaller automatically created a binary. It's seamless.
