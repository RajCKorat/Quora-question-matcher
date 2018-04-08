# Quora-question-matcher











Solution Submission Template






















Name of the College/Institution: U. V. Patel College of Engineering (Ganpat University) 					         Kherva.
Student Name: Raj Korat
E-Mail ID: srchraj97@gmail.com
1.	Background
	Over 100 million people visit Quora every month, so it's no surprise that many people ask similarly worded questions. Multiple questions with the same intent can cause seekers to spend more time finding the best answer to their question, and make writers feel they need to answer multiple versions of the same question. Quora values canonical questions because they provide a better experience to active seekers and writers, and offer more value to both of these groups in the long term.
2.	Our Understanding
	Rather than above, at the time of saving same(meaning) questions in database repeatedly, it results in data duplicating and just waste of space. 
	So, we have to implement some solution for every question to stop it. For it we have to check questions with same keywords and find out the probability for being same of it.
3.	Scope
	Pair of questions is given as file and this Python code with nltk and panda libraries can find out probability of being same.
1)	Quora, Stackoverflow and other online discussion forms
2)	Search engine optimization 
3)	Chat bots etc...
4.	Out of Scope
1)	this (Java Keyword ) :- In code, I removed some common words like this but the is etc from questions. but in case of someone asking  questions regarding this keyword in java, it will not work sufficiently.
2)	Synonymous :- in case of synonymous, result will be affected(less probability than expected).
3)	Spell mistakes also effects on result.
5.	Assumptions
	General Assumptions
-	There are no spelling mistakes.
-	Test.csv and Python files are in same folder. 
	Technical Assumptions
-	There should be good computational resources.

6.	Solution Approach
	Machine learning Pipeline
1)	Removing Punctuations( like ?,-. And all characters)
2)	Tokenization
3)	Removing stop words(common words)
4)	Lemmatizing(to keep words in original form) – for more datails :- https://pythonprogramming.net/lemmatizing-nltk-tutorial/ 
	
7.	Implementation Framework
	Implemented steps as per below:	
1)	Removed Punctuations (like ?,-. And all characters)
2)	Convert question to Tokens
3)	Removed stop words(common words)
4)	Lemmatized tokens(to keep words in original form)

8.	Solution Submission
Share the link with the code uploaded on GitHub.
9.	References
-	https://www.lynda.com/Python-tutorials/NLP-Python-Machine-Learning-Essential-Training/622075-2.html
