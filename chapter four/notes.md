
# chapter 4: object-oriented programming and functional programming
- object oriented programming and functional programming are paradigms based on underlying computer science principles.
- some programming languages support only one of them or strongly favors one over the other
- python supports both 

## 1. oject-oriented programming (OOP)
- in data science code some common objects could be a pandas dataframe, a numpy array, a matplotlib figure or a scikit-learn estimator.
- an object can hold data, it has some actions associated with it, and it can interact with other objects.
- you can also think about an object as a custom data structure. you design it to hold the data you want so that you can do something with it later.

    ### a) classes, methods and attributes

    1. class - a class defines an object, and you can think of it as a blueprint for making more objects of that variety. an individual object is an instance of that class, and each object is an individual “thing.”

    2. methods - thing that you can do to objects of that class. they define the behavior of that object and may modify its attributes.

    3. attributes - variables that are some property of that class, and each object can have different data stored in those attributes.

    - methods may take arguments, but attibutes cannot

    ### b) defining own classes
    - check code for exampless

    ### c) OOP principles
    
    1. inheritance
        - inheritance means that you can extend a class by creating another class that builds on it.
        - reduces repetition, because if you need a new class thats closely related to one you have already written, you dont need to duplicate that class to make a minor change
        - you may not need to use inheritance when defining your own classes, but you might need to use it with classes from an external library
        - check example in notebook.ipynb inheritance section
    
    2. encapsulation
        - encapsulation means that the class hides its detals from the outside
        - you can see only the interface to the class, never the internal details of whats going on.
        - the interface is made up of the methods and attributes that you design.

    3. abstractions
    - abstraction is closely linked to encapsulation. 
    - it means that you should deal with a class at the appropriate level of detail. 
    - so you might choose to keep the details of some calculation within a method, or you might allow it to be accessed through the interface.

    4. polymorphism
    - means you can have the same interface for different classes, which simplifies the code and reduces repetition.
    - two classes can have a method with the same name that produces similar result but the internal workings are different
    - the two classes can be parent and child or they can be unrelated.
    - scikit-learn contains a great example of polymorphism. every classifier has the same fit method to train the classifier on some data, even though it’s defined as a different class.