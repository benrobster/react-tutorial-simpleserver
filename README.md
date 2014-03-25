react-tutorial-simpleserver
===========================

Simple python HTTP Server to work with the [react.js tutorial](http://facebook.github.io/react/docs/tutorial.html).

The tutorial currently recommends using `python -m SimpleHTTPServer`.  However, that is a read-only server, and so if
you're following the tutorial literally, when you get to the part that talks about posting the data to the server, it
won't actually work and you may be frustrated. This extension of SimpleHTTPServer makes the tutorial work as written,
by accepting POST's of JSON data and appending them to the JSON list found in the requested url and then returning the
updated list.

### USAGE

1) Copy server.py into your react.js tutorial working directory.
2) Run `python server.py`
