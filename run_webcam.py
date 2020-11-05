import argparse
import logging
import profile
import time
import cv2
import tensorflow as tf
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh
import math
import time
logger = logging.getLogger('TfPoseEstimator-WebCam')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

fps_time = 0
start_seconds = 0
end_seconds = 0
repeats = 0

start_time = time.time()

def findPoint(pose, p):
    for point in pose:
        try:
            body_part = point.body_parts[p]
            return int(body_part.x * width + 0.5), int(body_part.y * height + 0.5)
        except:
            return (0, 0)
    return (0, 0)

'''
Odleglosc euklidesowa - sluzy do obliczenia odleglosci pomiedzy dwoma punktami w przestrzeni trojwymiarowej.
Miara ta jest odległością wyrażoną w linii prostej między skupieniami. Dedykowana jest tylko dla zmiennych ilościowych.
'''


def euclidianDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


'''
Funkcja odpowiedzialna za znalezienie kata gdy znane sa trzy punkty wzor, jest to
obliczanie katow miedzy wektorami.
Wykorzystano prawo cosinusów cas(c) = (a^2+b^2-c^2)/2ab
'''


def cosAngle(p0, p1, p2):
    '''
        p1 is center point from where we measured angle between p0 and p2
    '''
    try:
        a = (p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2
        b = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        c = (p2[0] - p0[0]) ** 2 + (p2[1] - p0[1]) ** 2
        angle = math.acos((a + b - c) / math.sqrt(4 * a * b)) * 180 / math.pi
    except:
        return 0
    return int(angle)


def lungesStart(a, b, c, d):
    """
    a oraz b to katy miedzy udem a lydka
    c oraz d to katy miedzy tulowiem a szyja
    """
    if (a in range(74, 195) or b in range(74, 195)) and (c in range(110, 150) or d in range(110, 150)):
        return True
    return False


def lungesDone(a, b):
    """
    a and b are angles of legs
    """
    if a in range(74, 100) or b in range(74, 100):
        return True
    return False


def lungesDoneScore(a, b):
    """
    a and b are angles of legs
    """
    if a in range(74, 90) or b in range(74, 90):
        return True
    return False


def pushUps(a, b, c, d, e, f, g, h):
    if (a in range(75, 200) or b in range(75, 200)) and (c in range(135, 175) or d in range(135, 175)) and \
            (e in range(150, 190) or f in range(150, 190) and (g in range(130, 190) or h in range(130, 190))):
        return True
    return False


def pushUpsDone(a, b):
    if a in range(75, 110) or b in range(75, 110):
        return True
    return False


def pushUpsDoneScore(a, b):
    if a in range(75, 90) or b in range(75, 90):
        return True
    return False


def plank(a, b, c, d, e, f, g, h):
    # There are ranges of angle and distance to for plank.
    """
        a and b are angles of hands
        c and d are angle of legs
        e and f are angle of body and legs.
        g and h are angle of head and body
    """
    if (a in range(80, 185) or b in range(80, 185)) and (c in range(125, 180) or d in range(125, 180)) and \
            (e in range(115, 185) or f in range(115, 185) and (g in range(130, 190) or h in range(130, 190))):
        return True
    return False


def plankDone(a, b):
    if a in range(70, 100) or b in range(60, 100):
        return True
    return False


def squats(a, b, c, d):
    if (a in range(75, 195) or b in range(75, 195)) and (c in range(120, 190) or d in range(120, 190)):
        return True
    return False


def squatsDone(a, b):
    if a in range(75, 100) or b in range(75, 100):
        return True
    return False


def squatDoneScore(a, b):
    if a in range(75, 90) or b in range(75, 90):
        return True
    return False


def drawStr(dst, xxx_todo_changeme, s, color, scale):
    (x, y) = xxx_todo_changeme
    if color[0] + color[1] + color[2] == 255 * 3:
        cv2.putText(dst, s, (x + 1, y + 1), cv2.FONT_HERSHEY_PLAIN, scale, (0, 0, 0), thickness=4, lineType=10)
    else:
        cv2.putText(dst, s, (x + 1, y + 1), cv2.FONT_HERSHEY_PLAIN, scale, color, thickness=4, lineType=10)
    # cv2.line
    cv2.putText(dst, s, (x, y), cv2.FONT_HERSHEY_PLAIN, scale, (255, 255, 255), lineType=11)


class Program:
    parser = argparse.ArgumentParser(description='tf-pose-estimation realtime webcam')
    parser.add_argument('--camera', type=str, default=0)
    parser.add_argument('--resize', type=str, default='400x368')
    parser.add_argument('--resize-out-ratio', type=float, default=4.0)
    parser.add_argument('--model', type=str, default='cmu')
    parser.add_argument('--show-process', type=bool, default=False)
    args = parser.parse_args()

    # print( "mode 0: Only Pose Estimation \nmode 1: People Counter \nmode 2: Fall Detection \nmode 3: Yoga pose
    # angle Corrector \nmode 4: Planking/Push up Detection \nmode 5: Hourglass ratio")
    mode = 4  # int(input("Enter a mode : "))

    logger.debug('initialization %s : %s' % (args.model, get_graph_path(args.model)))
    w, h = model_wh(args.resize)
    if w > 0 and h > 0:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))
    else:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(432, 368),
                            tf_config=tf.ConfigProto(log_device_placement=True))
    logger.debug('cam read+')
    cam = cv2.VideoCapture(args.camera)
    ret_val, image = cam.read()
    logger.info('cam image=%dx%d' % (image.shape[1], image.shape[0]))
    count = 0
    i = 0
    frm = 0
    y1 = [0, 0]
    global height, width, out
    orange_color = (0, 140, 255)
    white_color = (0, 0, 0)
    while True:
        ret_val, image = cam.read()
        i = 1
        humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
        pose = humans
        image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)
        height, width = image.shape[0], image.shape[1]
        if mode == 1:
            hu = len(humans)
            cv2.putText(image, str(hu), (20, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                        color=(0, 0, 255))
        elif mode == 0:
            for human in humans:
                for i in range(len(humans)):
                    try:
                        a = human.body_parts[0]  # Head point
                        x = a.x * image.shape[1]
                        y = a.y * image.shape[0]
                        y1.append(y)
                    except:
                        pass
                    if (y - y1[-2]) > 30:
                        print("fall detected.", i + 1,
                              count)  # You can set count for get that your detection is working
        elif mode == 2:
            if len(pose) > 0:
                "Wykroki"
                # angle
                angle1 = cosAngle(findPoint(pose, 10), findPoint(pose, 9), findPoint(pose, 8))
                angle2 = cosAngle(findPoint(pose, 13), findPoint(pose, 12), findPoint(pose, 11))
                angle3 = cosAngle(findPoint(pose, 8), findPoint(pose, 1), findPoint(pose, 0))
                angle4 = cosAngle(findPoint(pose, 11), findPoint(pose, 1), findPoint(pose, 0))
                # distance
                wrist_hipR = int(euclidianDistance(findPoint(pose, 4), findPoint(pose, 8)))
                wrist_hipL = int(euclidianDistance(findPoint(pose, 7), findPoint(pose, 11)))
                wrist_noseR = int(euclidianDistance(findPoint(pose, 4), findPoint(pose, 0)))
                wrist_noseL = int(euclidianDistance(findPoint(pose, 7), findPoint(pose, 0)))

                if angle1 < 70:
                    cv2.putText(image, "Zachowaj kat prosty w kolanie!", (20, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                color=(0, 0, 255))
                if angle3 < 150 or angle4 > 150:
                    cv2.putText(image, "Patrz przed siebie!", (20, 70), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                color=(0, 0, 255))
                if wrist_hipR > wrist_noseR:
                    cv2.putText(image, "Trzymaj ręce przy ciele!", (20, 90), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                color=(0, 0, 255))

                if (mode == 2) and lungesStart(angle1, angle2, angle3, angle4) and (
                        wrist_hipL < wrist_noseL or wrist_hipR < wrist_noseR):
                    image = TfPoseEstimator.draw_humans2(image, humans, imgcopy=False)
                    is_lunges = True
                    if (mode == 2) and lungesDone(angle1, angle2):
                        image = TfPoseEstimator.draw_humans3(image, humans, imgcopy=False)
                        if (mode == 2) and lungesDoneScore(angle1, angle2):
                            image = TfPoseEstimator.draw_humans4(image, humans, imgcopy=False)
                            cv2.putText(image, "Powrot do gory!", (20, 80), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                        color=(255, 255, 255))

        elif mode == 3:
            if len(pose) > 0:
                # angle calcucations
                angle1 = cosAngle(findPoint(pose, 4), findPoint(pose, 3), findPoint(pose, 2))
                angle2 = cosAngle(findPoint(pose, 7), findPoint(pose, 6), findPoint(pose, 5))
                angle3 = cosAngle(findPoint(pose, 8), findPoint(pose, 9), findPoint(pose, 10))
                angle4 = cosAngle(findPoint(pose, 11), findPoint(pose, 12), findPoint(pose, 13))
                angle5 = cosAngle(findPoint(pose, 1), findPoint(pose, 8), findPoint(pose, 9))
                angle6 = cosAngle(findPoint(pose, 1), findPoint(pose, 11), findPoint(pose, 12))
                angle7 = cosAngle(findPoint(pose, 8), findPoint(pose, 1), findPoint(pose, 0))
                angle8 = cosAngle(findPoint(pose, 11), findPoint(pose, 1), findPoint(pose, 0))

                if angle3 < 133:
                    cv2.putText(image, "Nie zginaj kolan!", (20, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.75, color=(0, 0, 255))
                if angle5 < 148:
                    cv2.putText(image, "Tylek nizej!", (20, 70), cv2.FONT_HERSHEY_TRIPLEX, 0.75, color=(0, 0, 255))
                if angle7 < 128:
                    cv2.putText(image, "Patrz przed siebie!", (20, 90), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                                color=(0, 0, 255))

                if pushUps(angle1, angle2, angle3, angle4, angle5, angle6, angle7, angle8):
                    image = TfPoseEstimator.draw_humans2(image, humans, imgcopy=False)
                    if pushUpsDone(angle1, angle2):
                        image = TfPoseEstimator.draw_humans3(image, humans, imgcopy=False)
                        if pushUpsDoneScore(angle1, angle2):
                            image = TfPoseEstimator.draw_humans4(image, humans, imgcopy=False)
                            cv2.putText(image, "Powrot do gory!", (20, 80), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                        color=(255, 255, 255))

        elif mode == 4:
            # distance calculations
            foot_distance = int(euclidianDistance(findPoint(pose, 10), findPoint(pose, 13)))
            ankle_distance = int(euclidianDistance(findPoint(pose, 3), findPoint(pose, 6)))
            # angle calcucations
            angle1 = cosAngle(findPoint(pose, 7), findPoint(pose, 6), findPoint(pose, 5))
            angle2 = cosAngle(findPoint(pose, 4), findPoint(pose, 3), findPoint(pose, 2))
            angle3 = cosAngle(findPoint(pose, 8), findPoint(pose, 9), findPoint(pose, 10))
            angle4 = cosAngle(findPoint(pose, 11), findPoint(pose, 12), findPoint(pose, 13))
            angle5 = cosAngle(findPoint(pose, 1), findPoint(pose, 8), findPoint(pose, 9))
            angle6 = cosAngle(findPoint(pose, 1), findPoint(pose, 11), findPoint(pose, 12))
            angle7 = cosAngle(findPoint(pose, 0), findPoint(pose, 1), findPoint(pose, 8))
            angle8 = cosAngle(findPoint(pose, 0), findPoint(pose, 1), findPoint(pose, 11))

            print('kat 7 : ' + str(angle7))
            print('kat 8 : ' + str(angle8))


            if angle1 < 70:
                cv2.putText(image, "Trzymaj kat prosty w lokciach!", (20, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.75,
                            color=(0, 0, 255))
            if angle3 < 123:
                cv2.putText(image, "Nie zginaj kolan!", (20, 60), cv2.FONT_HERSHEY_TRIPLEX, 0.75, color=(0, 0, 255))
            if angle5 < 125:
                cv2.putText(image, "Tylek nizej!", (20, 70), cv2.FONT_HERSHEY_TRIPLEX, 0.75, color=(0, 0, 255))
            if angle7 < 130:
                cv2.putText(image, "Patrz przed siebie!", (20, 80), cv2.FONT_HERSHEY_TRIPLEX, 0.75, color=(0, 0, 255))

            if plank(angle1, angle2, angle3, angle4, angle5, angle6, angle7, angle8) and foot_distance < ankle_distance:
                image = TfPoseEstimator.draw_humans2(image, humans, imgcopy=False)
                if plankDone(angle1, angle2):
                    image = TfPoseEstimator.draw_humans3(image, humans, imgcopy=False)
                    cv2.putText(image, "Tak trzymaj!", (20, 90), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                color=(255, 255, 255))

        elif mode == 5:
            if len(pose) > 0:
                # distance calculations
                foot_distance = int(euclidianDistance(findPoint(pose, 10), findPoint(pose, 13)))
                knee_distance = int(euclidianDistance(findPoint(pose, 9), findPoint(pose, 12)))
                ankles_distance = int(euclidianDistance(findPoint(pose, 2), findPoint(pose, 5)))
                # angle calcucations
                angle1 = cosAngle(findPoint(pose, 11), findPoint(pose, 12), findPoint(pose, 13))
                angle2 = cosAngle(findPoint(pose, 8), findPoint(pose, 9), findPoint(pose, 10))
                angle3 = cosAngle(findPoint(pose, 8), findPoint(pose, 1), findPoint(pose, 0))
                angle4 = cosAngle(findPoint(pose, 11), findPoint(pose, 1), findPoint(pose, 0))

                if angle3 < 120:
                    cv2.putText(image, "Glowa przed siebie!", (20, 60), cv2.FONT_HERSHEY_TRIPLEX, 0.75, color=(0, 0, 255))
                if foot_distance < 0.60 * ankles_distance:
                    cv2.putText(image, "Rozszerz stopy!", (20, 60), cv2.FONT_HERSHEY_TRIPLEX, 0.75, color=(0, 0, 255))
                if foot_distance > 1.55 * ankles_distance:
                    cv2.putText(image, "Stopy za szeroko!", (20, 60), cv2.FONT_HERSHEY_TRIPLEX, 0.75, color=(0, 0, 255))

                if squats(angle1, angle2, angle3, angle4) and (
                        foot_distance >= 0.4 * knee_distance) and (
                        foot_distance <= 1.6 * knee_distance) \
                        and (foot_distance >= 0.4 * ankles_distance) and (foot_distance <= 1.95 * ankles_distance):

                    image = TfPoseEstimator.draw_humans2(image, humans, imgcopy=False)
                    if squatsDone(angle1, angle2):
                        image = TfPoseEstimator.draw_humans3(image, humans, imgcopy=False)
                        if squatDoneScore(angle1, angle2):
                            image = TfPoseEstimator.draw_humans4(image, humans, imgcopy=False)
                            drawStr(image, (20, 50), "Squat", orange_color, 2)


        elif mode == 6:
            shoulder_hand_dst_l = int(euclidianDistance(findPoint(pose, 5), findPoint(pose, 7)))
            shoulder_hand_dst_r = int(euclidianDistance(findPoint(pose, 2), findPoint(pose, 4)))
            body_part_dst_l = int(euclidianDistance(findPoint(pose, 11), findPoint(pose, 13)))
            body_part_dst_r = int(euclidianDistance(findPoint(pose, 8), findPoint(pose, 10)))
            body_ratio_l = round(shoulder_hand_dst_l / body_part_dst_l, 2)
            body_ratio_r = shoulder_hand_dst_r / body_part_dst_r
            head_ankle = int(euclidianDistance(findPoint(pose, 15), findPoint(pose, 13)))
            hand_hand = shoulder_hand_dst_l + shoulder_hand_dst_l + int(
                euclidianDistance(findPoint(pose, 2), findPoint(pose, 5)))

            total_ratio = round(head_ankle / hand_hand, 2)
            drawStr(image, (20, 80), "hand_to_leg_ratio = " + str(body_ratio_l), orange_color, 1.5)
            drawStr(image, (20, 50), "height_to_width_ratio = " + str(total_ratio), orange_color, 1.5)

        cv2.putText(image,
                    "FPS: %f" % (1.0 / (time.time() - fps_time)),
                    (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 255, 0), 2)

        if frm == 0:
            out = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 15,
                                  (image.shape[1], image.shape[0]))
            print("Initializing")
            frm += 1
        cv2.imshow('tf-pose-estimation result', image)
        if i != 0:
            out.write(image)
        fps_time = time.time()
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
