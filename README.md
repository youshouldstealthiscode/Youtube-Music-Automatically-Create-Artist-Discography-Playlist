# Youtube-Music-Automatically-Create-Artist-Discography-Playlist
youtube music, searches for all music by a specified artist and creates a playlist of their entire discography chronologically


chat GPT prompt/program description:

"write a program that uses the ytmusicapi API to look through the entire youtube music catalogue, gather all music a specific artist is included on, and create a playlist for the user called "<artist's name> + < Discography>", that is ordered chronologically, beginning with earliest releases and going from there in order of release date. be sure to include all music the artist is included on, i.e. albums singles EPs features, anything that has that artist's name on it.
...
write the same program but add the functionality that, in the case of multiple releases having occurred in the same year, orders the same-year releases in the playlist by the date they were uploaded to the youtube music platform"

--------------------------------------------------------------------------------------------------

!!!!!HOW TO SET UP THE YTMUSICAPI ENVIRONMENT FOR THE SCRIPT TO WORK:!!!!!

1. Install the necessary packages: If you haven't already, ensure that you have Python installed on your computer. Then open a terminal or command prompt and run the following command to install the required packages:

pip install ytmusicapi requests

2. Log in to YouTube Music: Open a web browser and log in to YouTube Music (https://music.youtube.com) with the Google account you want to use for authentication.
3. Open Developer Tools: Access the Developer Tools in your web browser:

    For Google Chrome: Press Ctrl + Shift + J (Windows/Linux) or Cmd + Opt + J (Mac).
    For Firefox: Press Ctrl + Shift + K (Windows/Linux) or Cmd + Opt + K (Mac).
4. Go to the Network tab: In the Developer Tools, click on the "Network" tab. If you don't see the "Network" tab, you may need to expand the Developer Tools window.
5. Refresh the YouTube Music page: Refresh the YouTube Music web page in your browser to capture network requests.
6. Search for the "browse" request: In the "Network" tab of Developer Tools, look for a request with "browse" in its name. You can use the search/filter feature to make it easier to find.
7. Copy the request headers: Click on the "browse" request and navigate to the "Headers" tab. Find the section labeled "Request Headers". Copy the entire block of text starting with "{" and ending with "}".
8. Create the headers_auth.json file: Open a text editor and paste the copied text into a new file. Save this file as "headers_auth.json" in the same directory where you'll run your ytmusicapi scripts.

Now you have successfully created the "headers_auth.json" file, which will be used by ytmusicapi to authenticate with your Google account. Remember to keep this file secure, as it contains sensitive information about your Google account.

To use the "headers_auth.json" file in your ytmusicapi scripts, follow the examples provided in previous answers, which demonstrate how to load the headers from the file and create a YTMusic instance for making API calls.
