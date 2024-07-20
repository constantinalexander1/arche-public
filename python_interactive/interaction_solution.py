from typing import List

# AUFGABEN
# 1. SPEICHERE IM KONSTRUKTOR DIE PARAMETER IN DEN PASSENDEN VARIABLEN
# 2. SPEICHERE DIE STORYPOINTS IN EINER LISTE
# 3. GIBT DIE FRAGE EINES STORYPOINTS AUS
# 4. PRÜFE OB DER STORYPOINT EIN ENDPUNKT IST UND GIB DAS ERGEBNIS AUS
# 5. MACHE EINEN AUFRUF UM EINEN STORYPOINT AUSZUFÜHREN
# 6. IDENTIFIZIERE DEN NÄCHSTEN STORYPOINT
# 7. DENKE DIR SELBER EINE KURZE GESCHICHTE AUS UND ERSTELLE DIE NÖTIGEN STORYPOINTS

# FORTGESCHRITTENE AUFGABEN
# 8. SCHREIBE SELBST DIE get_story_point_by_id FUNKTION
# 9. VERSUCHE DEN TRY EXCEPT BLOCK ZU VERSTEHEN. WAS TUT ER UND WARUM IST ER NÜTZLICH?

class Option:
    option_description: str
    next_story_point_id: int

    def __init__(self, option_description: str, next_story_point_id: int):
        self.option_description = option_description
        self.next_story_point_id = next_story_point_id

class StoryPoint:
    id: int
    question: str
    options: List[Option]
    terminal: bool
    won: bool # only relevant if terminal is True

    def __init__(self, id: int, question: str, options: List[Option], terminal: bool, won: bool = False):
        # TASK 1: SPEICHERE IM KONSTRUKTOR DIE PARAMETER IN DEN PASSENDEN VARIABLEN
        # Du kannst mit "self.<Variable> = <Parameter>" die Parameter in den passenden Variablen speichern.
        # Tu dies für die Parameter id, question, options, terminal und won.
        # SOLUTION:
        self.id = id
        self.question = question # in case this is a terminal story point, the question will contain the result
        self.options = options
        self.terminal = terminal
        self.won = won


    def ask_question_let_user_choose_option_and_return_next_story_point_id(self):

        # TASK 3: GIB DIE FRAGE DES STORYPOINTS AUS
        # Du kannst etwas ausgeben mit der print()-Funktion.
        # Die Frage ist in der Variable self.question gespeichert.
        # SOLUTION:
        print(self.question)

        # TASK 4: PRÜFE OB DER STORYPOINT EIN ENDPUNKT IST UND GIB DAS ERGEBNIS AUS
        # Du kannst die Variable self.terminal verwenden, um zu prüfen, ob der Storypoint ein Endpunkt ist.
        # Mit "if <bool-Variable>:" kannst du prüfen, ob die Variable True ist.
        # Wenn der Storypoint ein Endpunkt ist, prüfe ob der Spieler gewonnen hat.
        # Du kannst die Variable self.won verwenden, um zu prüfen, ob der Spieler gewonnen hat.
        # Du kannst "if <bool-Variable>:"..."else:" verwenden, um zwischen zwei Fällen zu unterscheiden.
        # Wenn der Spieler gewonnen hat, gib "You won!" aus, ansonsten "You lost!".
        # Egal ob der Spieler gewonnen hat oder nicht, wenn der Storypoint ein Endpunkt ist, beende die Funktion mit "return None".
        # SOLUTION:
        if self.terminal:
            if self.won:
                print("You won!")
            else:
                print("You lost!")
            return None

        # print out the available options
        print("Choose between:")
        for i, option in enumerate(self.options):
            print(f"{i}: {option.option_description}")

        # get the user input and check if it is valid regarding inputting a number and if the number is in the range of the available options
        user_input = input()
        # TASK 9: VERSUCHE DEN TRY EXCEPT BLOCK ZU VERSTEHEN. WAS TUT ER UND WARUM IST ER NÜTZLICH?
        try:
            # try to convert the user input to an integer
            user_input = int(user_input)
        except ValueError:
            print("Invalid input. Please type a number. Try again!")
            return self.ask_question_let_user_choose_option_and_return_next_story_point_id()

        if user_input < 0 or user_input >= len(self.options):
            print("Invalid input. Please choose an available number. Try again!")
            return self.ask_question_let_user_choose_option_and_return_next_story_point_id()

        # return the next story point id
        return self.options[user_input].next_story_point_id

def get_story_point_by_id(story_points: List[StoryPoint], story_point_id: int):
    if len([story_point for story_point in story_points if story_point.id == story_point_id]) > 0:
        return [story_point for story_point in story_points if story_point.id == story_point_id][0]
    else:
        raise ValueError(f"Story point with id {story_point_id} not found.")

    # TASK 8: SCHREIBE SELBST DIE get_story_point_by_id FUNKTION
    # Kommentiere die bisherige Lösung aus und schreibe die Funktion selbst. (Die bisherige Lösung ist unnötig komplex und schwer nachvollziehbar.)
    # Du kannst durch die List der Storypoints durchgehen mit einer for-Schleife: "for story_point in story_points:"
    # In der Schleife kannst du mit "if ???" prüfen, ob die ID des Storypoints gleich der gesuchten ID ist.
    # Wenn ja, gib den Storypoint zurück.
    # Wenn du durch die Schleife durch bist und den Storypoint nicht gefunden hast, raise eine ValueError-Exception "raise ValueError(f"Story point with id {story_point_id} not found.")".
    # SOLUTION:
    # for story_point in story_points:
    #     if story_point.id == story_point_id:
    #         return story_point
    # raise ValueError(f"Story point with id {story_point_id} not found.")


def main():
    # define the story points, be careful to use an id only once!
    # TASK 7: DENKE DIR SELBER EINE KURZE GESCHICHTE AUS UND ERSTELLE DIE NÖTIGEN STORYPOINTS
    # Du kannst die bisher definierten Storypoints anpassen und als Vorlage für weitere Storypoints verwenden.
    starting_point = StoryPoint(id=1, question="You are standing at a crossroad. On the left you see 100 hungry lions waiting for human flesh. On the right you see your friends waiting to pick you up. What do you do?",
                                options=[Option("Go left", 2), Option("Go right", 3)], terminal=False)
    left = StoryPoint(id=2, question="You get eaten by the lions.", options=[], terminal=True, won=False)
    right = StoryPoint(id=3, question="You are picked up by your friends and go to a party. You have a great time.", options=[], terminal=True, won=True)

    # TASK 2: SPEICHERE DIE STORYPOINTS IN EINER LISTE
    # Du kannst um die Storypoints in einer Liste zu speichern "story_points = [<story_point_variable_1>, <story_point_variable_2>, ..., ...]" verwenden.
    # Stelle sicher, dass die Variable der Liste "story_points" heißt.
    # SOLUTION:
    story_points = [starting_point, left, right]

    # start a loop to go through the story points
    current_story_point = starting_point
    while current_story_point is not None:
        # TASK 5: MACHE EINEN AUFRUF UM EINEN STORYPOINT AUSZUFÜHREN
        # Du kannst von dem current_story_point die Funktion ask_question_let_user_choose_option_and_return_next_story_point_id() aufrufen, um den Storypoint auszuführen.
        # Die Funktion gibt die ID des nächsten Storypoints zurück.
        # Speichere die ID in einer Variable next_story_point_id.
        # SOLUTION:
        next_story_point_id = current_story_point.ask_question_let_user_choose_option_and_return_next_story_point_id()

        # if the returned next_story_point_id is not None, get the next story point
        if next_story_point_id is not None:
            # TASK 6: IDENTIFIZIERE DEN NÄCHSTEN STORYPOINT
            # Du kannst die Funktion get_story_point_by_id verwenden, um den nächsten Storypoint zu identifizieren.
            # Die Funktion erwartet zwei Parameter: die Liste der Storypoints und die ID des Storypoints.
            # Speichere den zurückgegebenen Storypoint in der Variable current_story_point.
            # SOLUTION:
            current_story_point = get_story_point_by_id(story_points, next_story_point_id)

        # if the returned next_story_point_id is None, the game is over, so set the current_story_point to None to end the loop
        else:
            current_story_point = None



if __name__ == "__main__":
    main()