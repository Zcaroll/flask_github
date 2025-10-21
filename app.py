from flask import Flask, render_template, request  # NOT the same as requests 
from github_api import get_github_user
app = Flask(__name__)

@app.route('/') # home page
def homepage():
    return render_template('index.html')

# handle requests to /get_user
@app.route('/get_user') # dont forget the /
def get_user_info():
    # get user info and display on a new page
    print('form data is', request.args)  # prints to terminal for debugging
    username = request.args.get('username') # safer
    # username = request.args['username'] # classic way to get form data. More error-prone
    user_info, error_message = get_github_user(username) #user info dictionary
    
    # redirect user to an error page if there is an error
    if error_message:
        return render_template('error.html', error=error_message)
    else:
        return render_template('github.html', user_info=user_info) # redirects webpage to github.html


if __name__ == '__main__':
    app.run()