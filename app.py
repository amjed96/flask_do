from flask import Flask, render_template, abort

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/messages/<int:idx>/')
def messages(idx):
    app.logger.info('Building the messages list ...')
    messages = ['Message Zero', 'Message One', 'Message Two']
    try:
        app.logger.debug(f'Get message with index: {idx}')
        return render_template('message.html', message=messages[idx])
    except IndexError:
        app.logger.error(f'Index {idx} is out of range causing an IndexError')
        abort(404)

@app.route('/500')
def error500():
    abort(500)
