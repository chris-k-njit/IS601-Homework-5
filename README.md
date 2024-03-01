# IS 601 - Homework 5, Calculator Design Patterns
## Homework Objectives
### Continue to build off of Homework #4

1. Make my Calculator interactive with REPL and Command Pattern. - [x]
  * Integrate these new concepts into my existing program from Homework #4 to be able to add four basic commands: Add, Subtract, Multiply and Divide.
  * Added in square root, and other messages that users can receive.
  
2. (BONUS) Implement a Menu Command - [x]
  * Create a menu command that displays available commands from the command ditionary at the application's srtat and when the user types 'menu'. Do this to reinforce dynamic command integration.
  * Users can type 'help' to bring up the options available (i.e. menu).

3. Testing and Code Coverage - [x]
  * Once calculator commands are integrated, update and expand tests to achieve a full 100% coverage, to ensure this calculator's functionality is fully verified.
  * Almost hit 100% when looking at TOTAL under all tests after running pytest --pylint --cov

4. Plugin Architecture - [ ]
  * Now, refactor my program to automatically load plugins, making it easier to provide command additions without manual updates.

5. (BONUS) Explore Multiprocessing Capabilities - [ ]
  * See about adding multiprocessing features to enable commands/plugins to run on separate cores. This is to ensure application can be scalable and can ensure performance improvements in the future.