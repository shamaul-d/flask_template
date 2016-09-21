from flask import Flask

sham = Flask(__name__)

@sham.route('/')
def deep():
    return 'insert deep quote here'

@sham.route('/nice')
def nice():
    return 'niceeeeeee'

@sham.route('/what')
def what():
    return 'what are you looking at'

if __name__ == '__main__':
    sham.run()
