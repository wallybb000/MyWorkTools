import subprocess
import sys

mainBranchName ="Main"
releaseBranchName ="19.XB000.PSPX9"
depotPrefix ="//depot/"
filePrefix ="C://"


class File:
    def __init__(self, input=""):
        arr = input.split('/') 
        self.fileName = arr[len(arr)-1]
        self.branchName = arr[4]    
        self.FileExName = self.fileName.split('.')[1]

        self.allPath = input
        self.workspaceFilePath = input.replace(filePrefix,depotPrefix)
        self.pathWithoutBranch = input[input.find(self.branchName)+len(self.branchName):len(input)] 
        #print input

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
    
    for a,b in matchArr:
        #print a.allPath ,b.allPath
        cmd = ["diff",a,b]
        subprocess.call(cmd)

