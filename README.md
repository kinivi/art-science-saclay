# 🍎 Mx. Apple: GPT-3 powered Q\A personality 
This project intends to connect art&science into one idea. Idea of tighter connection between human and objects of everyday life
a simple bot that allows you to chat with various personas.

---

📰 Check [published article at Towards Data Science](https://towardsdatascience.com/art-science-with-gpt-3-persona-chatbot-5dbdd29a6229) for more! 

---

![apple](https://user-images.githubusercontent.com/13486777/162563320-45883d84-16d6-4ad7-a095-f812e1b93246.png)


## Web interface
🚩 You need key to access GPT-3 by OpenAI. Check [this website](https://openai.com/blog/openai-api/)

Install requirements:
`pip install -r requirements.txt`

Add the key: 

`export OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX`

Run Flask back-end: 

`python3 web.py -p apple`  

## Hardware
Our idead is that instead of keyaboard we used touches. Special conductive paint was painted onto apple and connected to the Arduino. Each point corresponds to the topics of question. Touch triggers serial port message which listened for at Web UI. That triggers question to chatbot and display the responce.  

<img src="https://user-images.githubusercontent.com/13486777/162563697-ffd8aacb-23ad-4962-816a-65c76e0e69f2.jpg" width="400">

---

## 🫡 Thanks 

Thanks to [gpt3-persona-bot](https://github.com/harperreed/gpt3-persona-bot) for the awesome example of creating personality in few steps with OpenaAI API
