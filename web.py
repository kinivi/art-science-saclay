from distutils.log import debug
import flask
from flask import Flask, request, render_template, Response
import logging
import argparse
import serial
from numpy import broadcast
from persona_bot import persona_bot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = Flask(__name__)
app.config['SERIAL_TIMEOUT'] = 0.2
app.config['SERIAL_PORT'] = '/dev/cu.usbmodemHIDPC1'
app.config['SERIAL_BAUDRATE'] = 9600
app.config['SERIAL_BYTESIZE'] = 8
app.config['SERIAL_PARITY'] = 'N'
app.config['SERIAL_STOPBITS'] = 1

logging.info("Starting up bot")

parser = argparse.ArgumentParser(description=None)

parser.add_argument("-p", "--persona", default="guru")
args = parser.parse_args()
persona = args.persona

bot = persona_bot(persona_name=persona, log_level=logging.DEBUG)


@app.route('/get')
def bot_response(question=None):
    question = request.args.get("msg")
    logger.info("Q: " + question)
    response = bot.ask(question)
    logger.info("A: " + response)
    return response

@app.route('/')
def chat():
    # template largely based off of chatterbot python implementation
    # https://github.com/chamkank/flask-chatterbot
    return render_template('index.html', persona=bot.persona)

def event_barcode():
    ser = serial.Serial()
    ser.port = app.config['SERIAL_PORT']
    ser.baudrate = app.config['SERIAL_BAUDRATE']
    ser.bytesize = app.config['SERIAL_BYTESIZE']
    ser.parity = app.config['SERIAL_PARITY']
    ser.stopbits = app.config['SERIAL_STOPBITS']
    ser.open()
    s = ser.read(1)
    yield 'data: %s\n\n' % s

@app.route('/barcode')
def barcode():
    newresponse = flask.Response(event_barcode(), mimetype="text/event-stream")
    newresponse.headers.add('Access-Control-Allow-Origin', '*')
    return newresponse

    


if __name__ == '__main__':
    app.run(debug=True, port=8000)
