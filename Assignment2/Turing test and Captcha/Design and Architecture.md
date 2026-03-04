# Turing Test
## So the basic idea i thought is:
A human judge talks to two participants.
One participant is a human.
The other participant is a computer (AI).
The judge does not know which one is which.
After conversation, the judge decides who is human.

## The Design could be like this:
1. Judge Interface – where judge types questions
2. Human Interface – where human participant replies
3. AI Program – computer program that generates answers
4. Message Controller – sends messages between judge and participants
5. Result Section – stores judge’s final answer

## The flow would be like this:
```
       Judge
         ↓
  Message Controller
   ↓            ↓
Human        AI Program
   ↓            ↓
  Message Controller
         ↓
       Judge 
```
## So how it works is:
Judge sends a question.

Message Controller sends question to both human and AI.

Human types response.

AI program generates response.

Responses are sent back to judge.

Judge decides who is human.

System saves the result.

---------------------------------------------------------------------------

# CAPTCHA

## For captcha design i thought of four objects:
- User (person visiting website)
- CAPTCHA Generator (creates challenge)
- Answer Checker (checks if correct)
- Database (stores correct answer)

```
            User
              ↓
        Website Server
              ↓
        CAPTCHA Generator
              ↓
      User solves challenge
              ↓
        Answer Checker
              ↓
Access Granted / Access Denied
```

## How It Works
- User opens website.
- Server creates CAPTCHA.
- CAPTCHA is shown to user.
- User enters answer.
- Server checks answer.
- If correct → access allowed.
- If wrong → try again.
