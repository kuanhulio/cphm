# Custom Protocol Handler Maker

This tool allows you to create custom protocol handlers, such as `vscode://` and `steam://`.

The way this works is dependent on your operating system.

For Windows, this tool will modify the registry by adding (or deleting) protocol handlers from `HKEY_CLASSES_ROOT`.
For Linux, this tool will add a file to `~/.local/share/applications` and set `xdg-mime` to open the executable linked.
Mac OS is currently not supported, although the tool might work.
