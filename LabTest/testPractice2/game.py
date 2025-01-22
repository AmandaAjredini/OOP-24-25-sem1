import random

class Player(object):

   def __init__(self):
       print('Creating new player...')
       print('Hello! What is your name?')
       name = input()
       print('What is your country?')
       country = input()

       self.name = name
       self.country = country
       self.__highest_score = 100

   def __str__(self):
       return "{} from {}".format(self.name, self.country)

   def set_highest_score(self, score):
       if score < self.__highest_score:
           self.__highest_score = score

   def get_highest_score(self):
       return self.__highest_score

class Game(object):
   def __init__(self, high_num, player):
       self.high_num = high_num  # the highest possible number that can be chosen
       self.player = player  # the user's name
       self.guessesTaken = 0  # the initial number of guesses taken
       self.number = random.randint(1, self.high_num)  # the number the computer chooses
       self.guess = None  # the user's guess

   def play(self):
       print('Well, {},  I am thinking of a number between 1 and {}.'
             .format(str(self.player.name), self.high_num))
       while self.guessesTaken < 6:
           if not self.get_guess():
               continue
           # else: self.guess gets changed in get_guess function

           self.guessesTaken += 1

           if self.guess < self.number:
               print('Your guess is too low.')

           if self.guess > self.number:
               print('Your guess is too high.')

           if self.guess == self.number:
               break

       if self.guess == self.number:
           self.player.set_highest_score(self.guessesTaken)
           print('Good job, {}! You guessed my number in {} guesses! Your highest score is {} guesses'
                 .format(self.player.name, self.guessesTaken, self.player.get_highest_score()))
       else:
           print('Nope. The number I was thinking of was', self.number)

   def get_guess(self):
       print('Take a guess.')
       try:
           self.guess = int(input())
       except ValueError:
           print('Not a valid guess.')
           return False

       return True




def main():
    player = Player()

    while True:
        print('Type 1 for easy or 2 for difficult guessing game. Type q to quit.')
        user_choice = input()

        if user_choice.lower().startswith('q'):
            print("Goodbye!")
            return

        while True:
            try:
                user_choice = int(user_choice)
                if user_choice not in [1, 2]:
                    continue
                break
            except ValueError:
                continue

        if user_choice == 1:
            # make easy game
            easy_game = Game(20, player)
            # play easy game
            easy_game.play()

        elif user_choice == 2:
            # make difficult game
            diff_game = Game(30, player)
            # play difficult game
            diff_game.play()

        print("\nThank you for playing!")



main()
