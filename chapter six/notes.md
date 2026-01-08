
# chapter six: code formatting, linting, and type checking
- code formatting, linting, and type checking tools analyze your code to check for mistakes or areas for improvement. code formatting tools concentrate on how your code looks, while linting and type checking tools ensure that your code functions correctly.
- consistent, standardized formatting makes your code much easier to read.
- linting and type checking tools help ensure that your code is robust. When you run Python code, syntax errors will crash your code straight away wherever they are in the script, but if you have another mistake (for example, a misspelled variable name) the error will not show up until this line. 
-  linters and associated tools can help you find some of these mistakes before you run your code.

## code formatting and style guides
- formatting your code according to a style guide is an important part of writing good code. A style guide can be set by a company, for example Google’s style guide, or if your company doesn’t have its own style guide, the default is to use PEP8.
- applying a consistent style makes code more readable. it’s faster to read new code if it’s in a consistent style, because it’s easier to read code if you know what you are expecting. 
- this consistency also makes it less likely that you will inadvertently introduce syntax errors, for example, with missing or mismatched parentheses. again, this is because it’s easier to know what to expect with standardized code.
    
    ### --> pep8
    - python enhancement proposal 8, or PEP8, is the document that sets the standards for Python formatting. it is a style guide written by Guido van Rossum, Barry Warsaw, and Nick Coghlan in 2001 as a style guide for the Python standard library as Python first started to become popular.
    - a style guide is about consistency. consistency with this style guide is important. consistency within a project is more important. consistency within one module or function is the most important.

    ### --> import formatting
    - importing external modules frequently causes bugs. it’s really easy to forget to update the modules you import when you update your code, so it’s good to have a clear list of the modules you are using. PEP8 sets standards for how to group your imports
    - imports should be grouped in the following order:
        1. standard library imports
        2. related third-party imports
        3. local application/library specific imports.
    - you can use the isort library fo that. example:
        --> before:

    ```python
    import time
    from sklearn.metrics import mean_absolute_error

    import sys, os
    import numpy as np
    from sklearn.model_selection import train_test_split
    import pandas as pd

    from sklearn.neural_network import MLPRegressor
    import matplotlib.pyplot as plt

    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.preprocessing import FunctionTransformer, OneHotEncoder
    ```

    - run isort:

    ```bash
    isort my_script.py
    ```
    after:

    ```python
    import os
    import sys
    import time
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from sklearn.metrics import mean_absolute_error
    from sklearn.model_selection import train_test_split
    from sklearn.neural_network import MLPRegressor
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import (FunctionTransformer, OneHotEncoder,StandardScaler)
    ```

## linting
- linting means checking your code for errors before it runs.
- python linters will analyze your code and warn you of some of the things that would cause your code to fail when you run it.
- an example could be misspelling a variable name or forgetting to import a module, both of which would cause your code to throw an error when you run it.
- common linting tools for Python include Flake8, Pylint, and Ruff.
- on vs code there is a pylance extension that helps with linting.

## type checking
- type checking is another way of catching bugs before they cause errors in your code. 
- the term “type” refers to categories of objects used by python such as integers (ints), strings, floats, and so on. 
- a mismatch between the type of the input that a function is expecting and the type of the input that it receives will cause an error.

    ### type annotations
    - also called type hints, were introduces in python 3.5 to help reduce the number of bugs caused by incorrect types.
    - they tell anyone reading code what type of input a function expects or returns.
    - type annotations are relatively new to Python, and they are still somewhat controversial. 
    - some people find that they help with readability, but other people find that they make code harder to read. 
    - there’s also extra work involved in adding the annotations and checking them.
    - example:

        ```python
        from collections import Counter

        def mode_using_counter(list_of_numbers: List[float]) -> float:
            c = Counter(list_of_numbers)
            return c.most_common(1)[0][0]

    ### type checking with mypy

    ```bash
    pip install mypy
    ```

    ```bash
    mypy my_script.py
    ```