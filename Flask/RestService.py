from flask import Flask, jsonify;
from flask_cors import CORS;

app = Flask(__name__)

CORS(app)

# ENTRY FOR BODY GESTURES
# {
#     _id: ObjectId("64f91b92cded846930b6ee05"),
#     id_in_robot: 'DummyId',
#     movement_name: 'Nod',
#     description: 'Nod to the user',
#     status: 'Active'
#   }

# ENTRY FOR FACIAL EXPRESSIONS
# {
#     _id: ObjectId("64f91b92cded846930b6ee04"),
#     id_in_robot: 'DummyId',
#     expression_name: 'Happy',
#     description: 'Expression for happiness',
#     animation: "import { AnimatedSprite, Texture } from 'pixi.js';\n" +
#       '                    const alienImages = [\n' +
#       "                        'image_sequence_01.png',\n" +
#       "                        'image_sequence_02.png',\n" +
#       "                        'image_sequence_03.png',\n" +
#       "                        'image_sequence_04.png',\n" +
#       '                    ];\n' +
#       '                    const textureArray = [];\n' +
#       '                    for (let i = 0; i < 4; i++){\n' +
#       '                        const texture = Texture.from(alienImages[i]);\n' +
#       '                        textureArray.push(texture);\n' +
#       '                    }\n' +
#       '                    const animatedSprite = new AnimatedSprite(textureArray);\n' +
#       '                    ',
#     status: 'Active'
#   }

# ENTRY FOR FACIAL EXPRESSIONS
# {
#     _id: ObjectId("64f91b92cded846930b6ee04"),
#     id_in_robot: 'DummyId',
#     expression_name: 'Happy',
#     description: 'Expression for happiness',
#     animation: "import { AnimatedSprite, Texture } from 'pixi.js';\n" +
#       '                    const alienImages = [\n' +
#       "                        'image_sequence_01.png',\n" +
#       "                        'image_sequence_02.png',\n" +
#       "                        'image_sequence_03.png',\n" +
#       "                        'image_sequence_04.png',\n" +
#       '                    ];\n' +
#       '                    const textureArray = [];\n' +
#       '                    for (let i = 0; i < 4; i++){\n' +
#       '                        const texture = Texture.from(alienImages[i]);\n' +
#       '                        textureArray.push(texture);\n' +
#       '                    }\n' +
#       '                    const animatedSprite = new AnimatedSprite(textureArray);\n' +
#       '                    ',
#     status: 'Active'
#   }

# ENTRY FOR ROUTINES
#   {
#     _id: ObjectId("64f91b92cded846930b6ee08"),
#     user: 'User1',
#     last_modified: ISODate("2023-09-07T00:38:42.551Z"),
#     name: 'Dance_1',
#     file: "{
#               "Block_1": {"Talk" : 1 , "Walk" : 3, "Energetic" : 2, "Happy": 3},
#               "Block_2": {"Nod" : 1 , "Hum" : 3},
#               "Block_3": {"Talk" : 2 , "Walk" : 2, "Energetic" : 2, "Happy": 2},
#               "Block_4": {"Listen" : 3}
#            }"
#   }

# ENTRY FOR SPEECH
# {
#     _id: ObjectId("64f91b92cded846930b6ee07"),
#     id_in_robot: 'DummyId',
#     element_name: 'Talk',
#     description: 'Lol',
#     status: 'Active'
#   }

# ENTRY FOR TONE OF VOICE
# {
#     _id: ObjectId("64f91b92cded846930b6ee06"),
#     id_in_robot: 'DummyId',
#     tone_name: 'Energetic',
#     description: 'Eskeler mode',
#     status: 'Unactive'
#   }


weather = {
    "data": [
    {
        "day": "1/6/2019",
        "temperature": "23",
        "windspeed": "16",
        "event": "Sunny"
    },
    {
        "day": "2/6/2019",
        "temperature": "21",
        "windspeed": "18",
        "event": "Rainy"
    },
    {
        "day": "3/6/2019",
        "temperature": "31",
        "windspeed": "12",
        "event": "Sunny"
    },
    {
        "day": "4/6/2019",
        "temperature": "5",
        "windspeed": "28",
        "event": "Snow"
    },
    {
        "day": "5/6/2019",
        "temperature": "17",
        "windspeed": "18",
        "event": "Rainy"
    },
    {
        "day": "6/6/2019",
        "temperature": "19",
        "windspeed": "21",
        "event": "Rainy"
    },
    {
        "day": "7/6/2019",
        "temperature": "28",
        "windspeed": "14",
        "event": "Sunny"
    }
    ]
}


@app.route("/", methods=['GET'])
def index():
    return "Welcome to CodezUp"

@app.route("/weatherReport/", methods=['GET'])
def WeatherReport():
     global weather
     return jsonify([weather])

if __name__ == '__main__':
    app.run(debug=True)