import sys

def main():

    try:
        print("Multiple inputs using (,) as separators ")
        #inName = input("Enter Multiple Names: ")
        inName = "Test1, Test2, Test3"
        inName = inName.split(',')
        
        #inAddress = input("Enter Multiple Addresses: ")
        inAddress = "Bronx NY, New York NY, Queens NY" 
        inAddress = inAddress.split(',')
        
        #fname = input("Enter File Name(no need to add.txt): ")
        fname = "template"
        fname += ".txt"
        
    except:
        print("Enter correct inputs!")
    else:
        itr = 0
        while itr < len(inName):
            infile = openFile(fname)
            textProcessing(infile, inName[itr], inAddress[itr])
            itr += 1
            infile.close()
            
def openFile(fname):
    
    #Input and store string filename
    return open(fname,"r")


def textProcessing(infile,inName,inAddress):
    
    outfile  = open("outputTemplate_"+ inAddress+".txt",'w')
    
    #Modify and write to output.txt
    for line in infile:
        if line != '\n':
            #str.replace returns the original string if not matching string is found
            newString = line.replace("**INSERT NAME HERE**",inName)
            newString = newString.replace("**INSERT ADDRESS HERE**", inAddress)
            
            if newString != "":
                print(newString, file=outfile)

    outfile.close()

main()
