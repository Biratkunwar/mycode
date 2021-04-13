#!/usr/bin/python3

# allows creation of basic Flask web app
from flask import Flask
# allows Flask web app to respond with 3xx messages (redirects)
from flask import redirect
# allows Flask to redirect to the, "url for the following function..."
from flask import url_for

app = Flask(__name__)

# if you sent a GET to /admin
# it will return "Hello Admin" (anyone can do this... no restrictions)
@app.route("/admin")
def hello_admin():
    return "Hello Admin"

# listening for a GET to /guest/<guesty> where
# <guesty> is a captured variable passed into our function
# hello_guest()
@app.route("/guest/<guesty>")
def hello_guest(guesty):
    return f"Hello {guesty} Guest"
    #V2 FORMATTER - return "Hello {} Guest".format(guesty)
    #OLD FORMATTER - return "Hello %s as Guest" % guesty

@app.route("/user/<name>")
def hello_user(name):
    ## if you go to hello_user with a value of admin
    if name =="admin":
        # return a 302 response to redirect to /admin
        return redirect(url_for("hello_admin"))
    else:
        # return a 302 response to redirect to /guest/<guesty>
        return redirect(url_for("hello_guest",guesty = name))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
