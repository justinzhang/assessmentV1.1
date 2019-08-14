import csv
import smtplib
import flask
from flask import Flask, render_template,request, jsonify

#-------------CSV functions ported over--------
def csver(myDict):
	writefile = 'masterDatabase.csv'
	header = ['name', 'email', 'company', 'emailing', 'messaging', 'calendar', 'video', 'voice', 'secure', 'collab', 'mobile', 'access', 'remotely', 'fit', 'check', 'personalized', 'outside', 'onboarding', 'training', 'self-service', 'hardware', 'resources', 'security']
	with open(writefile, 'a', newline='\n') as csvFile:
		w = csv.writer(csvFile)
		w.writerow(myDict.values())

def intoDict(filename): #compiles a dictionary with the values in the csv
    with open(filename, mode='r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        counter=0
        dictionary={}
        for row in csv_reader:
            dictionary[counter] = row
            counter +=1
        return dictionary


def locator(dic,term):
    index=0
    for i in dic[0]: #looks through the header for the term
        if i == term:
            print(term + " has been found at " + str(index))
            break
        else:
            index += 1
    return index

def sort(dic,location): #sorts the items in the dic into a new one by location
    counter=0
    sortedDict = {}
    for j in dic:
        if dic[counter][location] not in sortedDict:
            sortedDict[dic[counter][location]] = [counter] #if list does not exist yet, create new list
        else:
            sortedDict[dic[counter][location]].append(counter) #else it appends on an existing one
        counter+=1
    return sortedDict


def ultraFind(filename,headerTerm):
    dictionary=intoDict(filename)
    location=locator(dictionary,headerTerm)
    print('---------this is the dictionary we are working with---------- \n')
    print(dictionary)
    sortedDict=sort(dictionary,location)
    del sortedDict[headerTerm] #deletes the header element in the dictionary
    print('\n ----------this is the dictionary sorted by the header term, ' + headerTerm + ':---------- \n')
    print(sortedDict)
    return sortedDict


#-----------FLASK APPLICATION---------------


#THIS IS THE APPLICATION OBJECT, ALLOWING USE OF APP
app = Flask(__name__)
app.config["DEBUG"] = True #DEBUGGER



#DECORATORS: THEY LINK FUNCTION TO A URL
@app.route('/')
def home():
    return 'Hello world! Perhaps you were looking for index' #returns hello world
@app.route('/index', methods = ['GET', 'POST'])
def index():
	return render_template('index.HTML')
	
@app.route('/results', methods = ['GET', 'POST'])
def results():
    
    if request.method == 'POST':
        result = request.form
        categories = ultraFind('assessment.csv','category')
        resultValues=list(result.values())[4:]
        index=0
        counter=0
        
        for res in resultValues:
            resultValues[counter] = int(res)
            counter+=1
        for category in categories:
            catLength=len(categories[category])
            percentify=100/(5*catLength)
            categories[category] = int(sum(resultValues[index:index+catLength])*percentify)
            index += catLength

        #categories['Communication'] = (int(result['emailing']) + int(result['messaging']) + int(result['calendar']) + int(result['video']) + int(result['voice'])) *4 #adds all the results up for COM and change it into percent
        #categories['Collaboration'] = (int(result['secure']) + int(result['collab']) + int(result['mobile']) + int(result['access']) + int(result['remotely'])) *4 #adds all the results up for COM
        #categories['Employment']    = (int(result['fit']) + int(result['check']) + int(result['personalized']) + int(result['outside']) + int(result['onboarding'])) *4  #adds all the results up for COM
        #categories['Investment']    = (int(result['training']) + int(result['self-service']) + int(result['hardware']) + int(result['resources']) + int(result['security'])) *4  #adds all the results up for COM
        csver(result)
        
    return render_template('results.HTML', categories = categories, result=result)#returns the results for HTML manipulation

app.run()
