
import sys

def main():

    try:
        
        infile = openFile()
        lineLength = int(input("Enter Max Lenth: "))
        
    except:
        
        print("Enter valid filename!")
    else:
        
        textProcessing(infile,lineLength)
       #Print result to screen
       #printResults()

        
def openFile():
    
    #Input and store string filename
    fname = input("Enter File Name: ")
    return open(fname,"r")


def textProcessing(infile,lineLength):
    
    outfile  = open("output.txt",'w')
    
    #Modify and write to output.txt
    
    for line in infile:
        if ( line != '\n'):
            
            wrapText(line,outfile,lineLength)
            

def wrapText(line,outfile,lineLength):
    isDone = False

    #Keep wrapping all text to fit the lineLength
    while( not isDone ):

         #check if string is longer than Wrap length
        if len(line) >= lineLength:
            
            print(line[:lineLength],file=outfile)
            
            line = line[lineLength:]
            
            if(line == '\n'):
                isDone = True
         #outer else       
        else: 
            print(line,file=outfile)
            isDone = True

main()
