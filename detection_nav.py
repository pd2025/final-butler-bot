import object_detection
import basic_drive_code_v2

basic_drive_code_v2.configure_motors(basic_drive_code_v2.mc)



def targetInPos(target):
    if target == "Goli":
        lowThreshX = 260.0
        upThreshX = 310.0
        lowThreshY = 50.0
        upThreshY = 120.0

    if target == "Celsuius":
        lowThreshX = 0.0
        upThreshX = 0.0
        lowThreshY = 0.0
        upThreshY = 0.0

    if target == "Mountain Dew":
        lowThreshX = 0.0
        upThreshX = 0.0
        lowThreshY = 0.0
        upThreshY = 0.0

    if target == "Diet":
        lowThreshX = 0.0
        upThreshX = 0.0
        lowThreshY = 0.0
        upThreshY = 0.0

    if object_detection.prediction['class'] == target and object_detection.prediction['x'] >= lowThreshX and object_detection.prediction['x'] <= upThreshX and object_detection.prediction['y'] >= lowThreshY and object_detection.prediction['y'] <= upThreshY:
        return True
    else:
        return False

def search(self):
    while object_detection.prediction['class'] == None:
        basic_drive_code_v2.turn_right(self, 20)

    object_detection.stop_all_motors(self)

def seekTarget(self):

    search(self)

    while not targetInPos():
        if object_detection.prediction['x'] < lowThreshX and object_detection.prediction['y'] < lowThreshY:
            object_detection.stop_all_motors(self)
            basic_drive_code_v2.move_front_right(self, 50)

        if object_detection.prediction['x'] > upThreshX and object_detection.prediction['y'] > upThreshY:
            object_detection.stop_all_motors(self)
            basic_drive_code_v2.move_back_left(self, 50, 0.25)

        if object_detection.prediction['x'] < lowThreshX and object_detection.prediction['y'] > upThreshY:
            object_detection.stop_all_motors(self)
            basic_drive_code_v2.move_back_right(self, 50, 0.25)

        if object_detection.prediction['x'] > upThreshX and object_detection.prediction['y'] < lowThreshY:
            object_detection.stop_all_motors(self)
            basic_drive_code_v2.move_front_left(self, 50, 0.25)
        
        elif object_detection.prediction['x'] < lowThreshX:
            object_detection.stop_all_motors(self)
            basic_drive_code_v2.translate_right(self, 50, 0.25)

        elif object_detection.prediction['x'] > upThreshX:
            object_detection.stop_all_motors(self)
            basic_drive_code_v2.translate_left(self, 50, 0.25)

        elif object_detection.prediction['y'] < lowThreshY:
            object_detection.stop_all_motors(self)
            basic_drive_code_v2.move_forward(self, 50, 0.25)

        elif object_detection.prediction['y'] > upThreshY:
            object_detection.stop_all_motors(self)
            basic_drive_code_v2.move_reverse(self, 50, 0.25)

    object_detection.stop_all_motors(self)