
# chapter eleven: APIs
- APIs (Application Programming Interfaces) are an important part of modern software engineering.
- APIs allow two systems to communicate and transfer data.
- they hide the details of your code behind a standard way of accessing a system, providing a useful layer of abstraction.
- many large software products use APIs to exchange data internally, and they’re particularly important in web development.
- an API lets you programmatically access some data or perform some  action. one of the first places you may come across an API is trying to download some data from a public API.
- they are an example of client and server communications. the server sits and waits for something to contact it, and the client is the one doing the contacting. the client requests some data from the server, and the server shares that data. web APIs generally use HTTP to make a request, then return a response as a JSON (JavaScript Object Notation) or XML file.

## calling an API
- the main types of API that you can encounter are `RESTful`, `SOAP`, and `GraphQl`. `SOAP` is an older API protocol that you'll see occasionallly, and `GraphQL` is a newer type that uses a query language to return data.
- `RESt (REpresentational State Transfer)` provides guidelines on how resources should be represented and manipulated using `HTTP` methods.

    ### `HTTP` methods and status codes
    - using `RESTful API`, you'll encounter a few standardized `HTTP` methods. each method correspods to a specific request you can make to the API to get a particular response.
    - each method corresponds to a specific request you can make to the API to get a particular response (endpoints):
        1. `GET` - retrieves some data
        2. `POST` - sends some data to create something and receive a response.
        3. `PUT` - sends data to update something that already exists.
        4. `DELETE` - deletes something that already exists.
    - one API may have a larger number of endpoints, for example, there can be many `GET` endpoints that return different types of data. some of them receive a parameter as input and return data that corresponds to this input, and some return the same data everytime.
    - when an API receives a HTTP request it returns a standard status code, depending on what happened. common codes:
        1. `2XX` - the request was succesful (eg, `200 "OK"`)
        2. `4XX` - client error. did something unexpected by the server eg, misspelling th endpoint path. this would give a `404 ("Not FOund")` response
        3. `5XX` - the server experienced an error. a bug occured in the API code when you made that request to it.
    - two other concepts: headers are metadata that are attached to an HTTP request to a server or a response from a server. common request headers include authorization credentials, and common response headers include the type of data that the server is returning,