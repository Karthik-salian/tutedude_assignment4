# tutedude_assignment4
### Task 2: Read File Content Line by Line  
This script reads the content of a text file and prints each line with its line number.  

- Tries to open a file named **`sample.txt`** in read mode.  
- If the file exists:  
  - Reads all lines using `readlines()`.  
  - Iterates through each line and prints it along with its line number.  
- If the file does not exist:  
  - Handles the **`FileNotFoundError`** gracefully and prints an error message.  

**Example:**  
Reading file content:
Line 1 : This is a sample text file.
Line 2 : It contains multiple lines.
