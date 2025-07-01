from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <html>
            <body>
                <form action="/greet" method="post">
                    Enter your name: <input type="text" name="username">
                    <input type="submit" value="Submit">
                </form>
            </body>
        </html>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('username', 'Guest')
    return f"<h2>Hello, {name}!</h2>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)