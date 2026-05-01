## Ship to Wikitext
# Extract ship data
* paste the contents of the faction's civilian, combat, station or emplacement folder into the /png folder
* run cosmoteer_save_tools.py
* this will output 2 files, ship-parts.json with only parts & ship-data.json with all the data for each ship file

# Create wikitext files
* run cosmoteer_create_page.py
* this should generate [shipname]wikitext.txt files inside the /wikitext folder

# Upload to wiki.gg
* make sure you have a wikimedia account, and an available bot associated
* run cosmoteer_send_to_wiki.py and login
* files should generate and send to site
* this can take a while
