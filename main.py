def solve( I , list_of_list ):
    result = []
    for i in range(int(I)) :
        disct = {
            "road": "",
            "time": 0
        }
        for elem in list_of_list :
            if int(elem[1])  ==  i :
                if disct["time"] == 0  :
                    disct["road"] = elem[2]
                    disct["time"] = int(elem[3])
                elif disct["time"] > int(elem[3]) :
                    disct["road"] = elem[2]
                    disct["time"] = int(elem[3])
        result.append(disct["road"])
    return result


def process(fileName):


    #  Read the open file by name
    inputFile = open(inputFilesDirectory + fileName , "rt")

    #  Read file
    firstLine = inputFile.readline()


    list_of_list = []
    #  Assign parameters
    D, I , S, V, F  = list(map(str, firstLine.split()))

    for i in range(int(S)) :
        line_i = inputFile.readline()
        list_of_list.append(list(map(str, line_i.split())))
    list_of_list_2 = []
    for j in range(int(V)) :
        line_j = inputFile.readline()
        list_of_list_2.append(list(map(str, line_j.split())))

    result= solve(I ,list_of_list)



    outputFile = open(outputFilesDirectory + fileName + ".out", "w")
    outputFile.write(str(I) + "\n")
    for k in range(int(I)) :
        outputFile.write(str(k) + "\n")
        outputFile.write(str(1) + "\n")
        outputFile.write(result[k] + " " + D + "\n")

    outputFile.close()


inputFilesDirectory = "Input/"  # Location of input files
outputFilesDirectory = "Output/"  # Location of output files

fileNames = ["f.txt"]  # File names

for fileName in fileNames:  # Take each and every file and solve
    process(fileName)





