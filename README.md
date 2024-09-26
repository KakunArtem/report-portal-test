# How to Activate a Python Virtual Environment (venv)

## Prerequisites
- Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

## Steps to Activate a Virtual Environment

### 1. Open Terminal or Command Prompt
Depending on your operating system, open the appropriate command line interface:

- **Windows**: Command Prompt or PowerShell
- **macOS/Linux**: Terminal

### 2. Navigate to Your Project Directory
Use the `cd` command to change to your project directory where you want to create or activate the virtual environment.

```sh
cd path/to/your/project
```

### 3. Create a Virtual Environment (if not already created)
If you haven't created a virtual environment yet, you can do so with the following command:

```sh
python -m venv venv
```

This will create a directory named `venv` in your project directory containing the virtual environment.

### 4. Activate the Virtual Environment
The command to activate the virtual environment varies depending on your operating system:

#### On Windows
```sh
venv\Scripts\activate
```

#### On macOS/Linux
```sh
source venv/bin/activate
```

### 5. Verify the Activation
You can verify that the virtual environment is activated by checking the command prompt. It should now include the name of the virtual environment (e.g., `(venv)`).

```sh
(venv) your-username@your-computer:~/path/to/your/project$
```

### 6. Deactivate the Virtual Environment
When you're done working in the virtual environment, you can deactivate it by simply running:

```sh
deactivate
```
