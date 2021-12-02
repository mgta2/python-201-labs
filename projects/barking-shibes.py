# Use a quotes API, e.g. http://quotes.stormconsultancy.co.uk/random.json
# to fetch a random quote. Then use string manipulation to convert it to
# Doge speech (https://blogs.unimelb.edu.au/sciencecommunication/2016/10/22/how-to-speak-doge/)
# Create a tiny webpage that displays a doge image together
# with the altered quote. You can get an image URL from another API:
# http://shibe.online/api/shibes
# Write the code logic to make the API calls and assign the output to
# `doged_quote` and `doge_image_url` respectively.
# Then write the `html` string to a `.html` file and look at it in your browser.

# -----------------------------------------------------------------------------

# Following along with https://www.youtube.com/watch?v=4WNMMOk958A&t=423s&ab_channel=CodingNomads
# for the HTML at the end.

import requests
from pathlib import Path

quotes_url = "http://quotes.stormconsultancy.co.uk/random.json"
images_url = "http://shibe.online/api/shibes"

quote_response = requests.get(quotes_url)
image_response = requests.get(images_url)

quote = quote_response.json()['quote']
doged_quote = "Wow! " + quote + " Much quote."

doge_image_url = image_response.json()[0]

# With the necessary info gathered, it's time to make the html file.

html = f"<p>{doged_quote}</p><img src='{doge_image_url}'>"
file_path = Path().home().joinpath("Desktop").joinpath("dogescript.html")

with open(file_path, "w") as file_out:
    file_out.write(html)