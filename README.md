# Python Programming: Foundations and Best Practices 2.0

### [# goit-pycore-hw-04](https://github.com/topics/goit-pycore-hw-04)

<p align="center">
  <img align="center" src="./assets/thumbnail.svg" width="200" title="Project thumbnail" alt="project thumbnail">
</p>


## Working with files and a modular system

This assignment consists of 4 parts in total, each specified separately and has a link to the solution file.

### Project Setup and Run Instructions

#### Prerequisites

Before starting, ensure that you have the following installed:

* Python 3.7+ (Make sure python and pip are available in your terminal)
* Git (optional, for version control)

#### Setting Up the Development Environment

**1. Clone the Repository**

If you haven't cloned the project yet, you can do so using:

```bash
git clone https://github.com/oleksandr-romashko/goit-pycore-hw-04.git
cd goit-pycore-hw-04
```

or download zip archive with code directly [from the repository](https://github.com/oleksandr-romashko/goit-pycore-hw-04/archive/refs/heads/main.zip).

**2. Create a Virtual Environment**

**Linux/macOS (using `bash` or `zsh`):**

Run the setup.sh script:

```bash
source setup.sh
```

This will:
* Create a virtual environment (`.venv`).
* Activate the virtual environment.
* Install dependencies listed in `requirements.txt`.
* Set the `PYTHONPATH` for module imports.

**Windows (using Command Prompt):**

If you're using Command Prompt to set up your development environment, you can run the `setup.bat` script:

```cmd
setup.bat
```
This will:
* Create a virtual environment (.venv).
* Activate the virtual environment.
* Install dependencies listed in requirements.txt.
* Set the `PYTHONPATH` for module imports.

#### Running the Project
Once your virtual environment is set up, you can run the task scripts.

**1. Running the Tasks in VS Code**

Once the virtual environment is activated and `PYTHONPATH` is set, you can run each of the task files directly from VS Code. Make sure that your `settings.json` (in `.vscode` folder) is correctly set up, as discussed previously.

VS Code will automatically use the virtual environment and set the correct `PYTHONPATH` if you’ve configured your settings properly.

**2. Running the Tasks from the Command Line**

After setting up your virtual environment and setting the `PYTHONPATH`, you can run the tasks directly from the terminal.

Each of these commands will run the corresponding task script (please note, that for Linux/macOS you might use `python3` instead of `python` command):

Run task 1:

```bash
python src/task_1/main.py
```

Run task 2:

```bash
python src/task_2/main.py
```

Run task 3:

```bash
python src/task_3/main.py
```

Run task 4:

```bash
python src/task_4/main.py
```

**Alternatively, you can use a script to run the tasks** (apply respective task number to run respective task script):

* **On Linux/macOS (shell script)**:

  Run task 1 with the script:
  ```bash
  ./src/task_1/run_task_1.sh
  ```

  Make sure the shell scripts have execution permission by running:

  ```bash
  chmod +x src/task_1/run_task_1.sh
  ```

* **On Windows (batch script)**:

  ```cmd
  src\task_1\run_task_1.bat
  ```

<details>

<summary>Assignment 1 - Calculate salary from data in a file</summary>

#### Solution:

Solution for this task is located in the following files:
* [./src/task_1/main.py](./src/task_1/main.py) - main entry point file.
* [./src/task_1/salary_calculator.py](./src/task_1/salary_calculator.py) - file with main business logic.

#### Task description:

There is a text file containing information about the monthly salaries of developers in your company.
Each line in the file includes a developer's full name and their salary, separated by a comma (with no spaces).

Example:
```
Alex Korp,3000  
Nikita Borisenko,2000  
Sitarama Raju,1000
```

The task is to write a function called `total_salary(path)` that analyzes this file and returns the total and average salary of all developers.

#### Task requirements:

1. The function `total_salary(path)` must accept a single argument — the path to the text file.
2. The file contains salary data separated by commas. Each line represents one developer.
3. The function should:
   1. Analyze the file
   2. Calculate the total salary
   3. Calculate the average salary
4. The function must return a tuple of two numbers: total salary and average salary.


#### Recommendations to the implementation:

1. Use a context manager `with` to read the file.
2. Don't forget to set the encoding when opening the file.
3. Use the `split(',')` method to separate the name and salary in each line.
4. Compute the total sum of all salaries, then divide it by the number of developers to get the average.
5. Handle possible exceptions, such as the file not existing.

#### Evaluation criteria:

1. The function must correctly calculate the total and average salaries.
2. It should handle cases where the file is missing or invalid.
3. The code should be clean, well-structured, and easy to understand.

#### Example:

Function usage:

```python
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
```

Expected result:

```shell
Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000
```

</details>

<details>

<summary>Assignment 2 - Get cat info from data in a file</summary>

#### Solution:

Solution for this task is located in the following files:
* [./src/task_2/main.py](./src/task_2/main.py) - main entry point file.
* [./src/task_2/cats_inventory.py](./src/task_2/cats_inventory.py) - file with main business logic.

#### Task description:

There is a text file containing information about cats. Each line of the file contains a unique identifier for the cat, its name, and age, separated by a comma. 

For example:
```
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
```

The task is to develop a function `get_cats_info(path)` that reads this file and returns a list of dictionaries containing information about each cat.

#### Task requirements:

1. The function `get_cats_info(path)` should accept one argument - the path to the text file (`path`).
2. The file contains data about cats, with each record containing a unique identifier, the cat's name, and age.
3. The function should return a list of dictionaries, where each dictionary contains information about one cat.

#### Recommendations to the implementation:

1. Use `with` to safely read the file.
2. Remember to set the file encoding when opening files.
3. For each line in the file, use `split(',')` to get the identifier, name, and age of the cat.
4. Create a dictionary with keys "`id`", "`name`", and "`age`" for each cat, and add it to the list, which will be returned.
5. Handle possible exceptions related to reading the file.

#### Evaluation criteria:

1. The function should correctly process the data and return the correct list of dictionaries.
2. Proper exception and error handling should be implemented.
3. The code should be clean, well-structured, and easy to understand.

#### Example:

Function usage:

```python
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
```

Expected result:

```shell
[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]
```

</details>

<details>

<summary>Assignment 3 - Directory Structure Visualizer</summary>

#### Solution:

Solution for this task is located in the following files:
* [./src/task_3/main.py](./src/task_3/main.py) - main entry point file with main business logic.

#### Task description:

Create a Python script that accepts a directory path as a command-line argument and visualizes the structure of that directory, displaying the names of all subdirectories and files. For better visual distinction, use different colors for directories and files.

#### Recommendations to the implementation:

1. First, install **colorama**. Use virtual environment and install package using `pip`.
2. Use `sys` module to get the path argument from the command line.
3. Use `pathlib` to work with files and directories.
4. Use `colorama` for styled terminal output.

#### Evaluation criteria:

1. Use of a virtual environment.
2. Correct handling and validation of the input directory path.
3. Accurate and visually structured output of the directory tree.
4. Proper use of colors for files and folders using **colorama**.
5. Code quality: readability, structure, comments.

#### Example:

If you run the script and pass an absolute path to a directory as a parameter:

```bash
python hw03.py /path/to/your/directory
```

This will result in the terminal displaying a list of all subdirectories and files in the specified directory, using different colors for directories and files to make the file structure easier to read visually.

For a directory with the following structure:

```
📦picture
 ┣ 📂Logo
 ┃ ┣ 📜IBM+Logo.png
 ┃ ┣ 📜ibm.svg
 ┃ ┗ 📜logo-tm.png
 ┣ 📜bot-icon.png
 ┗ 📜mongodb.jpg
```

The script should output a similar structure.

![task 3 output example](./assets/task_3_output_example.png)

</details>
