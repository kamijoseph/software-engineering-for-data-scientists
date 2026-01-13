
# chapter ten: sharing code: version control, dependencies, and packaging
- sharing your code and collaborating with others is hugely important to your success in data science. you might join an existing project that has a large codebase. You might start by working on your code in isolation, but as your project grows, you may want to share it with others so that they don’t need to solve the same problems as well. or you could be contributing to open source projects.
- you’ll need to know some tools and techniques that make it easier for multiple people to work on the same code.
- version control is important because it’s the standard way of collaborating on a codebase.

## version control using git
- version control is a way of tracking what changes have been made to a codebase, and it allows multiple people to work on the same code easily.
- lets you see who made what changes to the code, and it prevents conflicts if two people are working on the same line of code.
- if someone makes a change that causes a bug, or you make a mistake in your code, it’s easy to go back to the previous version of the code.
- copy of the code is stored on every developer’s machine and also saved in a central location.
- `git` is the most popular system for distributed version control. its open source created by linus torvalds in 2005
- `github`, by microsoft, is the most popular remote site for storing code tracked using git but there is no official link between the two. other sources include `gitlab` nd `bitbucket`.

    ### how does git work
    - works on the basis that each project you’re working on is stored in its own directory, and you’d like to keep track of all the changes to the code in that directory.
    - the underlying data stored by Git is a snapshot of the state of all the files and the folder structure of the directory you are tracking.
    - you have a history of all the changes that you (or someone else) have made to that code.
    - a local repository stores the state of your project code on your computer, but you can also have a remote repository. this is a copy of your project code on a central server such as GitHub.