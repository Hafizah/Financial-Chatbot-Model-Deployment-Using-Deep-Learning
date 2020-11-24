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
1. Due to over 250 terms, manual insertion of terms in the Json formated file became tedious and prone to duplication. One way that I used to inspect duplication is to look at the probability of the selected word. Duplicated words usually have probability of about 50%. 
2. Spelling mistakes while inserting terms. Aside from running spell checks, I manually checked for mistakes after deployment.

