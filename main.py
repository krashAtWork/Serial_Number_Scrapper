# write the story of the application
# define the reg pattern that you want to search, as an input from the user and store it as a string.
# can we get reg patterns from the user, i believe not.
import os, re, pandas as pd, timeit, datetime, math



# rp = input("Input the regex pattern you wish to search in the following files")
rp = r'N\D{3}-\d{5}'
# rp =r'Lorem'
# rp = r'^N\D{3}'

startTime = datetime.datetime.now()
'''returns a list of all the files from a folder path'''
# find all the files in a particular folder - 2nd task
path = "./SerialNumberScrapper/My_Big_Directory"
def getAllFilesFromFolder(path):
    listFiles =[]
    info = os.walk(path, True)

    for root, dir, files in info:
        if len(files) !=0:
            # print(f'{root}{files}') # files is a list
            for f in files:
                # print(f'{root}/{f}')
                listFiles.append(f'{root}/{f}')

    return listFiles

'''If i give a file find if a certain pattern exists in it return a pandas dataframe, 
that tells me file name and the line number'''
def findDsnInfile(fileName, rp):
    # print(fileName)
    with open(fileName, 'r') as file:
        text = file.read()
        print(text)
    found = re.search(rp,text)
    
    
    if found:
        # lim = found.span()
        # dsn = text[lim[0]:lim[1]]
        
        # print(found.span())
        fileName = os.path.basename(fileName)
        # print(type(filename))
        return [fileName, found.group()]
    else:
        return []
    
'''call the findDsnInFile for each file in listFiles '''
def createResultData(listFiles):
    counter = 0 # o found
    result =  pd.DataFrame(columns=["FILE:", "Serial NO."   ])
    for file in listFiles:
        res = findDsnInfile(file, rp)
        if res !=[]:
            counter +=1
            result.loc[len(result)] = res
    print(result)
    print(f"Count : {counter} found")
    endtime = datetime.datetime.now()
    total_time = endtime - startTime
    print(f'Search duration: {math.ceil(total_time.seconds)} seconds')
    return result


    
listFiles = getAllFilesFromFolder(path)
createResultData(listFiles)



        
             

   



