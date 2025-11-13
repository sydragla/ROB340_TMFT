from pylips.speech import RobotFace
from pylips.face import FacePresets
from pylips.face import ExpressionPresets

def main() -> None:
    face = RobotFace()

    # VOICE OPTIONS - AMAZON POLLY
        # Ivy - Female Child
        # Joanna - Female Adult (good voice)
        # Kendra - Female Adult
        # Kimberly - Female Adult
        # Salli - Female Adult (okay voice)
        # Joey - Male Adult (good voice)
        # Justin - Male Child (okay voice)
        # Matthew - Male Adult (good voice) - deeper than Joey
        # Brian - British Male Adult


    # GINGY - NON-HUMAN - GINGERBREAD MAN 

    # face = RobotFace(tts_method='polly', voice_id='Joey')
    # face.set_appearance(FacePresets.gingerbreadman)


    # EVE - NON-HUMAN - BLUE EYES

    # face = RobotFace(tts_method='polly', voice_id='Salli')
    # face.set_appearance({
    #         'background_color': "#000000",
    #         'eyeball_color': "#00000000",
    #         'iris_color': "#229cff",
    #         'eye_size': 500,
    #         'eye_height': 100,
    #         'eye_separation': 900,
    #         'iris_size': 150,
    #         'pupil_scale': 0.9,
    #         'eye_shine': False,
    #         'eyelid_color': "#FFFFFF",
    #         'nose_color': "#00000000",
    #         'nose_vertical_position': 0,
    #         'nose_width': 0,
    #         'nose_height': 0,
    #         'mouth_color': "#00000000",
    #         'mouth_width': 220,
    #         'mouth_height': 30,
    #         'mouth_thickness': 18,
    #         'brow_color': "#00000000",
    #         'brow_width': 70,
    #         'brow_height': 210,
    #         'brow_thickness': 20
    # })


    # MATTHEW - HUMAN - MALE

    face = RobotFace(tts_method='polly', voice_id='Matthew')
    face.set_appearance({
        'background_color': "#FDE7DD",
            'eyeball_color': '#ffffff',
            'iris_color': "#A1CAF1",
            'eye_size': 130,
            'eye_height': 70,
            'eye_separation': 400,
            'iris_size': 80,
            'pupil_scale': .7,
            'eye_shine': True,
            'eyelid_color': '#D7E4F5',
            'nose_color': '#ff99cc',
            'nose_vertical_position': -40,
            'nose_width': 0,
            'nose_height': 0,
            'mouth_color': '#2c241b',
            'mouth_width': 450,
            'mouth_height': 20,
            'mouth_thickness': 18,
            'brow_color': '#2c241b',
            'brow_width': 130,
            'brow_height': 210,
            'brow_thickness': 22
    })


    # ANNA - HUMAN - FEMALE

    # face = RobotFace(tts_method='polly', voice_id='Joanna')
    # face.set_appearance({
    #         'background_color': '#f9cebb',
    #         'eyeball_color': '#ffffff',
    #         'iris_color': '#818c3c',
    #         'eye_size': 140,
    #         'eye_height': 80,
    #         'eye_separation': 400,
    #         'iris_size': 80,
    #         'pupil_scale': .7,
    #         'eye_shine': True,
    #         'eyelid_color': '#D7E4F5',
    #         'nose_color': '#ff99cc',
    #         'nose_vertical_position': -40,
    #         'nose_width': 0,
    #         'nose_height': 0,
    #         'mouth_color': "#d1908e",
    #         'mouth_width': 300,
    #         'mouth_height': 20,
    #         'mouth_thickness': 27,
    #         'brow_color': "#6d4730",
    #         'brow_width': 100,
    #         'brow_height': 210,
    #         'brow_thickness': 12
    # })

    # because of this while loop, it is easier to rerun the code
    # and uncomment faces than make multiple faces
    while True:
        _input = input("> ")
        if not _input:
            continue
        face.say(_input)

if __name__ == "__main__":
    main()