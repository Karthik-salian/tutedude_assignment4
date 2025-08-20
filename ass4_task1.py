try:
    file1=open("sample.txt",'r')
    reading_file=file1.readlines()
    n=1
    print("Reading file content:")
    for line in reading_file:
        print("Line",n,":",line.strip())
        n=n+1
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")