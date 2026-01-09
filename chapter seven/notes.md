
# chapter seven: testing your code
- a test is code that calls a function and checks that it does what it is supposed to do.
- it gives you evidence and confidence that your code is working correctly.
- tests gives guarantee that the code is working, and you will know  if a change made breaks the code.
- also important when you are the only one working on your code.
- they’re a safety net that will help ensure that your code keeps working when you change it, rather than needing to rely on your memory.
- there are two types of testing in building software:
    1. automated code testing
    2. user testing the entire software product

## why write tests
- testing helps future proof your code from scenarios such as os updates, library, language & package update, different environments etc etc.
- also gives you confidence to make changes without being afraid that your code will break in some way that’s hard to spot. it gives you a good signal that, if you make a change, your code still functions correctly.

    ### test driven development (tdd)
    - process where developer writes the tests before writing the function tht actually achieve the objectives of the project.
    - the aim is to use the tests to describe the requirements of the code, and the tests specify the expected behavior and the function’s inputs and outputs.
    - this approach isn’t appropriate for many data science projects because, at the start of a typical data science project, you don’t know exactly what functions you’ll need.

## when to test for data scientist
- in data science projects, it can be difficult to know exactly when to start writing tests.
- testing generally isn’t worth the time it takes in the exploratory phase of your project, because you don’t know what code will be useful in the future but when you need to reuse your code and modify it, that can be a good time to add a test.
- writing tests early in your project can help you catch simple mistakes such as inconsistent names, missing imports, spelling errors, or syntax errors. sometimes these aren’t caught by the code editor.
- another time to add a test is when something goes wrong in your code and you get an unexpected error. adding a test can help you find the source of the error.
- tests are also extremely helpful if you need to refactor your code.

## how to write and run tests:
- there are two common type of tests:
    1. unit tests
    2. integration test

    ### a basic test
    - the simplest test checks that a function runs correctly with the kind of inputs that you expect if everything is going correctly.
    - a good starting point can be things that you repeatedly want to display in a notebook as you’re developing your function.
    - tests can be structure in 4 stages as described in pytest docs:
        
        1. arrange: set up everything you'll need to run the function, for example load some data
        2. act: run the function you are testing
        3. assert: check that the result of running the function is what you expect.
        4. cleanup: make sure the test doesnt leave any trace behind. for example, if you have opened a file, make sure to close it.
    
    - example in chap_7.py and test.py
    - it’s common practice to put your tests in a separate folder and to start the names of the Python files containing your tests with test_. this keeps the tests separate from the rest of the code and allows automated test runners to find your tests.

    ### testing unexpected inputs
    - as well as the code works with the inputs expected, its useful to make the code robust by testing whether the code can handle unexpected inputs
    - these are known as edge cases, which are extreme or unusual examples of an input that require special handling.
    - examples include empty strings, or data of an incorrect type

    ### running automated tests with pytest
    - `Pytest` is a framework that handles finding, collecting, and running tests
    - if you use it or another test framework, you dont need to run every single test function if you have many functions or write boilerplate code to run all the tests.
    - installation:

    ```bash
    pip install pytest
    ```
    
    ```bash
    pytest test_script.py
    ```

    - if you want to run all the tests in a folder, simply use the command pytest on its own. 
    - pytest will recursively search all the files in the folder where you run this command, and it will run tests from files that match the pattern test_*.py or *\_test.py. Inside these files, it will run any test functions that start with test_.
    - pytest prints a message to show that the test has failed, and it highlights the exact line that failed. 
    - it also prints out the assertion error and shows the incorrect value that the code generated.
    - other testing frameworks options:
        1. unittest - standard python library
        2. tox - includes setting up a venv, install application, and managing dependencies & python versions.

## types of tests
- patric viafore in `Robust Python (o'reilly 2021)` identifies six types of tests commonly used in software engineering:
    1. unit tests - check that units of code, such as functions or classes, do whatever a developer expects
    2. integration tests - checks that a larger system is connected correctly
    3. acceptance tests - checks that the system does what the user expects.
    4. load tests - checks that the system still functions correctly with data and users increase
    5. security tests - checks that the system is resistant to attacks
    6. usability tests - checks that the system is intuitive to use.

    ### 1. unit tests
    - a unit test takes a small component of your code and runs a test on it, for example, testing a function or a class. 
    - you’d usually write these while developing your code or while debugging. should be quick to run, so is best to use small datasets and avoid operations that can take a long time such as connecting to a database.; its best to use fake data instead.
    - unit tests should be deterministic. they should always give the same result with the same inputs, so dont include anythig that has some random component to it

    ### 2. integration tests
