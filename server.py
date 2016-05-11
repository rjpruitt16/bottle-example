import bottle

APP = bottle.Bottle()

@APP.get('/index.html')
def index():
  return bottle.static_file('index.html', '.')

if __name__ == '__main__':
  bottle.run(application=APP)
