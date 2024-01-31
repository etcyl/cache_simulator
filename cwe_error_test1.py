from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
  # Get user input from the query parameter "name"
  user_input = request.args.get('name', 'World')

  # This line is vulnerable to XSS. It directly places user_input into the HTML.
  return render_template_string('<h1>Hello, ' + user_input + '!</h1>')

if __name__ == '__main__':
  app.run(debug=True)
