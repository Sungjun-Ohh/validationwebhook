from flask import jsonify, request, Response
from app import app
import json


@app.route("/valid", methods=["POST"])
def getAddmissionReview():
    allowed = False
    result = "sjtest_result"
    warnings = "sjtest_warnings"
    data = request.json  
    print (json.dumps(data))
    uid = data["request"]["uid"]

    return jsonify({
      "kind": "AdmissionReview",
      "apiVersion": "admission.k8s.io/v1",
      "response": {
        "uid": uid,
        "allowed": allowed,
        "status": {
          "reason": result
        },
        "warnings" : [warnings]
        }})