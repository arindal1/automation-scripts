# Bulk File Renamer 

This simple script uses OS library for renaming files in bulk.

For Unix based systems please execute the following command to create venv.
```
make init
source .venv/bin/activate
```

## How to use

Execute in the terminal: 
`py main.py C:\\path\\to\\your\\folder new_name` or `py main.py C:/path/to/your/folder new_name`

### Example

`py main.py C:/my/path sakura`

```
Readme.txt   -   sakura - (0).txt
Icon.jpg   -   sakura - (1).jpg
Image.png -   sakura - (2).png
```
