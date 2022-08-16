"""
python script to define service apis
"""
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)
COLUMNS = ['FACTORY_ID', 'ORG_ID', 'COUNTRY', 'EXECUTION_DATE', 'FAIL_RATE']

@app.route("/")
def home():
    """
    home function to verify service has been deployed
    :return:
    """
    return "Inspectorio Data Engineer test"

@app.route("/query")
def query():
    """
    API for query data
    :return:
    """
    try:
        params = request.args.to_dict()
        qry = "SELECT * FROM FACTORY"
        if len(params) > 0:
            qry += " WHERE "
            lst = []
            for k, v in params.items():
                if k.upper() in ["COUNTRY"]:
                    v = "'{}'".format(v)
                lst.append(str(k) + " = " + str(v))
            qry += " AND ".join(lst)
        print(params, qry)
        with sqlite3.connect('test.db') as conn:
            cur = conn.cursor()
            cur.execute(qry)
            data = cur.fetchall()
            cols = [x[0] for x in cur.description]
            result = []
            for item in data:
                result.append({col: value for col, value in zip(cols, item)})
            return jsonify(result)
    except Exception as e:
        return jsonify({"message": str(e)})


@app.route("/add", methods=["POST"])
def add():
    """API for add data"""
    try:
        if not request.is_json:
            return jsonify({"message": "resquest is not in json format"})
        req = request.get_json()
        print(req)
        if "FACTORY_ID" not in req.keys():
            return jsonify({"message": "FACTORY_ID is missing!"})
        diff = [x for x in req.keys() if x not in COLUMNS]
        if len(diff) > 0:
            return jsonify({"message": "columns {} does not exists in table FACTORY".format(diff)})
        item = {k:v for k,v in req.items() if k in COLUMNS}
        qry = """INSERT INTO FACTORY (FACTORY_ID,ORG_ID,FAIL_RATE,COUNTRY,EXECUTION_DATE) VALUES """
        values = []
        for k in ["FACTORY_ID","ORG_ID","FAIL_RATE"]:
            values.append(str(req[k])) if k in req.keys() else values.append("")
        for k in ["COUNTRY","EXECUTION_DATE"]:
            values.append(f"'{req[k]}'") if k in req.keys() else values.append("")
        qry += "( " + ",".join(values) + ")"
        with sqlite3.connect('test.db') as conn:
            cur = conn.cursor()
            cur.execute(qry)
            conn.commit()
            return jsonify(item)
    except Exception as e:
        return jsonify({"message": "fail with Exception: " + str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000, debug=True)
