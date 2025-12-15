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

    response: requests.Response = requests.get(url)

def main() -> None:
    """
    The main function -- this where the program will actually start.
    """