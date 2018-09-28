
def main():

    #String to store filename
    fname = input("Enter File Name: ")

    #File variable that's set to read
    #infile = open(fname,"r")
    infile = open("allcaps.txt","r")
    
    #File varible that's set to write
    outfile = open("output.txt","w")

    #Read file and store it inside data
    #data = infile.read()

    #Print the data into a file with the filename that's been preset to
    #the object outfile
    #print(data.lower(),file=outfile)

    for line in infile:
        print(line[:-1],file=outfile)

main()
