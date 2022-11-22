# Yvora documentation

## How it works
It behaves more or less like a terminal\
With the *and* symbol you can do multiple commands (despite errors)

> __Note__
Yvora is a full made terminal built in Python.

## How to run the code
Use your system bash and run the file: __setup.py__

## How to import a new project
The stucture it's quite simple:

>:file_folder: bin\
:file_folder: root\
:file_folder: src\
:file_folder: utils\
:memo: interface.py\
:heavy_dollar_sign: __setup.py__

### Adding new content automatically

- Type the order `new`
- Complete the form
- It will create a new project on ./bin/__Project.py__
- Now try it by executing __project__

>__Warning__
Follow the project structure or it may not work properly

### Adding new content manually
- Open ./bin
- Now create your Python file and name it with capitals

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
