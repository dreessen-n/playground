from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/play/<int:num>/<string:color>')
def play(num, color):
    return render_template('index.html', num=num, color=color)

# Add in an error message for page not found - 404
@app.errorhandler(404)
def page_not_found(e):
    return f'Sorry! No response. Try again.'

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(host='localhost', port=5001, debug=True)    # Run the app in debug mode.