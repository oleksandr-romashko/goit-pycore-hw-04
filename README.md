# Python Programming: Foundations and Best Practices 2.0

### [# goit-pycore-hw-04](https://github.com/topics/goit-pycore-hw-04)

<p align="center">
  <img align="center" src="./assets/thumbnail.svg" width="200" title="Project thumbnail" alt="project thumbnail">
</p>


## Working with files and a modular system

This assignment consists of 4 parts in total, each specified separately and has a link to the solution file.

<details>

<summary>Assignment 1 - Calculate salary from data in a file</summary>

#### Solution:

Solution for this task is located in the [src/task01/salary_calculator.py](./src/task01/salary_calculator.py) file.

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