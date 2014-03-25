import BaseHTTPServer
import SimpleHTTPServer
import json
import urlparse


class ReactTutorialHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """
    Extension of SimpleHTTPRequestHandler that works with the react.js tutorial.
    In addition to standard SimpleHTTPServer file-webserver functionality, adds
    POST-ability.

    Upon receiving a POST:
    (1) converts posted data to a JSON object,
    (2) appends it to the json list assumed to be in the file at the requested URL, and
    (3) returns the updated list of data.

    USAGE: python server.py to serve files from the cwd
    (works the same as running python -m SimpleHTTPServer in the directory)
    """
    def do_POST(self):
        # Extract and print the contents of the POST
        content_length = int(self.headers['Content-Length'])
        post_data = dict(urlparse.parse_qsl(self.rfile.read(content_length).decode('utf-8')))
        try:
            f = open(self.translate_path(self.path), 'rb+')
        except IOError:
            self.send_error(404, "File not found")
            return None
        current_list = json.load(f)
        current_list.append(post_data)
        f.seek(0)
        json.dump(current_list, f)
        f.close()
        return self.do_GET()


def test(HandlerClass=ReactTutorialHTTPRequestHandler,
         ServerClass=BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandlerClass, ServerClass)


if __name__ == '__main__':
    test()