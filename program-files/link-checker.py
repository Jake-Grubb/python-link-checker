# File: link-checker.py
# Programmer: Name:   Jacob Grubb
#             e-mail: jagrubb@siue.edu
# Runs with Python 2.7
# 
# Takes a list of webpage URL's and tests the links on every webpage,
# then prints any broken links back into a text file, using w3c's link checker
# Requires installation of:
#      W3C-LinkChecker
#           github: https://github.com/w3c/link-checker
#           git: https://github.com/w3c/link-checker.git

#Imports
import sys
import Queue
import subprocess
from subprocess import call

def main():
    #Open links
    links = Queue.Queue()
    try:
        print("\nAttempting to open file (links.txt): "),
        inFile = open('../data-files/links.txt', 'r')
        print("Success")
        for line in inFile:
            links.put(line)
        if (links.qsize() == 0):
            print("No links to check! Program complete!")
            sys.exit(1)
        inFile.close()
    except IOError:
        print("Failed")
        print("\nlinks.txt could not be opened successfully. \nCheck if file exists.")
        sys.exit(1)

    #Output data to text file
    try:
        print("Attempting to open file (output.txt): "),
        outFile = open('../data-files/output.txt', 'w')
        print("Success\n")
        outFile.close()
        counter = links.qsize()
        for x in range (0, counter):
            outFile = open('../data-files/output.txt', 'a')
            print("Testing file (" + str(x + 1) + "/" + str(counter) + "):"),
            outFile.write("Testing File (" + str(x + 1) + "/" + str(counter) + ")\n")
            outFile.write("_____________________\n")
            outFile.close()
            #write output here
            checkLink(links.get())
    except IOError:
        print("Failed\n")
        print("output.txt could not be opened successfully. \nCheck if file exists.")
        sys.exit(1)
    finally:
        outFile.close()

    print("\nProgram successfully completed!")

def checkLink(string url):
    #Check the url
    url = str(url).strip()
    print(str(url))
    outFile = open('../data-files/output.txt', 'a')
    outputText = subprocess.check_output(["checklink", "-b", "-q", str(url)])
    outputText = outputText.decode("utf-8")
    #Fix the output so it only catches 404 errors.
    
    outputText = str(outputText).splitlines()
    firstText = outputText.pop()
    if (firstText == "Error: 500 Access to 'file' URIs has been disabled"):
        print("Error code 500, program failed.")
        sys.exit(-1)
    print(firstText)
    outFile.write(str(outputText.pop()))
    outputText.pop()
    outputText.pop()
    outputText.pop()
    for x in range (0, (outputText.count("")/5)):
        outFile.write("\n")
        url = outputText.pop()
        #print("URL: " + str(url))
        line = outputText.pop()
        print ("Error Line: " + str(url))
        code = outputText.pop()
        print ("Code: " + str(code))
        if(code == "Code: 404 Not Found"):
            outFile.write(str(url))
            outFile.write(str(line))
            outFile.write(str(code))
            outFile.write("\n")
        outputText.pop()
    outFile.write("\n\n")
    outFile.close()
    return "Success"


main()