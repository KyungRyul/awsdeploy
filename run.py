from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'aws'
# 1
if __name__ == '__main__':
  app.run(debug=True, ip='0.0.0.0')