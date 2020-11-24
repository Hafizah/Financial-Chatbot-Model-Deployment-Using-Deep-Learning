# Financial Chatbot using Deep Learning
**A chatbot** is an artificial intelligence program and a Human–computer Interaction model (*Bansal & Khan, 2018*). Simply, chatbot is a computer program that can hold a conversation with users (humans or another bots). In this project, the chatbot (Bela) uses Natural Language Processing, sentiment analysis and deep learning to communicate in human language. 

**Objective:** To create and deploy a financial chatbot that can define preset financial terminology. <br>
**Result:** RNN model with accuracy of 95% <br>
**Backend:** Python <br>
**Frontend:** HTML, CSS, BOOTSTRAP <br>
**Deployment:** Flask on Heroku <br>

**Steps taken:**
1. Built and stored over 250 financial terminology in JSON formated file.
2. Built model using deep learning (neural network).
3. Worked on frontend of the application.
4. Deployed model.

**Challenges:**
- Due to over 250 terms, manual insertion of terms in the Json formated file became tedious and prone to duplication. One way that I used to inspect duplication is to look at the probability of the selected word. Duplicated words usually have probability of about 50%. 
- Spelling mistakes while inserting terms. Aside from running spell checks, I manually checked for mistakes after deployment.

**Methodology**
1. Import all libraries used such as: Numpy, Tensorflow, JSON, NLTK.
2. Upload intent. Intent for this projet is written in JSON. It is a very useful format to store and transfer data from one place to another.
3. Next, all words were stemmed using Lancaster Stemmer. For example, the word "roaster", "roasting", "roasted" are shortened to "roast". You can also use other stemmer such as Porter. The difference is how the words are stemmed. The word "stabil" remains the same after Porter however, stemmed to "stabl" in Lancaster! Another option is to do lemmatization. 
4. Bag of words is a method that extract features from text documents. Then, texts were transformed into vectors used as input to train the ML model.
5. Use neural network to create model. I used deep learning so I can add non financial conversation such as greeting, jokes etc.
6. Build user response function using while loop to control responses. One very important condition to set is the probability of the correct answers. The number chosen really depends on how good your model set to learn. In this project, I dropped the probability from 0.9 to 0.75 to reduce the probability of the bot making mistakes. I also added another condition where the bot response differently for probability <0.75.
7. Lastly, work on the frontend of the web app and deploy.

**Frontend Visuals**

[chATBOT]('')
