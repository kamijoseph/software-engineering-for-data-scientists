
# chapter 3: using data structures effectively
- as a datascientist , you'll need to use a variety of data sctructures to store the data and its likely that some are appropriate for a certain problem  and others are less good choices.
- "...a large part of performant programming is knowing what questions you are trying to ask of your data, and picking a data structure that can answer those questions quickly."
- it’s important to use the correct data structure for the problem you’re working on for two main reasons: first, the data structure is optimized for that use case, and second, useful methods are associated with it.

## native python data structures
### 1. lists:
    - lists in Python are a type of array: a data structure that has some order. this means you can look up the first, third, or any other element of the list.
    - a python list is a dynamic array, and this means that it can resize if more elements are added. It can also store elements of different types, so, for example, a list could contain both strings and integers.
    - python allocates a continuous chunk of memory according to the size of the list, with one element of a list in the next door memory location to the next element. this has important implications: it’s very easy to look up an element in a list.
    - examples in notebook.ipynb
    - list look ups are O(1) complexity --> constant time
    - each time you add an element to a list it takes up extra space in memory. python allocates some extra space beyond the length of the original list, but once this space is full, the entire list needs to be copied into a new memory location with more consecutive space. appending at the end of a list is O(1) but with some overhead due to copying the list once the extra space is full.
    - if you insert something in the middle of a list, everything after that new element needs to move to a new memory location. So the insert operation is O(n). deleting an element from the middle of a list is also O(n). inserting and deleting are both O(n) because the list must always be in a continuous chunk of memory.
    - searching a list normally(from 1st value to the target) is O(n)  although there is efficient ways of doing that such as that of a binary search which is of O(log n) complexity

### 2. tuples:
    - tuples in python are also an array, but they have a static size. they are immutable once you’ve created a tuple, you can’t change it. you can’t append extra elements to the end of a tuple.
    - tuples are useful when you have only a few items you want to store in a data structure, and those items are not going to change. one thing to note is that a tuple is cached in the python runtime, rather than stored in memory, so it’s even faster to look up an element in a tuple than in a list. looking up an element in a tuple is O(1).

### 3. dictionaries:
    - dictionaries are based on key and value pairs, meaning that there are pairs of data elements that have some link between them, for example, the name of a person and their street adress.
    - they are powered by hash tables using a hash function to turn a key into the index for a list
    - a hash function maps strings or integers, whatever is in the dictionary key, to an integer that is the relevant index in the list of values.
    - the hash function must return the same integer every time it is applied to the same key. Keys in the dictionary also must be unique so that it’s possible to return the correct value. a dictionary key needs to be a hashable type such as a string, an integer, or a float. a python list can’t be hashed.
    - the hash table provides a useful feature: looking up the value corresponding to a particular key in a dictionary is O(1). you get the same performance as looking up an element in a list, but you don’t need to know the order in the list. Inserting, updating, and deleting a key and value pair are all O(1). items can be inserted in any order in the hash table.

### 4. sets:
    - a set is another data structure that is useful for data with no inherent order. sets are implemented in Python using a hash table, similar to dictionaries. however, instead of key and value pairs, they just have a set of unique keys. this means that all the elements in a set must be unique.
    - sets share the property with dictionaries that inserting, deleting, and updating items are all O(1). Looking up an element in a set is also O(1). converting a list to a set and then looking up the length is an efficient way to count the number of unique elements in a list.

## numpy arrays
- numpy is one of the most commonly used python liraries for data science, and this is because of its core data structure: the ndarray or n-dimensional array.

### a) numpy array functionalityand 
    - numPy arrays are n-dimensional arrays. best used wwhen the dataset is multidimensional.
    - one consideration with numPy arrays (as I’ll talk about much more in the next section) is that they can contain data of only one type. so they are not a valid choice if your data contains mixed types (for example, you need your data structure to contain both strings and integers).

### b) numpy arrays perfomance consideration
    - numPy uses types different from the standard Python types, which can also lead to some performance gains.
    - knowing that every element in a NumPy array is the same type leads to large performance gains, in particular for what’s known as vectorized calculations.
    - examples in notebook.ipynb
    - when using numpy arrays, you also need to consider whether you’ll need to add more elements to an array later. unlike a regular Python list, when numPy allocates space for an array, it doesn’t allow any extra room. so if you append more elements to a NumPy array the entire array needs to be moved to a new memory location every time.
    - therefore, appending to a numpy array is O(n) complexity.
    - it’s definitely worthwhile to initialize your array with the correct amount of space, and an easy way to do this is to use np.zeros like:

    ```python
    arr = np.zeros(1000)
    ```

    - you can then replace the zeros with a the new elements instead of appending to the array
    - you can also save alot of memory space by taking advantage of numpy's different types. numpy arrays are loaded into memory, so reducing their size may be helpful when you are dealing with large arrays.

### c) arrays in machin learning
    - data in ML is often stored in matrices (two-dimensional arrays) or tensors (higher-dimension arrays), whether that’s categorical, image, or text data.
    - frameworks for ML models, tensorFlow and pyTorch, offer optimized data structures for ML that take advantage of speedups gained by training on GPUs.
    - you can easily convert arrays for this framework such as:
    1. create np array:

        ```python
        np_tensor = np.random.rand(4, 4)
        ```

    2. convert for tensorflow

        ```python
        import tensorflow as tf
        tf_tensor = tf.convert_to_tensor(tensor_numpy)
        ```

    3. convert for pytorch

    ```python
    import torch
    pytorch_tensor = torch.from_numpy(np_tensor)
    ```

    - ML data structures are optimized for GPUs because these processors can run many tensor operations in parallel. Many ML algorithms are very easy to parallelize, including backpropagation in neural networks.
    - i also want to mention sparse matrices here. these are memory-efficient data structures for storing matrices that are mostly zeros. a common example of where these are useful is counting the frequency of different words in text data. for any given block of text, if the vocabulary you are using is large, most of the features are zeros.

## pandas dataframes
- pandas was originally built on top of numpy, therefore, many principles that apply to numpy arrays also apply to pandas dataframes, but there are features specific to pandas

    ### a) dataframe functionality
        - pandas has two key data structures: dataframes and series.
        - a dataframe is made up of one or more series.

        - a series is similar to a one dimensional numpy array, with key addition that it also has an index which lets you look up an item in a series ny its index as wll as its location
        - check example in notebook.ipynb
        - as with a numPy array, a series is created as a continuous block of memory. this means that some of the same performance considerations apply. for example, it’s slow to append new items to the end of a series because the whole structure must be moved to a new memory location.

        - a pandas dataframe  is a 2 dimensional arrangements of pandas series structures, with a column index as well.
        - unlike numPy arrays, each column within a DataFrame can be a different type. pandas also offers an object column type so that you can mix data of different types within a series. pandas also has more functions to handle missing data than numPy.
        - pandas data structures are particularly useful for two-dimensional tabular data with row and column information. they’re great for spreadsheet-style data as well. they can also be used similarly to database tables, giving you the option to join or query data, but this works best when your project is toosmall to be worth setting up a full database.
        - pandas also offers many specialized functions for working with time series.

    ### b) dataframe perfomance considerations
    - like numPy, the pandas library has many vectorized operations that apply calculations to all the elements in an array at once. many of these use numPy under the hood. if you’re doing something where a vectorized operation is available, this will almost always give you the best performance.
    - by default, a pandas DataFrame is loaded into memory. So if your DataFrame is larger than your computer’s memory, you have a problem.
    - it’s also difficult to estimate how much memory your data processing will take, so even if your DataFrame is smaller than your computer’s memory you might still have a problem.