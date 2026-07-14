from flask import Flask, jsonify
from tasks import generate_report

app = Flask(__name__)

@app.route("/run-report")
def run_report():

    task = generate_report.delay()

    return jsonify({
        "message": "Report task queued",
        "task_id": task.id
    })

@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(debug=True)
