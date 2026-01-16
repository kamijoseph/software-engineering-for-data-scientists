
# chapter thirteen: security
- the data you work with may include people’s personal data (which may be personally identifiable information, or PII). it could also include data that is important to your company’s business, such as financial data or data about how many customers your company has.
- this type of data can harm users and your company if it is exposed publicly.

## what is security
- security for software is concerned with protecting a system from theft of information, damage, disruption, or unwanted access to information.
- an attacker wishes to gain access to a system and use data within for some purpose that the holder of that data doesn’t want, or data is accidentally exposed in some way that it can be accessed by the public.
- security may be evaluated relative to external standards or to fulfill guarantees made to customers. Your company may comply with standards such as ISO 27001 or follow a framework from the US National Institute of Standards and Technology.

## security risks
- these are some examples of security risks that you should be aware of in your work as a data scientist. This is not an exhaustive list, but these are some of the risks you’re more likely to come across: 

    ### credentials, physical security and social engineering
    - this risk isn’t specific to Python or data science coding, but a common cause of security breaches is from an attacker getting access to an employee’s login credentials to company systems.
    -this can be done via an attack on physical security, for example, stealing company hardware, or via social engineering, for example, phishing emails.

    ### third party packages
    - the libraries that your code depends on may pose a security risk. When vulnerabilities are discovered, they are published in the MITRE online database of vulnerabilities. You can look up vulnerabilities in Python or vulnerabilities in older versions of NumPy.
    - library developers of active projects will work to fix them, then release a new version that does not have this vulnerability. it’s good practice to update all the packages your code depends on.

    ### the python pickle module
    - the pickle module allows you to save any form of data that you like. you may see it presented in ML examples as an easy way to save a model for later use. Unfortunately, the pickle module is not secure.
    - an attacker could plant any code in a pickle file and you wouldn’t know what it was until you unpickled. this could include Python code to delete files, for example.

    ### version control risks
    - committing to version control can pose a security risk. if you’re not careful, it’s possible to expose API keys and other credentials in public repositories.
    - committing data to a remote repository can also be a security risk. if your repository is public then anyone can see the data. and even if your repository is private, your company may not want data to be shared with GitHub.

    ### API security risks
    - if your API makes sensitive data available or you want to control who can use it, you should be aware of API security practices.
    - if the API is deployed on a cloud platform, anyone who has the URL can access the data from that API, so don’t use this for proprietary or sensitive data.
    - if your API gives access to a database, you need to be aware of SQL injection attacks andmake sure that you validate the inputs to your API.

## security practices
- there are a lot of ways that data can leak and your code’s security can be compromised.
- it’s impossible to completely eliminate threats because the code you’re working on is always changing and the code you depend on is also always changing.
- security practices aim to mitigate the threats and need to be updated often to keep up with new threats.

    ### security reviews and policies
    - if you are writing production code, you may be asked to take part in a threat modeling exercise or other security review. This is often carried out by a company’s security team, and it makes sure that security is considered early in the process of developing software.
    - the review’s aim is to consider potential threats to a system, what risks exist and how severe they are, and whether any actions need to be taken to address them.
    - the review process also ensures that a company’s security policy is applied, and it’s a chance for a development team to gather opinions from experts outside the team.

    ### secure coding tools
    - static code analysis or code scanning is an important technique for secure coding. this is where your code is checked against a list of rules but without actually running the code. static analysis encompasses linting and formatting but also includes checking for security issues.
    - tools for static analysis include SonarQube, Checkmarx, and many other commercial tools
    - code scanning tools are often included in a CI/CD workflow (see “deploying Code” for more details). They can be configured so that they allow code to be deployed only if it passes the security checks. Some code scanners also carry out linting and will check for patterns suggesting poor coding practices such as duplication.

    ### simple code scanning
    - you can use the CI/CD or bandit which is an open source cli code scanner for python that identifies vulnerabilities in the written code
    - bandit will scan all the lines of Python code in the files in the folder, and if you use the -r flag it will recursively scan the code in the subfolders as well. It will check your code against the rules in its database and alert you to any vulnerabilities it knows about.