Js Used:
->Dom manipulation.
->Event Handling.
->Dynamic Typing.
->Functional Programming.
->Cross-platform Support.
->OOP.
->prototypes.
->Asynchonous Programming.

Dom manipulation: 
    The Document Object Model (DOM) represents the structure of a web page. JavaScript can
    interact with the DOM to dynamically change the content, structure, and style of a webpage.
    document.getElementById("myElement").innerHTML = "Hello, World!";
Event Hangling:
    Event handling in JavaScript allows you to execute code in response to user interactions 
    like clicks, key presses, or mouse movements.

        Example:

        javascript
        Copy code
        document.getElementById("myButton").addEventListener("click", function() {
        alert("Button was clicked!");
        });
        This code attaches a click event listener to a button with the id
         myButton, which shows an alert when the button is clicked.
3. Dynamic Typing:
    JavaScript is dynamically typed, meaning you don't have to specify data types for variables.
    A variable's type is determined at runtime.
    
4. Functional Programming:
        JavaScript supports functional programming, a style of programming where you build programs using functions. Functions can be assigned to variables, 
        passed as arguments, and returned from other functions.

6. Object-Oriented Programming (OOP):
        JavaScript supports OOP, allowing you to create objects that contain both data and methods. 
        ES6 introduced the class syntax to make OOP more intuitive.

        Example:

        javascript
        Copy code
        class Person {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }

        greet() {
            console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
        }
        }

        const john = new Person("John", 30);
        john.greet(); // Outputs: Hello, my name is John and I am 30 years old.
Asynchronous operations:
        in JavaScript allow your code to perform tasks that may take some 
        time to complete (such as network requests, file reading/writing, or timers) 
        without blocking the execution of other code. This means that the JavaScript
        engine can continue to run other tasks while waiting for the asynchronous operation to finish, 
        leading to more efficient and responsive applications.

