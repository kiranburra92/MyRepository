# How to compile and Run Project 1

1.	Unzip the “.zip” folder
2.	Open Windows command prompt.
3.	Goto the location where the extracted folder  has been saved: 
			cd <path-extracted-folder>
4.	Goto -->  folder

cd Frequent_K+Itemsets_Mining

To Compile:

In windows command prompt: folder inside "Frequent_K+Itemsets_Mining": 
Type:		javac FrequentK_MiningDriver.java
•	“FrequentK_MiningDriver.java” is the Main Driver Class with the main () method inside it.
•	After the java code has been successfully compiled, the JAVA program must be executed.
•	If you get error: 'javac' is not recognized as an internal or external command, operable program or batch file, then refer to the following link:
https://www.youtube.com/watch?v=Uxlb-s-sxGU
To Run:
Option 1: To run from compiled code:
Path: 	Inside ‘src’ folder
Type:	java FrequentK_MiningDriver "[ <min sup>, <k>, <input file path>, <output file path>]"
Example: 	java FrequentK_MiningDriver 5 3 “transactionDB.txt” “Output.txt”

•	In the example given above, the Output File will be generated in the current folder.
•	Similarly, the Input File should be present in the current folder.
•	Provide fully qualified file path (absolute path)
•	The input file – “transactionDB.txt” should be in the current directory or in the “input file path” specified in the arguments list.
•	The output file "Output.txt" will be written to the current directory or to the “output file path” specified in the arguments list.


•	After the program has been successfully executed:
“Time taken in seconds: ____” will be printed in the windows command prompt.
  For example: Time taken in seconds: 524.
•	After successful execution of the FrequentK_MiningDriver.java program, Goto the “output file path” folder specified in the arguments list during execution.
•	“Output.txt” will be generated with all Frequent K + Itemsets appearing at least ‘min_sup’ number of times in the data.
Pre-requisite:
•	The Apriori Algorithm has been developed using JAVA 8. So, to execute the program, it requires Java to be installed in the system.
•	Make sure the Input File “transactionDB.txt” is present in the <input_file_path>. Otherwise, “java.io.FileNotFoundException: transactionDB.txt” will be thrown as error.
