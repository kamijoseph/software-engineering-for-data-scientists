# chapter one: what is good code

## what makes good code:
- good code could be the code that runs the fastest, easy to read, easy to scale and adapt, reduced complexity.
- easier to add new features to the code.

## why good code matters:
- important when your data science code integrates with a larger system
- this could be putting a machine learning model into production, writing packages for a wider distribution, or building tools for other data scientists.
- most udeful for large codebases that will run repeatedly
- good code is easier to maintain.

## adapting to changing requirements:
- you should expect things to change during or after the project, therefore good code should be easy to adapt and this is key as the codebases grows
- as the project grows and gets broken out into multiple scripts or notebooks that depend on each other, it can become more complex and harder to make     changes.

## features of good code:
### 1. simplicity
- complexity makes it hard to modify code when the requirements change
- complexity is anything related to the structure of a system that makes it hard to understand and modify
- to avoid complexity:
    1. dont repeat yourself (dry)
        - all knowledge should have one single representation in code.
        - if information is repeated  in multiple places, and that information needs updating because of changing requirements, then one change means many updates and that is not feasible at large.
        - example in notebook.ipynb
        - mitigation: dont repeat code instead use functions or object oriented programming if necessary. check notebook.ipynb for robust code
        - comments and documentation can also be a form of duplication; same knowledge is represented in the code and the documentation that describes it. dont write comments that describe exactly wha the code is doing ; instead, use them to add more knowledge

- avoid verbose code
- soemtimes you can make code simpler by having fewer lines of code as this means fewer opportunitis for bugs and less code for someone else to read and understand. however there is a tradeoff between making it shorter and making it less readable
- avoid writing own functions while built-in functions exists
- avoid using unnecessary temporary variables
- example, instead of doing this:

```python
i = float(i)
image_vector.append(1/255)
```
you can:
```python
image_vector.append(float(i)/255)
```

instead of:
```python
for img in images:
    img = img / 255

```
do:
```python
img = [img/255 for img in images]
```
remark: not always as squeezing code into a fewer lines can sometimes be extremely hard for anyone else to understand what is goin on

### 2. modularity
- writing modular code means breaking a big system into smaller components
- makes code easier to read, easier to locate source of problems, easy to reuse in the next project and its easier to test code that is broken into smaller components.
- think far ahead into the future of the project as possible and try to anticipate what the overall system will do and what might be the most sensible place to divide it up.
a data science project can be divide in chucks:
    data collection --> explore the data --> clean the data --> visualise --> feature engineering and selection --> modelling and training --> evaluation --> hyperparameter tuning --> deployment
- check notebook.ipynb; modular code section

### 3. readability
- "...code is read much more often than it is written" PEP8
- methods to make code readable:
    1. standards and conventions.
        - Coding standards have been developed to encourage consistency across everyone writing Python code, and the aim is to make code feel familiar even when someone else has written it
        - the main coding standard for python is PEPS (python enhancement proposal 8) established in 2001
        - example: correct
        ```python
        spam(ham[1], {eggs: 2})
        ```
        - example: incorrect
        ```python
        spam( ham[ 1 ], { eggs: 2 } )
        ```
        - there are many automated ways to check that the code conforms with coding standards, which saves you from the boring work of going through and checking every tiny detail. Linters such as Flake8 and Pylint highlight places where your code doesn’t conform with PEP8.

    2. names
    - choice of names affects how easy it is to work with code. non-descriptive or non-precise names means remembering names meaning offhead which is unsustainable
    - example: bad
    ```python
    import pandas as p
    x = p.read_csv(f, index_col=0)
    ```
    - example good:
    ```python
    import pandas as pd
    df = pd.read_csv(input_file, index_col=0)
    ```

    3. cleaning up
    - clean up the code after you have finished creating a function.
    - once the code is tested and you are confident it is working, you should remove code that has been commented out and remove unnecessary calls to the print() function that you may have used as a simple form of debugging.
    - you may decide to refactor it. refactoring means changing the code without changing its overall behavior.

    4. documentation
    -code can be documented at multiple levels of detail, starting with simple inline comments, moving up to docstrings that explain a whole function, to the README page displayed in a github repo and tutorials teaching users how to use a package
    - might even explain your code in the future
    - write a good documentation for the audience to undersand the code functionality and features.

### 4. perfomance
- good code needs to be perfomant. this is measured in runtime and memory usage.
- its useful to know which data structures and algorithms are efficient
- you should be aware of which parts of the code are taking a long time
- performance is particularly important when you are writing production code that is going to be called every time a user takes a particular action. if the user base grows, or the project is successful, the code could be called millions of times every day.
- you dont want the code to be slow in production

### perfomance
- good code should be robust; it should be reproducible
- code should be able to run from start to end without it failing
- code should be able to respond gracefully if system inputs change unexpectedly; should respond to changes.
- code can be made robust by properly handling errors, logging what has happened, and writing good tests
    1. errors and logging
        - robust code shouldnt behave unexpectedly when it gets an incorrect input
        - decide if you wan code to crash at an unexpected input, or handle that error and do something about it.
        - For example, if your CSV file is missing half the rows of data you expect, do you want your code to return an error or continue to evaluate only half the data?
        - make a choice to give an alert that something is not as it should be, handle the error, or fail silently
        - if an error is handled, it can still be important to record that it has happened so that it doesnt fail silently, if thatss not what you want to happen
    2. testing
        - software engineer uses two main types:
            a) user testing - a person uses a piece of software to confirm that it works correctly
            b) automated testing - a common method is sending an example input into a piece of code and confirming that the output is the expected one
        - necessary because code may work on one machine or environment and fails at other machines and environments
        - data changes, libraries are updated and different machines run different versions of a language
        - there are several different types of tests:
            a) unit tests - test a single function
            b) end to end tests - test the whole project
            c) integration test - tests a chunk of code that contains many functions but is still smaller than the whole project.
        - a good strategy for getting started, if you have a large codebase with no tests, is to write a test when something breaks to ensure that the same thing doesnt happen again.

## summary
In summary, here are some ways to think about how to write good code:
    1. Simplicity
    Your code should avoid repetition, unnecessary complexity,
    and unneeded lines of code.

    2. Modularity
    Your code should be broken down into logical functions,
    with well-defined inputs and outputs.

    3. Readability
    Your code should follow the PEP8 standard for formatting,
    contain well-chosen names, and be well documented.

    4. Performance
    Your code should not take an unnecessarily long time to run
    or use up more resources than are available.

    5. Robustness
    Your code should be reproducible, raise useful error
    messages, and handle unexpected inputs without failing.