from flask import Flask, jsonify
from ai.persona_agent import generate_content_idea

app = Flask(__name__)

@app.route("/generate/<persona>")
def generate(persona):
    try:
        content = generate_content_idea(persona)
        return jsonify({"persona": persona, "output": content})
    except Exception as e:
        return jsonify({"error": str(e)}), 404

if __name__ == "__main__":
    app.run(debug=True)
