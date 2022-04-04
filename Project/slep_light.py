import cv2
import mediapipe as mp
from grove.factory import Factory

relay = Factory.getGpioWrapper("Relay",16)
relay.off()

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def approximate(a, b, c):
      thres = 0.2
      if abs(a-b)<thres and abs(a-c)<thres and abs(b-c)<thres:
            return True

cap = cv2.VideoCapture(0)
with mp_pose.Pose(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    
    if results.pose_landmarks:
          
      nose_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y
      
      l_shoulder_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y
      
      r_shoulder_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y
      
      shoulder = (l_shoulder_y + r_shoulder_y) / 2
      
      l_hip_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y
      
      r_hip_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y
      
      hip = (l_hip_y + r_hip_y) / 2

    #   print(nose_y, shoulder, hip)

      if approximate(nose_y, shoulder, hip): relay.on()
      elif not approximate(nose_y, shoulder, hip): relay.off()
      
    cv2.imshow('Sleep light', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()