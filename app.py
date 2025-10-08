import os
from flask import Flask, render_template, jsonify, request
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
csrf = CSRFProtect(app)

# Mimic a database
posts = [
    {
        "id": 1,
        "author": "Arch User",
        "avatar": "https://upload.wikimedia.org/wikipedia/commons/1/13/Arch_Linux_%22Crystal%22_icon.svg",
        "description": "Just finished setting up my new Arch Linux install. The flexibility is amazing! #Linux #Arch",
        "likes": 128
    },
    {
        "id": 2,
        "author": "Python Coder",
        "avatar": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png",
        "description": "Working on a cool new Flask project with Ajax and CSRF protection. It's so seamless!",
        "likes": 256
    },
    {
        "id": 3,
        "author": "Web Developer",
        "avatar": "https://cdn-icons-png.flaticon.com/512/1005/1005141.png",
        "description": "This is the post with the cool new UI style. What do you think?",
        "likes": 91  # Updated to match your image
    }
]

@app.route('/')
def index():
    """Renders the main page with all the posts."""
    return render_template('index.html', posts=posts)

@app.route('/like/<int:post_id>', methods=['POST'])
def like_post(post_id):
    """Handles the AJAX request to increment a specific post's like count."""
    post_to_like = next((post for post in posts if post['id'] == post_id), None)
    
    if post_to_like:
        post_to_like['likes'] += 1
        return jsonify({'likes': post_to_like['likes'], 'message': 'Post liked!'})
    
    return jsonify({'error': 'Post not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
