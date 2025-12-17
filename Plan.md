-----------------------------------------------------------
12-15-2025, 5:34 PM

The application that I am being asked to build does not seem that far-fetched from the weather app I built previously. The only difference is that I am given a single URL to take data from and don't need to build one for each use case, and that I will have to POST the results back after the code is executed.

Time complexity is not a factor, so I don't have to worry too much about that. 

I will make this project in Python, since that is my most fluent language right now.

I will have to make use of the requests library to GET and POST the data.
-----------------------------------------------------------
12-15-2025, 6:02 PM

It seems like it won't be as similar to my weather app as I thought. I will probably have to make different constructs for each type of data (participant info, sessions, rounds). At least, this is what I am thinking of right now.
-----------------------------------------------------------
12-15-2025, 7:10 PM

I am completely sure that I have to create different constructs for each type of data now. However, I also feel like it might be a bit easier to also nest each data type within each other as to access the data much more easily at the end of all of this.

The data seems to follow a sort of hierarchy: Round->Session->Participant. So, for each higher hierarchal level class, it should probably contain a list of the lower level objects right below it, I think so at least. I will give this a try.
-----------------------------------------------------------
12-17-2025, 11:51 AM

Coming back off of a little break to avoid overworking myself. I realize that a big problem that has been recurring here is the organization of the entire code itself. I need to be making more use of the main() function clearly, and I don't think having a global raw_data variable would work for all of the classes. Maybe I should compartmentalize the data. 

Maybe I should also make another function for processing the data. I did something like that in my weather app I believe, through the display_weather() function. Helper functions might be useful here. 
-----------------------------------------------------------
12-17-2025, 12:34 PM

Now I started to expand upon the idea I had two days ago about nesting the classes within each other, under the nested structure all_participants. I was going to make all_participants a dictionary like I did for all_sessions and all_rounds, but maybe I shouldn't because I am going to have to post my solution as a JSON array anyways? Maybe I should store the participants in a list, without any keys linked (such as their participant IDs).

Ah, and it might be easier to sort a list alphabetically than a dictionary anyways, so maybe I should have it put in a list after all. 
-----------------------------------------------------------
12-17-2025, 12:43 PM

Yeah, now I get it. The purpose of having the all_rounds and all_sessions be dictionaries is just so the program can grab the items by ID quickly for linking them together. That is no longer necessary by the time we get to the all_participants list, since now the structure is essentially being packaged. It is fully nested by that point. 