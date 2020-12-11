import requests
from bs4 import BeautifulSoup

print("------------------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------------------------")


def resultFinder(nameLooker):
    result = requests.get("https://www.behindthename.com/name/"+nameLooker+"/rating")

    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    lookFor = "td"
    links = soup.find_all(lookFor)
    allJunk = []

    for i in links:
            allJunk.append([str(i.text)])
    
    temp2Dlist = [[] for i in range(14)]
    spotsAgain = 0
    switchAgain = 0

    for i in range(len(allJunk)):
        if ("%" in str(allJunk[i]) or "xa0" in str(allJunk[i])) and ("\\n" not in str(allJunk[i])):
            s = str(allJunk[i])
            s = s.replace('\\xa0','').replace("'","").replace("[",'').replace("]","")
            #print(s)
            temp2Dlist[spotsAgain].append(s)
            switchAgain += 1
            if switchAgain == 4:
                switchAgain = 0
                spotsAgain += 1

    if not temp2Dlist[0]:
        return("Unfortunatly, the popularity data for "+ nameLooker +" could not be found.")

    outPutCombine = "According to a popular vote, many people thought the name '" + nameLooker +"' was:"
    #print(outPutCombine)
    for i in range(len(temp2Dlist)):
        if (i == (0)):
            outPutCombine = outPutCombine + " " 
        elif(i == (len(temp2Dlist)-1)):
            outPutCombine = outPutCombine + ", and " 
        else:
            outPutCombine = outPutCombine + ", "

        if temp2Dlist[i][1] > temp2Dlist[i][2]:
            outPutCombine = outPutCombine + temp2Dlist[i][0]
        else:
            outPutCombine = outPutCombine + temp2Dlist[i][0]

        if i == (len(temp2Dlist)-1):
            outPutCombine = outPutCombine + "."

    
    
    return(outPutCombine)







print(resultFinder("John"))




# OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD 
"""
import requests
from bs4 import BeautifulSoup
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
searchedName = "frank"
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

result = requests.get("https://www.behindthename.com/name/"+searchedName+"/rating")
#print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
#print("------result.status_code")
#print(result.status_code)
#print("------result.headers")
#print(result.headers)
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")


src = result.content

soup = BeautifulSoup(src, 'lxml')


#print( soup)

lookFor = "td"
#print("------")
#print(lookFor)
#print("------")
links = soup.find_all(lookFor)
#print(links)

print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
allJunk = []

for i in links:
    #if "About" in link.text:
        allJunk.append([str(i.text)])
        #print("---")
        #print(link.attrs['href'])

#for i in allJunk:
    #print(allJunk[123])

#print(len(allJunk))

#for i in links:
    #print(str(allJunk[i]))
    #if "%" in str(i):
        #print(str(i.text))
    #elif "xa0" in str(i):
        #print("Yo")
    #if "%" in str(i.text):
        #print(i.text)

#print(allJunk)

temp2Dlist = [[] for i in range(14)]
spotsAgain = 0
switchAgain = 0

for i in range(len(allJunk)):
    #print(str(allJunk[i]))

    if ("%" in str(allJunk[i]) or "xa0" in str(allJunk[i])) and ("\\n" not in str(allJunk[i])):
        s = str(allJunk[i])
        s = s.replace('\\xa0','').replace("'","").replace("[",'').replace("]","")
        #print(s)
        temp2Dlist[spotsAgain].append(s)
        switchAgain += 1
        if switchAgain == 4:
            switchAgain = 0
            spotsAgain += 1
    #elif "xa0" in str(allJunk[i]):
        #s = str(allJunk[i])
        #print(s.replace('\\xa0','').replace("'","").replace("[",'').replace("]",""))

print(temp2Dlist) 

if not temp2Dlist[0]:
    print("Uh Oh")

print("_-_-_")
outPutCombine = "People thought the name '" + searchedName +"' was:"
print(outPutCombine)
for i in range(len(temp2Dlist)):
    if (i == (0)):
        outPutCombine = outPutCombine + " " 
    elif(i == (len(temp2Dlist)-1)):
        outPutCombine = outPutCombine + ", and " 
    else:
        outPutCombine = outPutCombine + ", "



    if temp2Dlist[i][1] > temp2Dlist[i][2]:
        outPutCombine = outPutCombine + temp2Dlist[i][0]
        #print(temp2Dlist[i][0])
    else:
        outPutCombine = outPutCombine + temp2Dlist[i][0]
        #print(temp2Dlist[i][3])

    if i == (len(temp2Dlist)-1):
        outPutCombine = outPutCombine + "."
'''
    if i == (len(temp2Dlist)-2):
        outPutCombine = outPutCombine + ", and" 
    else:
        outPutCombine = outPutCombine + ", "
'''

    
    

    #print(temp2Dlist[i])

print(outPutCombine)
print("------------------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------------------------")
"""

    




