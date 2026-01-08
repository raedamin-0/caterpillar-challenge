# Flow In The Field - Caterpillar Challenge
This repository consists of all the project files I used in my submission for the Sandbox 2026 Caterpillar Challenge.

## How to run my solution
1.  **You should install this dependency first.**
    You will need Python installed and the `requests` library.
    ```
    bash
    pip install requests
    ```
2.  **Then run the script. Simple!**
    Navigate to the project directory and run the main file.
    ```
    bash
    python challenge.py
    ```

## My thought process
I approached this challenge as an ETL pipeline, similar to a weather app I previously built. Interestingly enough, I only learned about the existence of ETL pipelines through this problem after a quick search. It is an application where data is extracted from a source, transformed into a usable format, and then loaded or stored into a database.

Anyways, here is my general thought process summarized:

* **Hierarchy:** I noticed that the data followed somewhat of a  hierarchy (`Round` -> `Session` -> `Participant`). So, instead of keeping the data in lists, I decided to make classes for each level where the parent object holds a list of its children objects. So sessions hold a list of rounds, and participants hold a list of sessions.
* **Bottom-Up Linking:** I designed the `main()` function to process the data from the bottom up. I first instantiated all `Round` objects, stored them in a dictionary for quick lookup, and then linked them to `Session` objects. Finally, I linked `Session` objects to `Participant` objects. This must be done so I can allow the hierarchy I just talked about to exist. 
* **Decoupling:** I would not say this contributed much to the program's functionality, but to keep the code clean, I separated things like the calculation logic (like averages and durations) and the language list builder logic into specific helper methods within each class rather than calculating everything at once in the main loop. If I had done that instead, it probably would have been extremely messy and out of hand. 

## Some of the primary technical problems I had
* **Data Organization:** My initial approach relied on global variables at first, which caused scope issues and made the classes hard to manage. So then I decided that I had to refactor the code to pass specific data dictionaries into class constructors instead.
* **Output Formatting:** One of the more confusing parts for me here was whether to use dictionaries or lists for the final output. At first, I thought of using a dictionary for participants, but later I realized that a list was actually necessary due to the JSON array format that was being asked of me for the final output, as well as to implement the alphabetical sorting easily.
* **Scope & Indentation:** A little more minor of a problem for me, but I also faced some logic errors where some calculations were running inside the wrong loops; for example language stats were being calculated *before* all of the rounds were collected, which I fixed by adjusting the indentation and logic flow. I would say this was generally an organization issue that I managed to fix eventually.

## Approximate time it took you to complete this project
I would say that it took approximately **6 hours** to complete.
