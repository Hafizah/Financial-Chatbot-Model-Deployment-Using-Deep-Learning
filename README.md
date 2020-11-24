![Title](https://github.com/Hafizah/Financial-Chatbot-Model-Deployment-Using-Deep-Learning/blob/main/result%20images/Title.png)

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
- Due to over 250 terms, the manual insertion of financial terms in the JSON format became tedious and prone to duplication. One way that I used to inspect duplication is to look at the probability of the selected words. Duplicated words usually have probability of about 50%. 
- Spelling mistakes while inserting terms. Aside from running spell checks, I manually checked for mistakes after deployment.
- Integrating all the files needed to deploy the model. I had to seperate 'punkt' into a seperate file instead of grouping together it with other libraries for a successful deployment.

**Methodology:**
1. Import all libraries used such as: Numpy, Tensorflow, JSON, NLTK.
2. Upload the intent of the project. Intent for this projet is written in JSON. It is a very useful format to store and transfer data from one place to another.
3. Next, stem all words using Lancaster Stemmer. For example, the word "roaster", "roasting", "roasted" are shortened to "roast". You can also use other stemmer such as Porter. The difference is how the words are stemmed. The word "stabil" remains the same after Porter however, stemmed to "stabl" in Lancaster! Another option is to do lemmatization. 
4. Then, texts were transformed into vectors used as input to train the ML model. Bag of words is a method that extract features from text documents. 
5. Use neural network to create model. Deep learning is used to ensure that the bot can carry other conversations. For example the bot can response to greeting, jokes etc, not only finance related facts.
6. Build user-response function using while loop to control responses. One very important condition to set is the probability of correct answers. The value chosen really depends on how good your model is set to learn. In this project, I dropped the probability from 0.9 to 0.75 to reduce the chances of the bot to make mistakes. I also added another condition where the bot will respond differently for probability less than 0.75.
7. Finally, design the frontend of the web app and deploy.

**Result - Bot Responses to questions:**

1. Response to facts.
<p align="center">
  <img width="780" height="550" src="https://github.com/Hafizah/Financial-Chatbot-Model-Deployment-Using-Deep-Learning/blob/main/result%20images/Facts.jpg">
</p>

2. Response to greetings and jokes.
<p align="center">
  <img width="780" height="600" src="https://github.com/Hafizah/Financial-Chatbot-Model-Deployment-Using-Deep-Learning/blob/main/result%20images/greeting%20and%20jokes.jpg">
</p>

3. Response to unrecognised words.
<p align="center">
  <img width="600" height="250" src="https://github.com/Hafizah/Financial-Chatbot-Model-Deployment-Using-Deep-Learning/blob/main/result%20images/Wrong%20words.jpg">
</p>

Thank you for checking out my repo! I'm currently working on updating this section with more in depth explanation. 
