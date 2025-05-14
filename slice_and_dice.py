import cv2
import mediapipe as mp
import random
import time
import math


lives = 5
score = 0
fruits = []
prev_x, prev_y = None, None
last_spawn_time = time.time()


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=2)

class Fruit:
    def __init__(self, x, y, velocity):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.radius = 30
        self.color = (0, 165, 255)
        self.alive = True

    def move(self):
        self.y += self.velocity
        if self.y > 480:
            self.alive = False  

    def draw(self, frame):
        if self.alive:
            cv2.circle(frame, (self.x, self.y), self.radius, self.color, -1)


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    curr_x, curr_y = None, None
    swipe = False

  
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            x = int(handLms.landmark[8].x * w)
            y = int(handLms.landmark[8].y * h)

            curr_x, curr_y = x, y
            cv2.circle(frame, (x, y), 10, (255, 0, 255), -1)

            # Detect swipe
            if prev_x is not None and prev_y is not None:
                dist = math.hypot(curr_x - prev_x, curr_y - prev_y)
                if dist > 40:
                    swipe = True

  
    if time.time() - last_spawn_time > 1.5 and lives > 0:
        new_fruit = Fruit(random.randint(50, w - 50), 0, velocity=5)
        fruits.append(new_fruit)
        last_spawn_time = time.time()

  
    for fruit in fruits:
        if fruit.alive:
            fruit.move()
            fruit.draw(frame)

           
            if not fruit.alive and fruit.y > 480:
                lives -= 1

           
            elif swipe and curr_x is not None:
                if abs(fruit.x - curr_x) < fruit.radius and abs(fruit.y - curr_y) < fruit.radius:
                    fruit.alive = False
                    score += 1
                    cv2.putText(frame, "Smashed it", (fruit.x - 20, fruit.y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

   
    fruits = [fruit for fruit in fruits if fruit.alive]

    prev_x, prev_y = curr_x, curr_y

  
    cv2.putText(frame, "Swipe it 🍊Slice it!", (w // 2 - 150, 40), cv2.FONT_HERSHEY_DUPLEX, 1, (147, 112, 219), 2)

   
    cv2.putText(frame, f"Score: {score}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.putText(frame, f"Lives: {lives}", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)

   
    if lives <= 0:
        cv2.putText(frame, "GAME OVER", (w // 2 - 150, h // 2), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)

    frame_resized = cv2.resize(frame, (1280, 720))
    cv2.imshow("Swipe and Slice", frame_resized)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
