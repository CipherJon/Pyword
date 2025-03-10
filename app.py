from flask import Flask, jsonify, render_template, request
from generator.password_generator import generate_password, evaluate_strength

app = Flask(__name__, template_folder='public')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    try:
        # Validate parameters
        length = int(request.args.get('length', 12))
        if not (8 <= length <= 64):
            raise ValueError('Password length must be between 8-64')

        # Get checkbox states (default to True for first three, False for special)
        use_upper = request.args.get('use_upper', 'true') == 'true'
        use_lower = request.args.get('use_lower', 'true') == 'true'
        use_digits = request.args.get('use_digits', 'true') == 'true'
        use_special = request.args.get('use_special', 'false') == 'true'

        # Validate at least one character set is selected
        if not any([use_upper, use_lower, use_digits, use_special]):
            raise ValueError('At least one character set must be selected')

        password = generate_password(
            length=length,
            use_upper=use_upper,
            use_lower=use_lower,
            use_digits=use_digits,
            use_special=use_special
        )
        strength = evaluate_strength(password)
        return jsonify({'password': password, 'strength': strength})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)