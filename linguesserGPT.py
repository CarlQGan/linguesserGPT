import argparse
import random
import sys
from gpt_bridge import GPTBridger

"""
--------------
Helper methods
--------------
"""

def __read_languages(languages_path):
    with open(languages_path, 'r') as file:
        languages = file.readlines()

    # strip newline characters and remove empty lines
    languages = [line.strip() for line in languages if line.strip() != '']

    return languages

languages_file_path = "./languages.txt"  # file path to the languages list file
LANGUAGES = __read_languages(languages_file_path)


"""
The main class for LinguesserGPT.
"""
class LinguesserGPT:
    def __init__(self, api_key : str = None, default_points : int = 1, default_attempts : int = 3) -> None:
        self.api_key = api_key
        self.bridger = GPTBridger(api_key)
        self.languages = LANGUAGES
        self.num_languages = len(self.languages)
        self.current_language = None
        self.current_attempts = 0
        self.previous_languages = []
        self.recognized_languages = []
        self.default_points = default_points
        self.default_attempts = default_attempts
        self.total_attempts = 0
        self.total_score = 0

    def is_correct(self, language : str, guess : str) -> bool:
        return guess.lower().strip() == language.lower().strip()

    def get_random_language(self) -> str:
        return random.choice(self.languages)
    
    def get_random_language_example(self) -> str:
        curr_lang = self.get_random_language()
        self.set_current_language(curr_lang)
        return self.bridger.get_next_language_example(curr_lang)
    
    def get_same_language_example(self) -> str:
        if self.get_current_language() is None:
            raise ValueError("No language selected.")
        return self.bridger.get_same_language_example()
    
    def get_current_language(self) -> str:
        return self.current_language
    
    def set_current_language(self, language : str) -> None:
        self.current_language = language

    def append_previous_language(self, language : str) -> None:
        self.previous_languages.append(language)

    def get_total_attempts(self) -> int:
        return self.total_attempts
    
    def add_total_attempts(self, num_attempts : int = 1) -> None:
        self.total_attempts += num_attempts
    
    def get_current_attempts(self) -> int:
        return self.current_attempts

    def add_current_attempts(self, num_attempts : int = 1) -> None:
        self.current_attempts += num_attempts
    
    def get_total_score(self) -> int:
        return self.total_score
    
    def get_recognized_languages(self) -> list:
        return self.recognized_languages
    
    def add_recognized_language(self, language : str) -> None:
        self.recognized_languages.append(language)

    def is_game_over(self) -> bool:
        return self.current_attempts >= self.default_attempts
    
    def reset_game(self) -> None:
        self.current_attempts = 0
        self.previous_languages = []
        self.recognized_languages = []
        self.total_attempts = 0
        self.total_score = 0
        self.current_language = None
        self.bridger = GPTBridger(self.api_key)
        self.set_current_language(self.get_random_language())
        example = self.bridger.get_next_language_example(self.get_current_language())
        print("Game reset! The example sentence is: {}".format(example))

    def next_round(self) -> None:
        self.current_attempts = 0
        self.append_previous_language(self.get_current_language())
        self.set_current_language(self.get_random_language())
        example = self.bridger.get_next_language_example(self.get_current_language())
        print("Next round! The example sentence is: {}".format(example))

            
def main(args):
    linguesser = LinguesserGPT(args.api_key, args.default_points, args.default_attempts)
    
    def check_answer(user_guess):
        if linguesser.is_correct(linguesser.get_current_language(), user_guess):
            print("Correct!")
            linguesser.add_recognized_language(linguesser.get_current_language())
            linguesser.total_score += linguesser.default_points
            linguesser.add_total_attempts()
            linguesser.next_round()
        else:
            print("Incorrect!")
            linguesser.add_current_attempts()
            linguesser.add_total_attempts()
    
    print("Welcome to LinguesserGPT!")
    print("You will be given a language and an example sentence in that language.")
    print("You will have to guess the language.")
    print("You will have {} attempts for each language.".format(args.default_attempts))
    print("You will get {} points for each correct guess.".format(args.default_points))
    print("You can type 'quit' to quit the game.")
    print("You can type 'skip' to skip the current language.")
    print("You can type 'same' to get another example sentence in the current language.")
    print("You can type 'score' to get your current score.")
    print("You can type 'attempts' to get your current attempts.")
    print("You can type 'recognized' to get the list of recognized languages.")
    print("You can type 'reset' to reset the game.")
    
    input("Press Enter to continue...")
    linguesser.set_current_language(linguesser.get_random_language())
    example = linguesser.bridger.get_next_language_example(linguesser.get_current_language())
    print("The example sentence is: {}".format(example))

    while not linguesser.is_game_over():
        user_input = input("Please guess the language: ")
        if user_input.lower().strip() == "quit":
            sys.exit()
        elif user_input.lower().strip() == "skip":
            linguesser.next_round()
            linguesser.add_total_attempts(linguesser.get_current_attempts())
        elif user_input.lower().strip() == "same":
            linguesser.add_total_attempts()
            example = linguesser.get_same_language_example()
            print("The example sentence is: {}".format(example))
        elif user_input.lower().strip() == "score":
            print("Your current score is: {}".format(linguesser.get_total_score()))
        elif user_input.lower().strip() == "attempts":
            print("Your current attempts is: {}".format(linguesser.get_total_attempts()))
        elif user_input.lower().strip() == "recognized":
            print("Your recognized languages are: {}".format(linguesser.get_recognized_languages()))
        elif user_input.lower().strip() == "reset":
            linguesser.reset_game()
        else:
            check_answer(user_input)
    
    print("Game over! Your total score is: {}".format(linguesser.get_total_score()))
    print("Your recognized languages are: {}".format(linguesser.get_recognized_languages()))
    print("Your total attempts is: {}".format(linguesser.get_total_attempts()))
    print("Thanks for playing LinguesserGPT!")
    print("Please give this repo a star if you like it!")
    print("Please report any issues to the Github repo, thanks!")
    print("See you next time!")
    sys.exit()
            


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LinguesserGPT - a language guessing game using GPT model.")
    parser.add_argument("--api_key", type=str, default=None, help="OpenAI API Key.")
    parser.add_argument("--default_points", type=int, default=1, help="Default points for each correct guess.")
    parser.add_argument("--default_attempts", type=int, default=3, help="Default attempts for each language.")

    args = parser.parse_args()
    main(args)
