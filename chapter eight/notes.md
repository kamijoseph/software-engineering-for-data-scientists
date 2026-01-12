
# chapter eight: design and refractoring
- in this chapter we will explore: how to design projects, how to arrange the code, refractoring code when the design changes.
- it will include ideas for how to organize and standardize the high level structure of the projects and breaking code into modular, reusable functions.
- good design, whether at the level of a whole project or at the level of indivindual functions has a number of benefits:
    1. if the project is standardized, it removes some of the mental load of switching from one project to another
    2. it is easier to reuse pieces of the code in other projects.
    3. it is easier to add new features.
- refractoring is the process of adjusting the structure of the code while keeping its behavior the same and this is a normal part of software engineering.

## project design and structure
- keeping the design somewhat standardized is very helpful as it reduces cognitive load of switching to a new project
- itd also easier to pick up work that someone else on the team has done if the standard design is shared.

    ### a) project design considerations
    - these questions will help design a project:
        1. what are the overall goals or aims of the projects. what is the overall problem needed to be solved. always have the big picture in mind to make sure all writen code is aimed at achieving that goal.
        2. what are the overall inputs and outputs of the project? for example, a machine learning project may take raw data as an input and output model predictions.
        3. who are the stakeholders in the project? how much do you need to do before you check in with them?
        4. what is the timeline of the project? what are the milestones or deadlines?
        5. what are the ideas you are going to try out? how much time can you spend on exploration and experimentation versus solving the problem needed?
        6. what is the likelihood that the scope of this project might change? or that some point in the future, the work you do hear could be reused for a different use case?
    
    ### b) an example of a machine learning project design and strucuture
    - there are many options for how to set up the file structure of a project, but one strategy is to use one file per step in the project. each of these steps often ends with saving some data.
    - steps typically include the following:
        1. load the data
        2. clean, and preprocess the data, then transform it into features suitable for machine learning.
        3. training the model.
        4. analyzing the model's perfomance on a validation dataset.
    - if you know that you are going to run some experiments to choose an initial model then turn the code into reproducible scripts, this could be a good design fo the project:

    ```yaml
    ├── README.md
    ├── requirements.txt
    │
    ├── notebooks
        │
        ├── explore_data.ipynb
        │
        └── try_regression_model.ipynb
    │
    ├── src
        │
        ├── __init__.py
        │
        ├── load_data.py
        │
        ├── feature_engineering.py
        │
        ├── model_training.py
        │
        ├── model_analysis.py
        │
        └── utils.py
    │
    ├── tests
        │
        ├── test_load_data.py
        │
        ├── test_feature_engineering.py
        │
        ├── test_model_training.py
        │
        ├── test_model_analysis.py
        │
        └── test_utils.py
    ```

    - breakdown:

    1. documentation and dependencies requirements:
    ```yaml
    ├── README.md
    ├── requirements.txt
    ```
    - these are documentation and dependenices requirements list which every project should have.

    2. research and experimentation notebooks:
    ```yaml
    ├── notebooks
        │
        ├── explore_data.ipynb
        │
        └── try_regression_model.ipynb
    ```
    - its good practice to keep notebooks for experiments and research in which you are trying out different models in their own folders

    3. source scripts:
    ```yaml
    ├── src
        │
        ├── __init__.py
        │
        ├── load_data.py
        │
        ├── feature_engineering.py
        │
        ├── model_training.py
        │
        ├── model_analysis.py
        │
        └── utils.py
    ```
    - its also good to keep scripts in their own folder. a common python convention is to put all the code for a package in a folder named src (short for "source")
    - useful to put "helper" functions that are reused in many places in a utils.py file

    4. tests:
    ```yaml
    ├── tests
        │
        ├── test_load_data.py
        │
        ├── test_feature_engineering.py
        │
        ├── test_model_training.py
        │
        ├── test_model_analysis.py
        │
        └── test_utils.py
    ```
    - keeping tests in a separate folder keeps things tidy and also lets the testing framework discover them easily. each file in the src folder gets its own tests

- this is just one option for structuring a project. once there is a project structure that works for many projects, it can be turned into a template and replicated using `Cookiecutter`, or using `Kedro` to help you set it up.

## code design
- `design is the art of arranging code` --sandi metz

    ### modular code
    - dividing the code base into indivindual classes and function is a critical step. its good to think what functions and classes are appropriate from the begining.
    - modular code means that your code is broken into small independent parts. it is much easier to work with modular code.
    - make sure each one class or function have a desifned purpose.. should be something that can be describable by a sentence for example "this functions cleans data and this other one creates a data visualizatioon"
    - try avoid coupling in the functions - which is when you change code in one location, then need to change something in another location.
    - consider these questions to think through what functions and classes are appropriate for the problem being solved:
        1. what common patterns are visible in the written code? this could be a data transformation or a piece of business logic.
        2. what components could be reused in many places? an example couuld be the transformation of some data from one timezone to another
        3. what is the purpose of the function you are writing? as far as posibble, each function or method should do only one thing.

    ### a code design framework
    - one framework you can think about to construct your function, class, or method is the following (adapted from “Six steps to more professional data science code” on Kaggle by Rachel Tatman):
        1. function name
            - well named, as it sets the intention for what you want the function to do.
        2. inputs
            - function's interface should stay consistent, so before writing the body of the function decide what the inputs should be
        3. behaviour
            - the body of the function or method contains the actual operations that it carries out, what you want the function to do.
        4. outputs
            - the outputs of the function are what you include in the return statement or can also be data saved to a file. also part of the interface.
    
    ### interfaces and contracts
    - a useful place to start when writing indivindual functions is to figure out what does it accept as an input and what does it return as an output
    - once inputs and outputs been decided on, you shouldnt change them as other components of the system may be depending on them, this is also known as contract.
    - its best to keep number of input arguments small: three or four atmost
    - function test should confirm that the contract is maintained by checking that the correct inputs are accepeted and the correct outputs are returned.

    ### coupling
    - when dividing code into pieces, its important to make sure that those pieces are as independent from each other as possible.
    - if changing one part of the code changes another, the complexity of the whole project increaces and becomes harder to work on.
    - term coupling describes dependence between functions or modules.

## from notebooks to scalable scripts
- if notebooks are a standard part of the project workflow, you may reach a point where you need to move away from them to python scripts that are needed to run repeatedly.

    ### why use scripts instead of notebooks
    - one disadvantage of using notebooks; because you can execute code in a different order from the order it is written in, and you dont need to run all the code in a notebook at once, the notebook doesnt always reflect the code you've actuallty run. this can make it diffucult to reproduce the steps taken.
    - notebook also dont work well with a number of standard software engineering tools mentioned in this book. its not as easy to lint, format, or type check notebooks as it is with a python script
    - version control doesnt capture what cells have been run in a notebook. you may need to use external tools to easily review the changes that has been made in a notebook.
    - a common point to switch from notebooks to scripts is when you move the code into a production environment where it will be run repeatedly and some companies may require this due to potential security risks from notebooks.

    ### creating scripts from notebooks