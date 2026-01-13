
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
    - each commit should be about only one thing, for example, fixing a problem or adding one small feature.

    ### branches and pull requests
    - branches in Git let you isolate the changes you are making and try out new features without affecting the primary version of the code while still tracking the changes you have made.
    - useful when many people are working on the same codebase, because you can work on the same code without overlap.
    - making a branch doesn’t create a copy of the files containing your code. instead, Git tracks a set of changes introduced from a particular point in the project’s timeline. This means that you can easily work on different features and then merge the changes back into the original code.
    - all repositories have a default branch, usually named `main`.
    - to create a new branch:

    ```bash
    git branch new_branch
    ```

    - change where you are working to this branch:

    ```bash
    git checkout new_branch
    ```

    - you can combine the two commands;
    
    ```bash
    git checkout -b new_branch
    ```

    - after you have checked out the branch, any changes you make to the code on your computer will take place on your new_branch development branch, not the main branch.

    - saving a new branch to remote repo, run:
    
    ```bash
    git push origin new_branch
    ```

    - before merging, make sure to switch to the main branch:

    ```bash
    git checkout main
    ```
    - then merge:
    
    ```bash
    git merge new_branch
    ```

    - after merging you should delete that branch. the commit history will be preserved.
    - there may be merge conflicts when merging a branch. this arise when you have changed a line of code in new branch that has also been changed in the main branch. you will need to decide which version of this line to keep.
    - if you would like someone else to review the code before merging to branch, you can use the pull request. you can use the pull request interface on github.
    - a pull request should include comments to describe what you are changing, and why those changes should be made. This will help the reviewer know where to focus the discussion.

## python packaging
- if you want to make your code easy for other people to use, you can turn it into a package. this means that people can install it in their own Python environment, then import it into any project they are working on, in the same way you use NumPy or pandas.
- one of the biggest strengths of Python is its huge ecosystem of packages, and PyPI (the Python Package Index) enables this. PyPI hosts an enormous number of packages so that they’re available for you to download.
- a package ensures that your code is completely reproducible.

    ### packaging basics
    - before you start building your package, ensure that your code meets the following criteria so that users of your package get a good experience:
        1. meets the designed planned
        2. fully functional
        3. neatly formatted
        4. throroughly tested
        5. well documented.
        6. exists in a single folder
    
    - from pypi packaging involves the following steps:
        1. prepare a configuration file that contains metadata about the project and isntructions for a package building tool. the standard is poetry pyproject.toml file.
        2. use a tool that reads the source code and configuration file to turn it into a package file (or build artifact). this is what makes it installable on another person's system.
        3. upload the build artifact to pypi or some other distribution service.

    ### building and uploading packages