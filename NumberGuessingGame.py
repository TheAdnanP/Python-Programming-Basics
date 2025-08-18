import random 
attempt = 0
secret = random.randint(1,20)
guess = 0
max_attempts = 5


while guess != secret:
    if attempt == 5:
        break
    
    attempt = attempt + 1
    guess = int(input(f"\nAttempts = {attempt}/{max_attempts} \nGuess the number: "))
    
    if guess < secret:
        print(f"Your guess is lower 📉")
    
    elif guess > secret:
        print(f"Your guess is higher 📈")
    
    else:
        print(f"You guessed it right 🤩🤩\nin {attempt} attempts")
    
if guess != secret:
    print(f"\nYour chance is over \nThe secret number was {secret}")
