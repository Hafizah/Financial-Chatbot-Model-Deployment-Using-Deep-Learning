![Title](https://github.com/Hafizah/Financial-Chatbot-Model-Deployment-Using-Deep-Learning/blob/main/result%20images/Title.png)

**A chatbot** is an artificial intelligence program and a Human–computer Interaction model (*Bansal & Khan, 2018*). Simply, a chatbot is a computer program that can hold a conversation with users (humans or another bots). In this project, the chatbot (Bela) uses Natural Language Processing, sentiment analysis and deep learning to communicate in human language. Since 2016, the popularity of chatbots has spiked  and the usage of the keyword "chatbot" and other related terms are highest in United States compared to other countries as seen in the figures below from [Scopus](https://www.scopus.com/home.uri). You can checkout the chatbot [here](https://bela-the-chatbot.herokuapp.com).

<p align="center">
  <img width="700" height="350" src="https://github.com/Hafizah/Financial-Chatbot-Model-Deployment-Using-Deep-Learning/blob/main/result%20images/Year_.jpg">
</p>


<p align="center">
  <img width="700" height="350" src="https://github.com/Hafizah/Financial-Chatbot-Model-Deployment-Using-Deep-Learning/blob/main/result%20images/Country_.jpg">
</p>

**Objective:** To create and deploy a financial chatbot that can define preset financial terminology. <br>
**Result:** RNN model with accuracy of 95%.<br>
**Backend:** Python. <br>
**Frontend:** HTML, CSS, BOOTSTRAP. <br>
**Deployment:** Flask, Heroku. <br>

**Steps taken:**
1. Built and stored over 250 financial terms and phrases using a JSON formated file
2. Built the model using deep learning (neural network)
3. Worked on frontend of the application 
4. Deployed the model using Heroku 

**Challenges:**
- Due to over 250 terms, the manual insertion of financial terms in text corpus was tedious and has a high tendency of term duplication. One way used to inspect duplication was to look at the probability of the selected words. Duplicated words usually have probability of about 50%. 
- Spelling mistakes while inserting terms. Manual review as well as spell checking software was used to find spelling mistakes.
- The chatbot would sometimes confuse terms with similar words. For example, "put warrant", "call warrant", "warrant". After several trials, by adding more styles of asking questions in "patterns" in text corpus, the chatbot was able to differentiate between these terms.
- The chatbot did not recognize the short form of terms. For example: CPI for "consumer price index". To halp mitigate this, I added common words that users would tend to use. Users are likely to type NASDAQ instead of "National Association of Securities Dealers Automated Quotations". 
- Integrating all of the files needed to deploy the model was combersome. I had to seperate 'punkt' into a seperate file instead of grouping it together with other libraries for successful deployment.

**Methodology:**
1. Import all libraries used: Numpy, Tensorflow, JSON, NLTK.
2. Upload the intent of the project. The intent for this projet was written in JSON. It is a very useful format to store and transfer data from one place to another.
3. Next, stem all words using Lancaster Stemmer. For example, the word "roaster", "roasting", "roasted" are shortened to "roast". You can also use other stemmer programs such as Porter. The difference is in how the words are stemmed. The word "stabil" remains the same after Porter however, is stemmed to "stabl" in Lancaster. (Another option is to do lemmatization) 
4. Then, texts were transformed into vectors and used as input to train the ML model. "Bag of words" is the method used to extract features from the text documents. 
5. Use a neural network to create model. Deep learning was used to ensure that the bot could carry other conversations. For example, the bot can respond to greetings, jokes etc, not only finance related facts.
6. Built a user-response function using a while loop to control responses. One very important condition to set was the probability of correct answers. The value to choose really depends on how good your model is set to learn. In this project, I dropped the probability from 0.9 to 0.75 to reduce the chances of the bot making mistakes. I also added another condition for the bot to respond differently when the probability is less than 0.75.
7. Designed the frontend of the web app
8. Finally, deployed the chatbot using Heroku.

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

Thank you for checking out my repo! I'm currently working on updating this section with more in depth explanations. 
