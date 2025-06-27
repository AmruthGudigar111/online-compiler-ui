from flask import Flask, request, jsonify
import subprocess
import uuid
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/run', methods=['POST'])
def run():
    data = request.get_json()
    language = data['language']
    code = data['code']
    user_input = data.get('input', '')

    filename = f'temp/{uuid.uuid4()}'
    if language == 'python':
        filepath = f"{filename}.py"
        with open(filepath, 'w') as f:
            f.write(code)
        result = subprocess.run(['python3', filepath], input=user_input.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elif language == 'c':
        c_path = f"{filename}.c"
        out_path = f"{filename}.out"
        with open(c_path, 'w') as f:
            f.write(code)
        compile_proc = subprocess.run(['gcc', c_path, '-o', out_path], stderr=subprocess.PIPE)
        if compile_proc.returncode != 0:
            return jsonify({'output': compile_proc.stderr.decode()})
        result = subprocess.run([out_path], input=user_input.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        return jsonify({'output': 'Unsupported language'})

    return jsonify({'output': result.stdout.decode() + result.stderr.decode()})

if __name__ == '__main__':
    import os
    os.makedirs('temp', exist_ok=True)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))