# from flask import Flask, request, jsonify
# from shotgun_api3 import Shotgun

# app = Flask(__name__)
# sg = Shotgun('https://riff-intern.shotgrid.autodesk.com/', 'filemanager', 'mmuzarqwmxdvvsjin4Uebhtz%')


# @app.route("/webhook", methods=["POST"])
# def webhook():
#     # Get the data from the incoming request
#     data = request.json

#     # Process the data and fetch the updated data from ShotGrid
#     if data.get("event_type") == "Shotgun_Entity_Change":
#         entity_type = data.get("entity_type")
#         entity_id = data.get("entity_id")
#         updated_fields = data.get("attribute_names", [])

#         # Fetch the updated entity details
#         updated_entity = sg.find_one(entity_type, [["id", "is", entity_id]], fields=updated_fields)

#         # Do something with the updated_entity data (e.g., print it)
#         print("Updated entity data:", updated_entity)

#     return jsonify({"status": "success"})


# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000)


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.get_json()
        print(True)
        if data is not None:
            # Process the data received from the webhook
            print("Received webhook data:")
            print(jsonify(data))
            # Add your processing logic here
            # ...

            return jsonify({"status": "success"}), 200

    return jsonify({"status": "error"}), 400

if __name__ == '__main__':
    app.run(host='192.168.1.110', port=5000)

