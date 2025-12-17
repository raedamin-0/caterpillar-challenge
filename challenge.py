""""
Flow In The Field Data Tracker App - Caterpillar Challenge Submission for Sandbox
"""
# Before implementing anything, we need to import our respective libraries.
from typing import Dict, Optional, Any # Typing hints to help with debugging
import requests # The library that will be used for GET and POST requests

# The url that I will be sending GET and POST requests to
url: str = "https://recruitment.sandboxnu.com/api/eyJkYXRhIjp7ImNoYWxsZW5nZSI6IkZsb3ciLCJlbWFpbCI6ImFtaW4ucmFlQG5vcnRoZWFzdGVybi5lZHUiLCJkdWVEYXRlIjoiMjAyNS0xMi0xOVQwNTowMDowMC4wMDBaIn0sImhhc2giOiJaRVZhLTBNMjBHQkxIV0cyb1lrIn0"

def get_data() -> Any:
    """
    Extracts all of the data from the url, including all session, round, and participant info.
    """
    # Getting and storing the data
    response: requests.Response = requests.get(url)

    # Checking if successful, and converting/formatting data to JSON
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 400:
        print("Error 400: Bad request")
    else:
        print(f"Error: {response.status_code}")
    return None

class Round:
    # Initializing the statistics for the Round data type.
    def __init__(self, round_data: Dict[str, Any]) -> None:
        self.roundId: int = round_data['roundId']
        self.sessionId: int = round_data['sessionId']
        self.score: int = round_data['score']
        self.startTime: int = round_data['startTime']
        self.endTime: int = round_data['endTime']

    def get_duration(self) -> int:
        return (self.endTime - self.startTime)

class Session:
    # Initializing the statistics for the Session data type.
    def __init__(self, session_data: Dict[str, Any]) -> None:
        self.participantId: int = session_data['participantId']
        self.sessionId: int = session_data['sessionId']
        self.language: str = session_data['language']
        self.startTime: int = session_data['startTime']
        self.endTime: int = session_data['endTime']

        self.rounds: list[Round] = []

    def get_duration(self) -> int:
        return (self.endTime - self.startTime)

    def get_session_score(self) -> int:
        # Need an accumulator to calculate the total score of all rounds
        session_score = 0
        for r in self.rounds:
            session_score += r.score
        return session_score

    def get_average_round_score(self) -> Optional[float]:
        # Need an accumulator to calculate the average of the total score of all rounds
        session_score = 0
        for r in self.rounds:
            session_score += r.score
        if len(self.rounds) == 0:
            return None # To catch a potential ZeroDivisionError
        else:
            average_round_score = session_score / len(self.rounds)
        return average_round_score

class Participant:
    # Initializing the statistics for the Participant data type.
    def __init__(self, participant_data: Dict[str, Any]) -> None:
        self.participantId: int = participant_data['participantId']
        self.name: str = participant_data['name']
        self.age: int = participant_data['age']

        self.sessions: list[Session] = []

    def get_average_total_round_score(self) -> Optional[float]:
        # For calculating the average total score
        total_score: int = 0
        total_rounds: int = 0
        for s in self.sessions:
            total_score += s.get_session_score()
            total_rounds += len(s.rounds)
        if total_rounds == 0:
            return None # To catch a potential ZeroDivisionError
        else:
            average_total_score = round(total_score / total_rounds, 2)
        return average_total_score

    def get_average_session_duration(self) -> Optional[float]:
        # For calculating the average session duration
        total_duration: int = 0
        for s in self.sessions:
            total_duration += s.get_duration()
        average_session_duration = round(total_duration / len(self.sessions), 2)
        return average_session_duration

    def get_languages(self) -> list[Dict[str, Any]]:
        languages: list[Dict[str, Any]] = []
        rounds_for_languages: Dict[str, Any] = {}
        
        for s in self.sessions:
            if s.language not in rounds_for_languages:
                rounds_for_languages[s.language] = []
            rounds_for_languages[s.language].extend(s.rounds) # Learned how to use .extend() instead of using another iterator here
        
        for language, rounds_list in rounds_for_languages.items(): # .items() to get both the key and values
            language_total_score = 0
            language_total_duration = 0
            for r in rounds_list:
                language_total_score += r.score
                language_total_duration += r.get_duration()
            language_average_score = round(language_total_score / len(rounds_list), 2)
            language_average_duration = round(language_total_duration / len(rounds_list), 2)
        
            language_dict: Dict[str, Any] = {
                "language": language,
                "averageScore": language_average_score,
                "averageRoundDuration": language_average_duration,
                "totalScore": language_total_score # Need this for sorting the languages
            }
            languages.append(language_dict)

        languages.sort(key=lambda x: x['totalScore'], reverse=True)
        return languages

    def get_participant_stats(self) -> Dict[str, Any]:
        if self.sessions == []:
            return {
            "id": self.participantId,
            "name": self.name,
            "languages": [],
            "averageRoundScore": "N/A",
            "averageSessionDuration": "N/A"
            }
        return {
            "id": self.participantId,
            "name": self.name,
            "languages": self.get_languages(),
            "averageRoundScore": self.get_average_total_round_score(),
            "averageSessionDuration": self.get_average_session_duration()
        }

def main() -> None:
    """
    The main function -- this where the program will actually start.
    """
    raw_data: Optional[Dict[str, Any]] = get_data()

    if raw_data is None:
        print("Failed to retrieve data.")
        return

    all_rounds: Dict[int, Round] = {} # Initializing a helper dictionary for rounds

    # The following loops are responsible for nesting the objects within each other, and to make all_participants a fully nested structure.
    # Loop for initializing an all_rounds dict to prepare for linking into session data
    for r in raw_data['rounds']:
        new_round = Round(r)
        all_rounds[new_round.roundId] = new_round

    all_sessions: Dict[int, Session] = {} # Initializing a helper dictionary for sessions

    # Loop for building an all_sessions dict as well as linking round data into session data
    for s in raw_data['sessions']:
        new_session = Session(s)

        round_ids = s['rounds']

        for round_id in round_ids:
            if round_id in all_rounds:
                selected_round = all_rounds[round_id]
                new_session.rounds.append(selected_round)

        all_sessions[new_session.sessionId] = new_session

    all_participants: list[Participant] = [] # Initializing a final list for participants

    # Loop for building an all_participants list as well as linking session data into participant data
    for p in raw_data['participantInfo']:
        new_participant = Participant(p)

        session_ids = p['sessions']

        for session_id in session_ids:
            if session_id in all_sessions:
                selected_session = all_sessions[session_id]
                new_participant.sessions.append(selected_session)

        all_participants.append(new_participant)

    final_output: list[Dict[str, Any]] = []

    # Loop for building the final array of participant stats
    for participant in all_participants:
        stats = participant.get_participant_stats()
        final_output.append(stats)

    final_output.sort(key=lambda x: x['name']) # Sorting it alphabetically by name

    post_response = requests.post(url, json=final_output) # POSTing the data!

    print(f"Status Code: {post_response.status_code}") # Two print statements to check the result of the POST
    print(f"Response: {post_response.text}")

if __name__ == "__main__":
    main()