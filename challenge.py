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

raw_data: Optional[Dict[str, Any]] = get_data()

class Participant:
    # Initializing the statistics for the Participant data type.
    def __init__(self) -> None:
        if raw_data is not None:
            self.participantId: int = raw_data['participantInfo']['participantId']
            self.name: str = raw_data['participantInfo']['name']
            self.age: int = raw_data['participantInfo']['age']
            self.sessions: list[int] = raw_data['participantInfo']['sessions']

class Session:
    # Initializing the statistics for the Session data type.
    def __init__(self) -> None:
        if raw_data is not None:
            self.participantId: int = raw_data['sessions']['participantId']
            self.sessionId: int = raw_data['sessions']['sessionId']
            self.language: str = raw_data['sessions']['language']
            self.rounds: list[int] = raw_data['sessions']['rounds']
            self.startTime: int = raw_data['sessions']['startTime']
            self.endTime: int = raw_data['sessions']['endTime']

class Round:
    # Initializing the statistics for the Round data type.
    def __init__(self) -> None:
        if raw_data is not None:
            self.roundId: int = raw_data['rounds']['roundId']
            self.sessionId: int = raw_data['rounds']['sessionId']
            self.score: int = raw_data['rounds']['score']
            self.startTime: int = raw_data['rounds']['score']
            self.endTime: int = raw_data['rounds']['endTime']

def main() -> None:
    """
    The main function -- this where the program will actually start.
    """
