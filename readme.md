# Yvora documentation

## How it works
It behaves more or less like a terminal\
With the *and* symbol you can do multiple commands (despite errors)

> __Note__
Yvora is a full made terminal built in Python.

>__Warning__
Before running the code I'll recommend you using a Virtual Enviroment

Follow the following this steps:
- $ python3 -m venv ${your_env_name_directory}
- $ cd ${your_env_name_directory}
- On Windows: > Scripts\Activate.ps1
- On Linux: $ source bin/activate

## How to run the code
Use your system bash and run the file: __setup.py__

## How to import a new project
The stucture it's quite simple:

>:file_folder: bin    - Python Projects\
:file_folder: root - File Directories\
:file_folder: src - Local Storage\
:file_folder: utils - Python Hooks\
:memo: interface.py - Main Output\
:heavy_dollar_sign: __setup.py__ - Executable and  project reloader

### Adding new content automatically

- Type the order `new`
- Complete the form
- It will create a new project on ./bin/__Project.py__
- Now try it by executing __project__

### Adding new content manually

>__Warning__
Follow the project structure or it may not work properly

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
