from flask import Flask, session, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = 'chapstick'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def load_homepage():
  return render_template('home.html')

@app.route('/secretkey')
def show_partyinfo():
  SECRET_KEY= 'chapstick'
  secretcode = request.args['secretkey']

  if (SECRET_KEY == secretcode):
    session['code_entered'] = True
    return redirect('/invitation')
  else:
    return render_template('error.html')

@app.route('/invitation')
def show_invitation():
  if session.get('code_entered', False):
    return render_template('invitation.html')
  else:
    return redirect('/')