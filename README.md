## WIP : I'm currently working on adapting the work made for the company
## to a more general usage. The README is therefore not entirely up-to-date.
These files were developped by Victor Nepveu [nepveu.victor@imt-atlantique.net] for Xelya.


They implement Word2Vec algorithms, and especially apply it to support tickets, numerous
at Xelya. The point is, for a given ticket, to find the closest ticket that has already been 
solved, and send the client the solution used for this ancient ticket, so that the client 
doesn't remain helpless if the client relation doesn't contact them back quickly.

## Folder's content :

`/obj/ :`
Contains objects generated by the different steps of the algorithm.
Any file you want to use should at least be in this folder
The subfolders of this folder are pretty self-explanatory as to what
they contain.

`File ending in .py :`
A brief description of the purpose of the file can be found in the first lines of each.

`ticket_with_unique_id_without_date.csv :`
CSV file extracted from Xelya's ORM, that contains all demands  (as of 10/07/18).
A lot of the tickets (about a third) in there contain either gibberish, empty or useless content.
It is about 350,000 lines long, with around 240,000 useful lines.

`requirement.txt :` 
Result of the "pip freeze" command, shows the required modules to run the different programs
in this folder. A simple "pip install --user -r requirements.txt" should be enough.


## Running the different apps :

Only the "main" and "app" files are supposed to be ran as standalone programs.

The main files should be ran in this order : 

`1. main_csv_to_pickle :` this will generate a pickle file that contains the content of
the aforementioned CSV file

`2. main_text_treatment :` this will make the text go through standard text-processing in the NLP
field : tokenization (ie separating a sentence into words) and numerics removal are some 
of the realized operations

`3. main_model :` generate a Word2Vec model based on the corpus of tickets, and save it

`4. main_vectorization :` for each ticket, use the Word2Vec model to compute the vector 
corresponding to the text of the ticket, and save it

`5. main_document_similarity :` takes a list of tickets in input, and for each ticket, find
the semantically closest ticket from the whole pool of tickets 

The app files require the main files to have been ran at least once, and there needs to be
configuration as to which data the applications should be dealing with. The configuration lies
in the filename used within the "load" functions


## TODOs :

- [ ] Modify the training corpus
- [ ] Propagate data structure modification
- [ ] Improve user-friendliness
- [ ] Make the programs into at most 5 files
