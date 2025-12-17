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
        self.startTime: int = round_data['score']
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

    def get_average_score(self) -> float:
        # Need an accumulator to calculate the average of the total score of all rounds
        total_score = 0
        for r in self.rounds:
            total_score = total_score + r.score
        average_score = total_score / len(self.rounds)
        return average_score

class Participant:
    # Initializing the statistics for the Participant data type.
    def __init__(self, participant_data: Dict[str, Any]) -> None:
        self.participantId: int = participant_data['participantId']
        self.name: str = participant_data['name']
        self.age: int = participant_data['age']

        self.sessions: list[Session] = []

    def get_participant_stats(self) -> Dict[str, Any]:
        return {} # Must implement later

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

    for participant in all_participants:
        stats = participant.get_participant_stats()
        final_output.append(stats)

if __name__ == "__main__":
    main()