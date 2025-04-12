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

**Windows (using Command Prompt or PowerShell):**

**1. For Command Prompt:**

If you're using Command Prompt to set up your development environment, you can run the `setup.bat` script:

```cmd
setup.bat
```
This will:
* Create a virtual environment (.venv).
* Activate the virtual environment.
* Install dependencies listed in requirements.txt.
* Set the `PYTHONPATH` for module imports.

**2. For PowerShell:**

If you're using PowerShell to set up your development environment, you can run the `setup.ps1` script:

```powershell
.\setup.ps1
```

This will:
* Create a virtual environment (.venv).
* Activate the virtual environment.
* Install dependencies listed in requirements.txt.
* Set the PYTHONPATH for module imports.

#### Running the Project
Once your virtual environment is set up, you can run the task scripts.

**1. Running the Tasks in VS Code**

Once the virtual environment is activated and `PYTHONPATH` is set, you can run each of the task files directly from VS Code. Make sure that your `settings.json` (in `.vscode` folder) is correctly set up, as discussed previously.

* **Task 1:**
  ```bash
  python src/task_1/main.py
  ```
* **Task 2:**
  ```bash
  python src/task_2/main.py
  ```
* **Task 3:**
  ```bash
  python src/task_3/main.py
  ```
* **Task 4:**
  ```bash
  python src/task_4/main.py
  ```

VS Code will automatically use the virtual environment and set the correct `PYTHONPATH` if you’ve configured your settings properly.

**2. Running the Tasks from the Command Line**

After setting up your virtual environment and setting the `PYTHONPATH`, you can run the tasks directly from the terminal.

Each of these commands will run the corresponding task script:

```bash
python src/task_1/main.py
```
```bash
python src/task_2/main.py
```
```bash
python src/task_3/main.py
```
```bash
python src/task_4/main.py
```

<details>

<summary>Assignment 1 - Calculate salary from data in a file</summary>

#### Solution:

Solution for this task is located in the [src/salary_calculator.py](./src/salary_calculator.py) file.

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
