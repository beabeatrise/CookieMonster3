import random
print("Welcome to rock paper scissors!")
WORDS= ("rock", "paper", "scissors")
user_turn= input(" Your turn: ")
computer_turn= random.choice(WORDS)
print("Computer turn: ", computer_turn)

"rock">"scissors"
"scissors">"paper"
"paper">"rock"

if user_turn == computer_turn:
 print("Draw")

elif user_turn > computer_turn:
 print("User wins!")

else:
  print("Computer wins!")