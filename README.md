--------
A Python Trello API utility Script is to 
        create board,
        create list ,
        create cards to that list name
        Edit a card
        Add a new comment to the card
--------
You can use this script to :

1. Create Trello Boards

2. Create List

3. Create Trello Cards

4. Add a new comment to the Card

5. Edit the card 

6. Delete the card

You can refer to the Trello API page https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post for more details. I have used Python Request module to make the API calls.

------
Setup 
------
Add the Trello API Key and Token in authorization.py file


-------------------
Requirements
-------------------

Python 3.8
Add the Python Path to ENV variables
PyCharm IDE --> Set the Python interpretor user Python.exe path


---------------------------
COMMANDS FOR RUNNING SCRIPT
---------------------------

python trello_main.py


--------
ISSUES?
--------

a) If Python complains about an "Import" exception, please 'pip install requests'
