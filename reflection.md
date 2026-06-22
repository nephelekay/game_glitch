# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What the game looked like the first time I ran it: 
  1. Numbers should be between 1 and 100, however the secret number was negative. This was an inconcistency that the user faced  when playing the game. It became visible when the user guessed positive numbers but the secret number ended up being negative.
  2. The hints to guesses are not accurate in the game. It was saying to guess lower even when the user guessed lower than the secret number. Therefore the hints where of no visible consequence to the secret number.
  3. When the player loses, they are prompted to click 'Start New Game'. However a new game does not start unless the player refreshes. Thankfully, 'Start New Game' works when the user has not yet ran out of guesses.

**Bug Reproduction Log**


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

- I utilized Chat GPT on this project. The specific model I used was GPT-5.5, the default when you search for chat gpt.
- When I struggled with running pytest, the LLM suggested that it may be to one of the folders not being declared as a package. It provided an explanation as to why my tests were running into errors and how the Python version I am currently using is limiting. This was expecially insightful as it was beyond the scope of my knowledge and I would not have been able to troubleshoot it on my own.
- AI suggested changes to the scoring system. Those changes would have simplified it and given greater insentive to try again without a large penalty for wrong guesses. However I chose to maintain the old scoring system with a few tweaks.

---

## 3. Debugging and testing your fixes

- To determine whether a bug was really fixed, I conducted pytest cases and tested the changes by acting as a user on the website. I was thus able to verify whether the bugs were fixed and gaauge the necessary adjustments.
- I revised the app.py file in order to adhere to the premises laid out on the side dashboard regarding each level (normal, easy, hard). Depending on the level, the number of attempts and range for the secret number guesses had to change. These changes were initially not reflected in the game, therefore I made sure to apply them. To test them, I conducted numerous trials of the different levels. This can be characterized as manual testing since a pytest did not oversee these changes.

- AI helped me to both design and understand my tests. I had not previously worked with pytest, therefore LLM was like a tutor for me taking me through it step by step. I learned about how to structure the tests, run them, and use them to evaluate my code.

---

## 4. What did you learn about Streamlit and state?

- Streamlit is like playing a video. Everytime the user interacts with it, pressing a button, the screen is cleared and the video starts to play start to finish. Before clearing the screen, state saves all the important information which is used when replaying the video. It is very usefull and allows a developer to make changes and easily see the outcome of his/her actions.

---

## 5. Looking ahead: your developer habits

- A strategy from this project that I would like to reuse in future labs or projects is picking up new skills and questioning why each change happens. Why do I need this specific command or dependencies for my code to work and to accomplish my objective? I want to keep asking myself these questions and gradually improve my understanding while growing as a developer. I wish to use LLMs as a tool to grow and not to replace my thinking and reasoning skills.

- The next time I work with AI on a coding task, one thing I would do differently is to comment my code better. That way when I am going back to working on it after a break, I will face less challenges.
- This project highlighted the ease with which AI  can come up with solutions to simple projects. I would like to see how it does with more complex issues. In the past when I tried to use it and inquire about bugs regarding more complex data structures, I had a lot of trouble with it. However this project was a breeze compared to those experiences. 