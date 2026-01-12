
# chapter nine: documentation
- documentation is often overlooked aspect of data science commonly left at the end of the project therefore it is either rushed or ommited completely.
- documentation is a crucial part of making your code reproducible.
- first, it’s important to consider who you’re writing the documentation for.are you recording your experiments for another data scientist who might take over your project in the future? are you documenting a piece of code that you think might be useful for other people on your team?
- other aspects of good documentation include being up to date: documentation is not useful if it is not maintained.
- good documentation should also be well structured. The most important information should be easiest to find, so put it at the start or make it obvious where to find it.
- Try to answer questions like this in your documentation:
    1. Why did you select the data you used in this project?
    2. What are the assumptions you are making about your data?
    3. Why did you choose this analysis method rather than another?
    4. are there circumstances where this analysis method does not work?
    5. What (if any) shortcuts did you take that could be improved later?
    6. What are some other avenues for future experimentation that you
    7. would suggest to anyone who works on this project in the future?
    8. What are the lessons you learned from this project?

## documentation within the codebase
- a readable codebase should contain text as well as code, in the form of comments, docstrings, and longer documents.
- hierachy of documentation within the codebase, from shorter to longer:
    1. names of functions, classes, and modules give information on what you should expect that piece of code to do.
    2. comments make a small individual point that adds extra information, similar to a footnote in a book.
    3. docstrings give a longer overview of what a function or class does, including details of any edge cases.
    4. API documentation shows what each API endpoint expects as its input and returns for its output.
    5. longer documents such as readmes and tutorials give an overview of how to use all the code in a project.