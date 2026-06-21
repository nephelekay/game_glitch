# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. Numbers should be between 1 and 100. The secret number was negative.
  2. Guesses are not accurate. It was saying to guess lower even when I guessed lower than the secret number
  3. When the player loses, they are prompted to click start new game. However a new game does not start unless the player refreshes. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input          | Expected Behavior    | Actual Behavior | Console Output / Error |
|----------------|----------------------|-----------------|------------------------|
|-50, 70, 90     |-Should instruct to go|-Instructs to go |-Inconsistent direction |
|                |lower                 |higher           |on whether to guess high|
|                |                      |                 |or low                  |
|-Prompts user   |-Secret number should |-Secret number is|-Secret number does not |
|to guess between|between 1 and 100     |negative         |adhere to constraints   |
|1 and 100       |                      |                 |                        | 
|-Prompts user to|-Game should reset and|-Clicking on 'New|-'New Game' does not    |
|start new game  |prompt user to make a |Game' has no     |work after user has lost|
|after loss      |new guess             |effect           |the game                |


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
