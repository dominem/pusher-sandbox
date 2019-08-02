Pusher Sandbox
==============

Visit https://pusher.com to get familiar with the Pusher.


1. `cp secrets.example.js secrets.js` and edit it.
2. `cp secrets.example.py secrets.py` and edit it.
3. `pipenv install`.
4. `pipenv shell`.
5. `env FLASK_APP=presence.py flask run`.
6. Visit the index.html file from your web browser.
7. Visit the file again in other tabs multiple times. Note what's going on
   with the pages content. The "Presence channel members count" number should
   change when you open or close an instance of the page.
8. Run `python main.py` and note what's going on with the pages content. It
   should add a new message under the "Pusher Sandbox" text. Run it multiple
   times.
