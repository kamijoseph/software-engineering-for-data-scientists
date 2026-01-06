
# chapter 2: analyzing code perfomance

## introduction
- if you are writing code that forms part of a larger system, it is very important that your code is perfomant.
- it should return its output in a timely manner and shouldnt exceed the computing resources available.
- but first, and important is that the code  works and before optimising for perfomance make sure it solves the problem required and returns the expected outputs.
- second, ask whether there is a requirement for improved perfomance, you will need to know the expectations of the larger system your code is interfacing with
- for example, your machine learning model may need to return its prediction within 100 ms so that the prediction can be shown to the user. if your code already returns its result within the time allowed, there may be no need to spend time optimizing its performance.
- the first step to improving perfomance is to find out which parts of it are the slowest or taking up the most memory and once you collected data you can know whether these slow or memory hungry parts are things that can be fixed.
- "...premature optimization is the root of all evil (or at least most of it) in programming."

## methods to improve perfomance
- in this part, improving perfomance is defined on the context of minimizing the amount of computer resources the code uses.
- choice of methods to improve coe perfomance depends on programming language. in python:
    1. choice of algorithm - for example, avoid nested loops where possible so that you dont iterate through a list twice when you need to iterate through it just once.
    2. data structure choice - depending on a task, different data structures may have differet trade offs. for example it is easier to looka  value in a dictionary than in a list
    3. using built-in functions - most builtin functioons are implemented in c and they are almost always more efficient to use than custom write.
    4. compiling python - you may be able to get your code to run faster by compiling pythoon to a lower level languae using tools like cython, numba and pypy.
    5. asynchronous code - you may be able to speed up code by having it accomplish a task while it waits for the outcome of another. for example, yur code might be waiting for an api to return a response over a slow network.
    6. parallel and distributed computing - parallel computing means running code on more that one processor within a computer. can run your code on multiple CPUs at once using the multiprocessing module.distributed computing means running your code on multiple different machines at the same time.

## timing your code
- the simplest way of figuring out which parts of your code are slow is to measure the time taken to run a function or a line of code, make a change,then measure it again.
- it’s good practice to make only one change at a time because otherwise you can’t tell what caused the speedup or slowdown.
- code example:
    the example shows a simple piece of code that calculates the statistical mode of a list of numbers.
    check main.ipynb under timing code

## profiling your code
- profilers can tell you which part of a function takes the most time and give you extra levels of detail, making it easier to find the bottlenecks in your code.

    1. cprofile:
        - cProfile is the built-in profiler for Python, and you can use it to get a basic overview of the locations of bottlenecks in a longer script.
        - check notebook.ipynb code profiling.cprofile section for implementation
    2. line profiler:
        - The package line_profiler gives a much more readable breakdown of your code.
        - line_profiler isn’t installed by default, so you can install it using:
        
        ```bash
        pip install line_profiler
        ```
        ```python
        %load_ext line_profiler
        ```
        ```bash
        %lprun -f function
        ```
    3. memory profiling with memray
        - Memray is a memory profiling tool developed by Bloomberg that can give you different reports on the memory usage of your code.
        - You can install Memray using this command:

        ```bash
        pip install memray
        ```

        ```bash
        memray run script.py
        ```

        ```bash
        memray flamegraph memray-script.py.17881.bin

## time complexity
