# Title
**Dev:** *CWei*
**Date:** *05.31.2020*
## Introduction to Pickle module & Error Handling
Now that I have had opportunities to explore the basics of coding with Python on PyCharm, I will explore and explain my use of Python’s “pickle” module and use of error handling within my code. This will be a simple code based on this week’s Lab07-1 script to take a Customer and ID

## Error Handling
Now that the core of my script is created (functions to handle the processing and input/output, I/O), I can now address how I could handle possible errors in my code.

### Try for Exception IOError
Error Handling is an especially useful assertion for any system that takes instructions. It only returns an error (i.e. wrong data types, syntactic errors) when the exception is true otherwise stays quiet in the script. Although the interpreter will catch and return information about these errors, Try/Except statements will keep the application running while returning to the UI why an error occurred and how not to trigger it again.
I will show how it works for ‘Add Customer’ block of code that checks if a file exists. Before I add the new customer to memory, the try statement will attempt to read the data file, ‘AppData.dat’. If this is the first instance of our application, the exception will catch this process and return an IOError then display “Remember to save your session.”
img01

## Summary
Placeholder, Loren ipsum
