# 🤖 Simple Python Chatbot — CodeAlpha Internship

This is a rule-based Python chatbot developed as part of the **CodeAlpha Python Programming Internship**.  
It reacts to greetings, emotions, jokes, motivation requests, time/date queries, and general small talk.

---

## ✨ Features

- Responds to greetings (`hi`, `hello`, `hey`)
- Gives emotional support (sad, bored, tired)
- Sends motivational quotes
- Tells jokes related to programming
- Provides current **time** and **date**
- Replies to questions about CodeAlpha
- Shows command list using `help`
- Graceful exit on `bye`, `exit`, or `quit`

---

## 🧠 How It Works

The chatbot uses **keyword-based response matching**.  
Incoming user text is analyzed through conditional checks, including:

- Greetings  
- Emotional keywords  
- Compliments  
- Time/date requests  
- Motivational keywords  
- Joke requests  
- Help commands  
- Closing commands  

If nothing matches, it returns a default fallback message.

Built using only:

- `random` — random responses  
- `datetime` — time and date  
- Basic Python logic  

No external libraries required.

---

## ▶️ How to Run

```
python chatbot.py
```

Start chatting:

```
You: hi
Bot: Hello! 👋
You: motivate me
Bot: Don’t stop until you’re proud 💪
You: joke
Bot: Why don’t programmers like nature? Too many bugs 😂
You: bye
```

---

## 📁 Project Info

- **Internship:** CodeAlpha – Python Programming  
- **Task:** Build a simple rule-based chatbot  
- **Developer:** Janakisetty Mukesh Babu
