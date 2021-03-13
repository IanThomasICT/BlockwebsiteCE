# BlockwebsiteCE
Block website with Covenant Eyes in real-time. Specific for an Internet Filtering/Accountability software called Covenant Eyes.

This Python file runs in the background and blocks the current website that the user is viewing when the execute hotkey is pressed: "alt+`"

If the user is browsing the internet and the hotkey "alt + `" is pressed, the program will do the following:
1.) Copy the current website URL

2.) Parse the URL for just the basic domain name (e.g. www.google.com)

3.) Open a headless Chrome browser

4.) Navigates to the filter block site for Covenant Eyes

5.) Logs into Covenant Eyes using the username and password provided in the code

6.) Inserts the parsed url into the block field and blocks the website

7.) Restarts the Covenant Eyes Client to force the filter to take effect immediately

8.) Enters back into an infinite while loop until the hotkey is pressed again

Download the .vbs file and assign it to run upon Computer startup using "Task Scheduler" in Windows 10

Use the kill-hotkey "ctrl + alt + -" to stop the program/break the infinite while loop.
