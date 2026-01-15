
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