
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