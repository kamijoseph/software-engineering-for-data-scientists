
# chapter twelve: automation and deployment
- automating your coding processes helps ensure they are standardized and reproducible.
- you can make sure that your code is always linted, formatted, and tested before it reaches a production system, or even before it is committed to version control.
- automation also helps ensure that your processes are standard across your team. if tests are automated, everyone is more likely to run them, and there will be fewer mistakes in the team’s code. This can help you set up a culture of writing good code within your team.

## deploying code
- deploying your code means that you’ve reached some stage where you’re satisfied with the code you have, in contrast to the development stage of writing software where you’re trying out new ideas and constantly changing things.
- it’s common practice to have multiple environments where code can be deployed. before deploying your code to production, you might first deploy it to a testing environment.
- this means your code gets tested where it interacts with the rest of the software product, and it gets deployed to the production environment only after you’re sure that it doesn’t cause any problems.
- CI/CD - continuous integration / continuous deploment or delivery - refers to the whole pipeline of a deployment process, which may include running tests, security checks, and building and deploying containers.

    ### continuous integration
    - when a developer makes a change to a codebase and commits it to version control, a CI server builds the project, runs the tests, and checks that everythin works.
    - if there are errors, the CI system alerts developer so that they can fix them

    ### continuous delivery
    - after the CI has run, code is ready to deploy. it has passed all tests and the project has been built.
    - it then needs a manual final step to deploy it, which lets someone review it before deploying.

    ### continuous deployment
    - if al tests pass, the code automatically deploys to a production environment

- CI/CD systems require that your code is in version control, you have a good set of tests, and your whole team is on board with automating the system.
- in ML CI/CD can be triggered by changes to a model’s training data or by a decline in the model’s performance.
- the system retrains and redeploys the model when the selected trigger occurs.

## automation examples
- this section is aout automating some common tasks in  the coding workflow, such as using pre-commit hooks and lack, automatically removing data from jupyter notebooks before they reach the github repository
- also how to run tests automatically using github actions.

    ### pre-commit hooks
    - they are a type of Git hook, which is a custom script that runs before or after some Git action (such as a commit).
    - pre-commit hooks are useful because they let you identify problems before committing to version control.
    - particularly good for tasks that are easy to automate, such as linting and formatting. Using hooks for linting will detect poor practices and prevent poorly written code from being committed to the codebase.
    - you can also use pre-commit hooks to run unit tests, and this can be good for small projects.
    - pre-commit is a multilanguage framework that uses a `.yaml` file to manage configurations. `YAML (YAML Ain’t Markup Language)` is a human-readable markup style language often used for configuration files.

    ### github actions
    - gitHub Actions is one of the easiest CI/CD platforms to get started with, and you can use it to automate many tasks in your coding workflow. it runs any code that you specify whenever a GitHub event occurs, such as a push to a remote repository or a pull request.
    - to get started, you’ll need to already be tracking changes using Git, and you’ll need to have a remote repository hosted on GitHub
    - create a .github/ folder with a workflows/ folder within it. as with pre-commit hooks, GitHub Actions configurations are stored in a .yaml file. Create this in the workflows/ folder.
    - in this YAML file, you’ll specify the name of your workflow, the trigger for your workflow, and what you want to happen as a result of that trigger.
    - it’s important to note that whatever you run in the jobs section will run on GitHub’s servers, not your own computer.
    - next, you need to say what you want to happen in the steps section. since this job will run on GitHub’s servers, the first thing you need to do is copy your code to this server.
    - you need Python on your server, and there’s a prebuilt action for choosing a server that already has a Python installation.
    - the next step is to install the dependencies for your project. you can use a requirements.txt file

## cloud deployments
- ideally, you want your API to start up without needing any manual commands and automatically restart after a problem. To do this, you can use a Docker container.
- you’ll also need some kind of a host computer where you can run the code for your API.
- cloud providers such as Amazon Web Services (AWS), Microsoft Azure, and Google Cloud have become increasingly popular in recent years as places to host and run code, instead of on traditional servers.
- they provide on-demand computing resources that can scale up or down depending on how much they are being used.

    ### main steps to deployment for most cloud providers:
    1. create a docker container on the local machine that contains the API code and details of the libraries the code depends on.
    2. upload this container to a container registry on the chosen cloud profiler's system. the container registry can contan many containers.
    3. instruct the cloud provider to run the chosen container. this exposes the API code in the container to the internet so that users can access it. the container (and therefore the code) runs on the provider's server.

    ### containers and docker
    - a container is an isolated place to run the API or any other applications, and this means that the environment is reproducible (including libraries that the code depends on)
    - `Docker` - is a system for building and managing containers.
    - a `Docker` container is based on an image, and this provides instructions for building a container.
    - you can define a Docker image in a text file called a `Dockerfile`, and this file contains commands to install and set up everything you need in your container. You can then run an instance of a container locally or deploy it elsewhere.

    ### building a docker container