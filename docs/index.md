# Title
**Dev:** *CWei*

**Date:** *05.31.2020*
## Introduction to Pickle module & Error Handling
Now that I have had opportunities to explore the basics of coding with Python on PyCharm, I will explore and explain my use of Python’s “pickle” module and use of error handling within my code. This will be a simple code based on this week’s Lab07-1 script to take a Customer and ID. To share exapmles of error handling and pickle, I will use parts of my [assignment07.py](https://github.com/cVarW/ITFnd100Mod07/blob/master/docs/Assignment07.py).

## Error Handling
Now that the core of my script is created (functions to handle the processing and input/output, I/O), I can now address how I could handle possible errors in my code.

### Try for Exception IOError
Error Handling is an especially useful assertion for any system that takes instructions. It only returns an error (i.e. wrong data types, syntactic errors) when the exception is true otherwise stays quiet in the script. Although the interpreter will catch and return information about these errors, Try/Except statements will keep the application running while returning to the UI why an error occurred and how not to trigger it again.
I will show how it works for ‘Add Customer’ block of code that checks if a file exists. Before I add the new customer to memory, the try statement will attempt to read the data file, ‘AppData.dat’. If this is the first instance of our application, the exception will catch this process and return an IOError then display “Remember to save your session.”

![Using try/except image01](https://user-images.githubusercontent.com/65147516/83363183-3e858080-a34c-11ea-9b6d-9dd3ab2ead9a.png "Using try/except image01")

This happens because the data file has not yet been created or is not located in the same folder as the Assigment07.py file. Because we used the Try/Except statement, I can keep the application running but am alerted that data does not exist in any form (data file or in RAM). The exception allows me to continue my session and add data & create the data file. As you can see with the figure 3, the UI will display an empty list if nothing was added by either UI inputs or from a file (since a file has yet to be generated).

![Exception occured image02](https://user-images.githubusercontent.com/65147516/83363194-4e9d6000-a34c-11ea-80a5-b73df8e84dc1.png "returns exception image02")

Creating a return in the except stated can also be added to the else statement. By including an else statement to the Try/Except, I can now control what will be displayed to the UI if the error was not triggered. Therefore, regardless if the data was from a file or from RAM, any customers (& the respective ID) will still be displayed if it exists in the customer list.
![exception passed else occured image03](https://user-images.githubusercontent.com/65147516/83366317-15241f00-a363-11ea-9134-9fb4f92bf880.png "pass eception return else image03")

## Pickle: Load and Dump
Speaking of reading data from the data file, I will share how I used the pickle module for my simple code.
Importing the pickle module is just like import a library for other languages. By including it in the first line of code after the script header, I can now save my database as binary data in the ‘AppData.dat’ file. Reading (and writing) a collection of data from (or to) a text file using pickle is easier and requires less code than the conventional write() function in python.

![marshalling data to file image04](https://user-images.githubusercontent.com/65147516/83363218-81475880-a34c-11ea-8f3b-b8d6263a4b97.png "writing binary data to file image04")

![data to list image05](https://user-images.githubusercontent.com/65147516/83363220-84dadf80-a34c-11ea-8bef-4385a86a8654.png "write data to list image05")

By pickling the data, I can access and manipulate any compilation of data without using loops to write to (or from) data files. After I retrieve and convert my binary data back to a list table, lstCustomer, I just use a two line for loop to display the data now saved in RAM. Now that I have tested my code a few times more, saved my data file created, saved as binary, then read back as my original list, I tried adding another ‘Happy’ customer to list of customers.

![list serialized to dat file image06](https://user-images.githubusercontent.com/65147516/83363231-9328fb80-a34c-11ea-96cc-b097dd1a6397.png "list wrote to dat image06")

![deserialized list image07](https://user-images.githubusercontent.com/65147516/83363234-9623ec00-a34c-11ea-90c2-221007654716.png "list loaded from pickle image07")

## What is the Purpose of Pickling?
Although pickling our data does not make it secure or invulnerable to cyber-attacks and may not be compatible with other programming languages, pickle offers convenience of shared data to be sent and retrieved between **safe channels** by marshalling (serializing) python objects (in this example, lists of dictionaries). 
As demonstrated in my included code, Assignment07.py, very few lines of code to read and write from files, hardly any complicated while or for loops to produce a streamlines UI experience. Additional information on python.org & Real Python gives more uses and examples of how to use pickle, advantages, functions, and other modules (similar to pickle) to use alongside or in lieu of the pickle module (ex, shelves, dill, and creating zip files for larger files).

## Summary
Python is really a great steppingstone for new coders as well as those with an immense coding repertoire. Utilizing the pickle module and incorporate error handling to my python script will just help me create a better UI experience. [Data camp](https://www.datacamp.com/community/tutorials/exception-handling-python) helped me with the correct syntax for error handling and I really loved the clarity of [Real Python](https://realpython.com/python-pickle-module/)’s explanation of pickling. In the book “Python for the absolute beginner” Pp.201-4, I was also introduced to the inclusion of the shelves module. However, for my sample script, shelves, zips and data security was not needed. Other sites that helped me understand the pickle module are listed below. Hope this has been a helpful sample of error handling & pickle for python.

## additional sites I recommend:
### Error Handling:
[tutorials point](https://www.tutorialspoint.com/python/python_exceptions.htm) https://www.tutorialspoint.com/python/python_exceptions.htm

### Pickle:
[Real Python:](https://realpython.com/python-pickle-module/) https://realpython.com/python-pickle-module/

[Python.org:](https://docs.python.org/3/library/pickle.html) https://docs.python.org/3/library/pickle.html

[Python Basics:](https://pythonbasics.org/pickle/) https://pythonbasics.org/pickle/

[data camp:](https://www.datacamp.com/community/tutorials/pickle-python-tutorial) https://www.datacamp.com/community/tutorials/pickle-python-tutorial

[geeks for geeks:](https://www.geeksforgeeks.org/pickle-python-object-serialization/) https://www.geeksforgeeks.org/pickle-python-object-serialization/

#### more detailed explanation fo the code found in [Assignment07.pdf](https://github.com/cVarW/ITFnd100Mod07/blob/master/docs/Assignment07.pdf)
