# tutedude_assignment4
### Task 2: Read File Content Line by Line  
This script reads the content of a text file and prints each line with its line number.  

- Tries to open a file named **sample.txt** in read mode.  
- If the file exists:  
  - Reads all lines using readlines().  
  - Iterates through each line and prints it along with its line number.  
- If the file does not exist:  
  - Handles the **FileNotFoundError** gracefully and prints an error message.  

**Example:**  
Reading file content:  
Line 1 : This is a sample text file.  
Line 2 : It contains multiple lines.

### Task 3: Write and Append to a File  
This script writes user input to a text file and then appends additional input. Finally, it displays the full content of the file.  

- Opens a file named **`output.txt`** in write mode (`'w'`).  
- Prompts the user to enter text and writes it to the file.  
- Prints a confirmation message after writing.  
- Prompts the user for additional text and appends it to the file.  
- Prints a confirmation message after appending.  
- Reads the final content of the file and displays it.  

**Example:**  

Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.
Enter additional text to append: Learning file handling in Python
Data successfully apended.
Final content of output.txt:
Hello, Python!
Learning file handling in Python
