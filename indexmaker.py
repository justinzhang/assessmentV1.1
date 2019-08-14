import csv
import os

dirname= os.path.dirname(__file__)
filename=os.path.join(dirname, '\\templates\\index.html')
#---------------------------HTML LEGOS-------------------------------
htmlTop='''<!DOCTYPE html>
<html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
    <style>
    * {
      box-sizing: border-box;
    }
    
    body {
      background-color: #f1f1f1;
    }
    
    #regForm {
      background-color: #ffffff;
      margin: 100px auto;
      font-family: Raleway;
      padding: 40px;
      width: 70%;
      min-width: 300px;
    }
    
    h1 {
      text-align: center;  
    }
    
    input {
      padding: 10px;
      width: 100%;
      font-size: 17px;
      font-family: Raleway;
      border: 1px solid #aaaaaa;
    }
    
    /* Mark input boxes that gets an error on validation: */
    input.invalid {
      background-color: #ffdddd;
    }
    
    /* Hide all steps by default: */
    .tab {
      display: none;
    }
    
    button {
      background-color: #0192ff;
      color: #ffffff;
      border: none;
      padding: 10px 20px;
      font-size: 17px;
      font-family: Raleway;
      cursor: pointer;
    }
    
    button:hover {
      opacity: 0.8;
    }
    
    #prevBtn {
      background-color: #bbbbbb;
    }
    
    /* Make circles that indicate the steps of the form: */
    .step {
      height: 15px;
      width: 15px;
      margin: 0 2px;
      background-color: #bbbbbb;
      border: none;  
      border-radius: 50%;
      display: inline-block;
      opacity: 0.5;
    }
    
    .step.active {
      opacity: 1;
    }
    
    /* Mark the steps that are finished and valid: */
    .step.finish {
      background-color: #0192ff;
    }
    body{
    margin: 0px;
}
.outside{
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    padding: 50px;
    background-color: #C7C6C6;
}
.square{
    display: block;
    text-align: center;
    background-color: #FFFFFF;
    box-shadow: -1px 0px 14px 1px #454444;
    border-radius: 10px;
}
.square2{
    display: block;
    text-align: left;
    background-color: #FFFFFF;
    box-shadow: -1px 0px 14px 1px #454444;
    border-radius: 10px;
}
.section{
    padding-top: 20px;
}
.description{
    font-style: italic;
    padding: 10px;
    font-size: 13px;
}
.question{
    font-size: 13px;
}

label[for="form"]{
    text-align: left !important;
    font-size: 13px;
}
label[for="radio"]{
    padding-right: 15px;
    padding-left: 15px;
    font-size: 13px;
    font: 15px/1.7 'Open Sans', sans-serif;
     color: #333;
     -webkit-font-smoothing: antialiased;
     -moz-osx-font-smoothing: grayscale;
}
.form {
    border-radius: 5px;
    padding: 20px;
}
input[type=text], select {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}
input[type=submit] {
    width: 25%;
    background-color: rgb(105, 105, 105);
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
  
input[type=submit]:hover {
    background-color: #464646;
}

.form-radio
{
     -webkit-appearance: none;
     -moz-appearance: none;
     appearance: none;
     display: inline-block;
     position: relative;
     background-color: #f1f1f1;
     color: #666;
     top: 10px;
     height: 30px;
     width: 30px;
     border: 0;
     border-radius: 50px;
     cursor: pointer;     
     margin-right: 7px;
     outline: none;
}
.form-radio:checked::before
{
     position: absolute;
     font: 13px/1 'Open Sans', sans-serif;
     left: 11px;
     top: 7px;
     content: '\\02143';
     transform: rotate(40deg);
}
.form-radio:hover
{
     background-color: #f7f7f7;
}
.form-radio:checked
{
     background-color: #f1f1f1;
}
.radio{
    padding-bottom: 10px;
}
    </style>
    </head>
<body>



<div class="outside">
<form id="regForm" action="/results" method="post">
  <h1>Assessment:</h1>
  <!-- One "tab" for each step in the form: -->
  <div class="tab">Contact Info:
    <p><input placeholder="Input your Name" name="name"></p>
    <p><input placeholder="Input your Company Name"  name="company"></p>
    <p><input placeholder="Input your position at the Company" name="position"></p>
    <p><input placeholder=" Input your E-mail" name="email"></p>
  </div>
'''
categoryStart='''<div class="tab">CATEGORYNAME:
<p class="description">Rate your organization from 1 to 5, 1 being the least relevant and 5 being the most relevant, depending on the statement</p>
'''
categoryQuestion='''<p class="question">QUESTIONNAME</p>
                <div class="radio">
                <label for="radio"><input type="radio" name="QNAME" value=1 class="form-radio" id="q#a" >1</label>
                <label for="radio"><input type="radio" name="QNAME" value=2 class="form-radio" id="q#b">2</label>
                <label for="radio"><input type="radio" name="QNAME" value=3 class="form-radio" id="q#c">3</label>  
                <label for="radio"><input type="radio" name="QNAME" value=4 class="form-radio" id="q#d">4</label>
                <label for="radio"><input type="radio" name="QNAME" value=5 class="form-radio" id="q#e">5</label>
                    </div> '''
weightedQuestion='''<p class="question">QUESTIONNAME</p>
                <div class="radio">
                <label for="radio"><input type="radio" name="QNAME" value=1 class="form-radio" id="q#a" >1</label>
                <label for="radio"><input type="radio" name="QNAME" value=1 class="form-radio" id="q#b">2</label>
                <label for="radio"><input type="radio" name="QNAME" value=1 class="form-radio" id="q#c">3</label>  
                <label for="radio"><input type="radio" name="QNAME" value=5 class="form-radio" id="q#d">4</label>
                <label for="radio"><input type="radio" name="QNAME" value=5 class="form-radio" id="q#e">5</label>
                    </div> '''
categoryEnd='</div>'
htmlMiddle='''<div style="overflow:auto;">
<div style="float:right;">
  <button type="button" id="prevBtn" onclick="nextPrev(-1)">Previous</button>
  <button type="button" id="nextBtn" onclick="nextPrev(1)">Next</button>
</div>
</div>
<!-- Circles which indicates the steps of the form: -->
<div style="text-align:center;margin-top:40px;">'''
bubbles='<span class="step"></span> \n'
htmlBottom='''
</div>
</form>

<script>
var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
// This function will display the specified tab of the form...
var x = document.getElementsByClassName("tab");
x[n].style.display = "block";
//... and fix the Previous/Next buttons:
if (n == 0) {
document.getElementById("prevBtn").style.display = "none";
} else {
document.getElementById("prevBtn").style.display = "inline";
}
if (n == (x.length - 1)) {
document.getElementById("nextBtn").innerHTML = "Submit";
} else {
document.getElementById("nextBtn").innerHTML = "Next";
}
//... and run a function that will display the correct step indicator:
fixStepIndicator(n)
}

function nextPrev(n) {
// This function will figure out which tab to display
var x = document.getElementsByClassName("tab");
// Exit the function if any field in the current tab is invalid:
if (n == 1 && !validateForm()) return false;
// Hide the current tab:
x[currentTab].style.display = "none";
// Increase or decrease the current tab by 1:
currentTab = currentTab + n;
// if you have reached the end of the form...
if (currentTab >= x.length) {
// ... the form gets submitted:
document.getElementById("regForm").submit();
return false;
}
// Otherwise, display the correct tab:
showTab(currentTab);
}

function validateForm() {
// This function deals with validation of the form fields
var x, y, i, valid = true;
x = document.getElementsByClassName("tab");
y = x[currentTab].getElementsByTagName("input");
// A loop that checks every input field in the current tab:
for (i = 0; i < y.length; i++) {
// If a field is empty...
if (y[i].value == "") {
  // add an "invalid" class to the field:
  y[i].className += " invalid";
  // and set the current valid status to false
  valid = false;
}
}
// If the valid status is true, mark the step as finished and valid:
if (valid) {
document.getElementsByClassName("step")[currentTab].className += " finish";
}
return valid; // return the valid status
}

function fixStepIndicator(n) {
// This function removes the "active" class of all steps...
var i, x = document.getElementsByClassName("step");
for (i = 0; i < x.length; i++) {
x[i].className = x[i].className.replace(" active", "");
}
//... and adds the "active" class on the current step:
x[n].className += " active";
}
</script>

</body>
</html>'''



# ----------------CSV/DICTIONARY HELPER FUNCTIONS--------------------
def intoDict(filename): #compiles a dictionary with the values in the csv
    with open(filename, mode='r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        counter=0
        dictionary={}
        for row in csv_reader:
            dictionary[counter] = row
            counter +=1
        csv_file.close
        #print("here is dictionary \n")
        #print(dictionary) #0 is header, questions start at 1
        return dictionary
#HOW TO CONSTRUCT CSV SO THERE IS NO PROBLEM
        #1. CREATE A COPY OF THE TEMPLATE FILE FILE
        #2. KEEP HEADER THE SAME; ONLY EDIT ROWS 1 AND BEYOND

def databaseCreator(): #creates another csv that will track the results when ran through server testing
    writefile = 'masterdatabase.csv' #NOTE: this resets the entire database when there are changes
    header = ['name','email','company','position']
    questionNames= ultraFind('assessment.csv','name')
    for objects in questionNames:
        header.append(objects)
    with open(writefile, mode='w') as csv_File:
        w = csv.writer(csv_File)
        w.writerow(header)
    csv_File.close

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



#------------THE FUNCTION THAT MAKES THE SAUCE ROCK---------------
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
    

       
#--------HTML VARIABLE FUNCTIONS ----------



def howManyTabs(categoryDictionary): #returns amount of tabs based on the amount of categories
    howMany = len(categoryDictionary) + 1 #the one is the contacts tab
    tabs = bubbles * howMany
    return tabs

def categorySplit(category): #takes an individual category and returns the HTML start of the respective category.
    cat = categoryStart.replace('CATEGORYNAME',category)
    print('hey! you are in categorySplit! The category is ' + category)
    return cat

def questionHTML(ID,questionList,questionNameList,qNo,w): #takes the question number and returns an the question HTML which replaces QUESTIONNAME, QNAME, and #. Updated to include weighted question
    print('questionHTML is working with question' +str(qNo) + '!')
    if ID in w['y']: #If the id of the question is in the yes portion of the sorted dictionary, then we use the weighted question instead.
        print('ATTENTION! This question is weighted!')
        questionChange=weightedQuestion.replace('QUESTIONNAME',list(questionList)[ID-1]) 
        nameChange=questionChange.replace('QNAME',list(questionNameList)[ID-1])
        IDChange=nameChange.replace('#',str(qNo))
    else:
        questionChange=categoryQuestion.replace('QUESTIONNAME',list(questionList)[ID-1]) 
        nameChange=questionChange.replace('QNAME',list(questionNameList)[ID-1])
        IDChange=nameChange.replace('#',str(qNo))
    #print(IDChange)
    return IDChange

def engraveHTML(fileName,parsee):#we will use this to create an index
    file= open(fileName, mode='w')
    file.write(parsee)
    file.close








#----------ENDGAME FUNCTION----------
def bigBadBaddie(csv):
    categories = ultraFind(csv,'category')
    questions  = ultraFind(csv,'question')
    qName = ultraFind(csv,'name')
    weighted = ultraFind(csv,'weighted?')
    questionNumber=1
    HTML=htmlTop
    for eachCategory in categories:
        HTML += categorySplit(eachCategory)
        for eachQuestion in categories[eachCategory]:
            HTML += questionHTML(eachQuestion,questions,qName,questionNumber,weighted)
            questionNumber += 1
        HTML += categoryEnd
    HTML += htmlMiddle
    HTML += howManyTabs(categories)
    HTML += htmlBottom
    print(HTML)
    engraveHTML('templates\\index.html',HTML)#Need soultion on how to make this relative path
    databaseCreator()







bigBadBaddie('assessment.csv')

