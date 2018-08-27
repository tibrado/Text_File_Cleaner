import os

#VERSION = [
#    'Created by: Marketne Noel',
#    'Date Updated: 27 Aug 2018',
#    'Version 1.0'
#    ]

# class to read documnet and create temp files as txt also add changes to txt needed 
class FileCleaner(object):
    def __init__(self, in_file):
        self.msg = None

        #######################################################
        # change any doc to a text file and back 
        # change a text file to any doc 
        try:
            checkFile = open(in_file, 'r')
            checkFile.close()
            self.in_file_name = in_file
        except IOError:
            self.msg = "Unable to open file: " + in_file
        

    # print error messages
    def errors(self):
        return self.msg


    # make new line at input value default '.', return file name 
    def newLine(self, after = '.'):
        t = open('newline.txt', 'w')
        f = open(self.in_file_name, 'r')

        for line in f.read(): 
            for a in after:
                if line == a:
                    line = line.replace(a, a + '\n')
            t.write(line)

        f.close()
        t.close()

        return 'newline.txt'

    # Remove extra whitespace from text 
    def cleanWhiteSpace(self, fromFile = None, clean = ' '):
        t = open('whiteSpace.txt', 'w')

        if fromFile != None:
            f = open(fromFile, 'r')
        else:
            f = open(self.in_file_name, 'r')

        previous = '\n'

        for line in f.read(): 
            if line == clean  and (previous == clean or previous == '\n'):
                previous = line
                line = line.replace(line, '')
            elif line == '\n' and previous == '\n':
                previous = line 
                line = line.replace(line, '')
            else:
                previous = line 

            t.write(line)

        f.close()
        t.close()

        return 'whiteSpace.txt'

    # Change characters to, return file name 
    def changeTo(self, change = '\n', to = ' '):
        t = open('change.txt', 'w')
        f = open(self.in_file_name, 'r')
        i = 0
        tline = ''

        if len(change) == 1:
            for line in f.read(): 
                line = line.replace(change, to)
                t.write(line)
        elif len(change) > 1:
            for line in f.read(): 
                if change[i] == line:
                    tline += line
                    i+=1

                    if tline == change:
                        i = 0
                        tline = to
                else:
                    tline += line 
                    t.write(tline)

                    i = 0
                    tline = ''

            

        f.close()
        t.close()

        return 'change.txt'

    # split text file strings 
    def splitBy(self, what = ' '):
        f = open(self.in_file_name)
        text = f.read()
        f.close()

        return text.split(what)

    # make all alpha char lower case, return File name 
    def makeLowerCase(self):
        t = open('lowercase.txt', 'w')
        f = open(self.in_file_name, 'r')
        
        for line in f.read(): 
            if ord(line) >= 65 and ord(line) <= 90:
                line = chr(ord(line)+32)
            t.write(line)

        f.close()
        t.close()

        return 'lowercase.txt'    

    # make all alpha char Uper case, return File name 
    def makeUpperCase(self):
        t = open('uppercase.txt', 'w')
        f = open(self.in_file_name, 'r')
        
        for line in f.read(): 
            if ord(line) >= 97 and ord(line) <= 122:
                line = chr(ord(line)-32)
            t.write(line)

        f.close()
        t.close()

        return 'uppercase.txt'  
    
    # get word count, returns diction(word : number)
    def pairSimilar(self, what = 'chr'):
        matchDic = {}

        ## match characters 
        if what == 'chr':
            f = open(self.in_file_name, 'r')
        
            for line in f.read(): 
                if line in matchDic:
                    matchDic[line] += 1
                else:
                    matchDic[line] = 1
            f.close()
        elif what == 'word':
            t = open('stemp.txt', 'w')
            f = open(self.in_file_name, 'r')
        
            for line in f.read(): 
                if (ord(line) >= 65 and ord(line) <= 90) or (ord(line) >= 97 and ord(line) <= 122):
                    line = line
                else:
                    line = ' '

                t.write(line)

            f.close()
            t.close()
            
            t = open('stemp.txt', 'r')
            text = t.read()
            stext = text.split(' ')

            t.close()
            self.delFile('stemp.txt')

            for s in stext: 
                if s in matchDic:
                    matchDic[s] += 1
                else:
                    matchDic[s] = 1
        elif what == 'sentence':

            t = open('stemp.txt', 'w')
            f = open(self.in_file_name, 'r')
        
            for line in f.read(): 
                line = line.replace('!', '.')
                line = line.replace('?', '.')
                
                t.write(line)

            f.close()
            t.close()
            
            t = open('stemp.txt', 'r')
            text = t.read()
            stext = text.split('.')

            t.close()
            self.delFile('stemp.txt')

            for s in stext: 
                if s in matchDic:
                    matchDic[s] += 1
                else:
                    matchDic[s] = 1
        else:
            t = self.splitBy(what)
            for s in t: 
                if s in matchDic:
                    matchDic[s] += 1
                else:
                    matchDic[s] = 1

        return matchDic

    # key word search and return file name 
    def findKeys(self, keys, type = 'sentence' ):
        dictionary = self.pairSimilar(type)
        t = open('keysFound.txt', 'w')

        for sentence in dictionary:
            for key in keys:
                if(self.searchString(sentence, key)):
                    t.write(sentence)
                    t.write('.\n')

        t.close()
        a.cleanWhiteSpace('keysFound.txt')
        return 'keysFound.txt'

    # search string for a matching parttern function
    def searchString(self, stringToSearch, searchFor):
        i = 0

        for sts in stringToSearch:
            if sts == searchFor[i]:
                i += 1
            else: 
                i = 0
            if i == len(searchFor):
                return True
        return False
 
    # Update text file 
    def updateTxt(self, file):
        self.delFile(self.in_file_name)
        os.rename(file, self.in_file_name)
        self.delFile(file)

        return None

    # make a temp file 
    def makeFile(self, name):
        try:
            temp = open(name, 'w')
            temp.close() 
            return temp
        except:
            self.msg = 'Unable to make file ' + name
            return None

    # del a file 
    def delFile(self, name):
        try:
            os.remove(name)
            return True
        except:
            self.msg = 'Unable to dellete file ' + name
            return False

    # clean document 
    def clean(self):
        p = '.', '?', '!'
        self.updateTxt(self.newLine(p))
        self.updateTxt(self.cleanWhiteSpace())
        



