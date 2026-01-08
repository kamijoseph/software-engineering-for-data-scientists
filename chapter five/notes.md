
# chapter five: errors, logging and debugging

## errors in python
- an error is when the code stops unexpectedly before the program has completed all tasks it is supposed to do; also whatever depends on the code may also stop.
- sometimes you want it to stop but other times you want something else to happens so that the code continues running; handling the error.
- to makme code robust, it should be predictable for the set of things that are expected to happen

    ### a) reading python error messages
    - there are two types: syntax errors and exceptions. syntax errors arise when you write code that isn’t completely correct Python language, for example, failing to close parentheses or forgetting def in a function definition. these can’t be correctly parsed by the python interpreter, and the code stops and returns an error.
    - exceptions comprise all other errors, for example, a missing input to a function or trying to look up the value for a key that doesn’t exist in a dictionary.
    - python errors are printed as tracebacks. they show all the functions that were called that produced the error.
    - a good strategy for dealing with Python error messages is to start at the end of the message. the last line tells you what type of error you are dealing with (for example, nameError) and some information on how to fix the error, if python thinks it can help you.

    ### b) handling errors
    - if the function raises an error, it may cause a cascade of errors in a larger system. if this is the case, you should “handle” the error so that your code behaves predictably.
    - using try and except keywords:

    ```python
    try:
        # code you want to run
    except KeyError:
        # what to happen instead when an error of this type is raised
    ```

    - another feature of python error handling is `finally` block that runs whether or not an error is raised, and this must go after the try, except and the optional else blocks. mostly used to release a resource, such as closing an open file

    ### c) raising errors
    - in some circumstances, you might want the code to raise an error when something happens. you may also want any code that depends on the function to stop
    - in this situation, you use the `raise` keyword in python to raise an error even if it wouldnt normally trigger an error, and you can customize what error is that.
    - example"
    
    ```python
    def fit_trendline(year_timestamps, data):
        if not year_timestamps or data:
            raise ValueError("timestamp and data cannot be empty lists")
        # more functionality goes
    ```

    - you can also define custom errors if none of the python errors covers what you want. good practice for large projects, because you can give errors custom names to allow the code's users to asily tell where the error has come from. example (with inheritance):
    
    ```python
    class NewException(Exception):
    ```
    - using custom errors can make the code easier to read and maintain. when they are well defined, other parts of the code can handle specific errors and responfd appropriately ensuring that errors from different parts of the codebase do not get mixed up, therefore, preventing unintended consequences. also makes debbuging and trouble shooting more efficient.

## logging
- logging is a method of recording what your code has done in a separate file while it runs. this means that your code can communicate to other people what is going on, and this helps other people reason about your code.
- it helps make your code more readable and more robust because there is a record of what happens if it goes wrong.
- logging is hugely helpful in debugging a production system or a long-running task and serves as evidence that the code does what it is supposed to do

    ### a) what to log
    - the `logging` method lets you record whatever message you woulf like.
    - logging includes:
        1. a message to say that a long-running task has started or finished.
        2. error messages so that you know what has gone wrong in a production system.
        3. which functions called some other functions
        4. the inputs and outputs of a function
        5. the filepath where some data has been saved.
    
    ### b) logging configuration
    - the first configuration setting to consider is the severity level of the logs that get recorded
    - `logging` module has 5 different severity levels:
        from `DEBUG` --> least severe to `CRITICAL` --> most severe
    - these levels allows to easily find the messages you are looking for or only log messages above a certain level, depending on the use case.
    - the five criticality levels:
        1. `DEBUG` - detailed information, typically of interest only when diagnosing problems.
        2. `INFO` - confirmation that things are working as expecteed.
        3. `WARNING` - an indication that something unexpected happened, or indicative of some problem in the near future eg "disk space low"
        4. `ERROR` - due to a more serious problem the software has not been able to perfom some function.
        5. `CRITICAL` - a serious error, indicationg that the program itself may be unable to continue running.
         - default logging level in python `logging` modeule is `WARNING`
         - check noteboo.ipynb for more info

    ### c) how to log
    - it can be useful to add timestamp to the logs so that you know when the code ran that particular line of code and for easier searchiing later.
    - you can in configuration settings:

    ```python
    import logging
    logging.basicConfig(
        filename = "chapter_5_log.log",
        level = logging.DEBUG,
        format = "%(asctime)s %(message)s"
    )
    ```

    - it is a good idea to log error messages, as:

    ```python
    import logging
    logging.basicConfig(
        filename = "chapter_5_log.log",
        level = logging.DEBUG,
        format = "%(asctime)s %(message)s"
    )

    def fit_trendline(year_timestamps, data):
        logging.info("running fit_trendline function................")
        try:
            result = linregress(year_timestamps, data)
        except TypeError as e:
            logging.error("both lists must contain floats or integers.")
            logging.exception(e)
        else:
            slope = round(result.slop, 3)
            r_squared = round(result.rvalues**2, 3)
            logging.info(f"completed analysis. slope of the trendline is {slope}.")
            return slope, r_squared
    ```

## debugging
- Debugging means finding and removing bugs in your code.
- a bug is when your code is throwing unexpected errors or producing results that you don’t expect.

    ### a) strategies for debugging
    - a great starting point is to run an experiment. make small changes in the code and see how this affects the results while being sure to change only one thing at a time.
    - another top tip is to save a copy of whatever caused the error, whether this is the inputs to your function or the results of a particular database query. this is where logging can be very helpful, because you have a record of what has happened.
    - searching fo error messages on the internet is a great starting point.
    - talking to other people and developers is another great strategy of debugging. talk to other people or a rubber duck out loud makes you think through what you've been doing alittle differently than jus looking at the code.
    - another strategy of debugging is to take a break from coding and do somethinfg else like taking a walk, a workout, a puzzle etc. the solution might come to you as you do something completely unrelated.

    ### b) tools for debugging
    - an easy way of debugging is adding print statements to the code
    - there exists better debugging tools that can help with the debugging process.
    - debuggers use the concept of breakpoints. breakpoints are points you select where you want to pause code execution and inspect the state of some variable (or a saved file or database).
    - integrated development environments (IDE) such as visual studio code commonly include a deugger.
    - you also can still use a debugger even if you’re not using an IDE. pdb is a command line debugger that is included in the Python standard library.