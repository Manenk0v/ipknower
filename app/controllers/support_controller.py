from app import app
from flask import render_template
@app.route('/support/privacy_policy')
def privacy_policy():
    # ...
    return render_template(
        "support/privacy_policy.html",
        )
@app.route('/support/agreement')
def agreement():
    # ...
    return render_template(
        "support/agreement.html",
        )
@app.route('/support/help')
def help():
    # ...
    return render_template(
        "support/help.html",
        )







