import subprocess
import sys

mainBranchName ="main"
releaseBranchName ="18.XB000.PSPX8.OEM"
depotPrefix ="//depot/"
filePrefix ="C://"


class File:
    def __init__(self, input=""):
        arr = input.split('/') 
        self.workspaceFilePath = input.replace(filePrefix,depotPrefix)
        self.Name = arr[len(arr)-1]
        self.branchName = arr[4]    
        self.allPath = input[0:input.find(self.Name)] 
        self.pathWithoutBranch = input[input.find(self.branchName)+len(self.branchName):len(input)] 
        self.FileExName = self.Name.split('.')[1]

        #print self.pathWithoutBranch

def replaceStr(input= ""):
    splitPos = input.find("#")
    path = input[0:splitPos]
    return path


def readFile():
    if (len(sys.argv)!=2):
        return

    arr =[]

    fileName = sys.argv[1]
    for inputStr in open(fileName,'r'):
        m = File(replaceStr(inputStr))
        arr.append(m)
    return arr 

if __name__ == '__main__':
    arr = readFile()
    releaseFileArr = [m for m in arr if m.branchName == releaseBranchName]
    mainFileArr = [m for m in arr if m.branchName == mainBranchName]

    matchArr= [[a,b] for a in releaseFileArr for b in mainFileArr if a.pathWithoutBranch == b.pathWithoutBranch]
    



