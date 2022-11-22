# Yvora documentation

Yvora is a full made terminal built in Python.\
So you basically need to have it installed before testing it.

## How it works
It behaves more or less like a terminal\
With the *and* symbol you can do multiple commands (despite errors)

## How to run the code
Use your system bash and run the file: __setup.py__

## How to import a new project
It's stucture it's quite simple:

>:file_folder: bin
file_folder: root\
:file_folder: src\
:file_folder: utils\
:heavy_dollar_sign: \_\_loader\_\_.py\
:memo: interface.py

### Adding new content
Open bin :file_folder:\
Now create your Python file and name it with capitals\
\
Create you Python file following the constructor architecture like this:

```python
class Project():
  def __init__(self, ...args):
    # Your code here
```

After you wrote your code make sure you added your project and arguments on `src/apps.json` like this:

```json
"project": {
        "help": "Blah blah blah",
        "creator": "You name",
        "version": "x.x.x",
        "args": ["foo", "bar", "baz"]
}
```
