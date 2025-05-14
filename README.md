
# Swipe and Slice Game

"Swipe and Slice" is an exciting and interactive game where you use hand gestures to slice falling fruits. The game utilizes MediaPipe for real-time hand gesture recognition and OpenCV for computer vision.

## Requirements:

* Python 3.x
* OpenCV
* MediaPipe
* Numpy

To install the required libraries, run:

```
pip install -r requirements.txt
```

## How to Play:

* A fruit will appear at the top of the screen and fall down.
* Use your hand in front of the webcam to "slice" the fruit by swiping in the air.
* Each time you slice a fruit, you earn points.
* If a fruit hits the ground without being sliced, you lose a life.
* The game ends when all lives are lost.

## Key Features:

* Hand Gesture Recognition: The game uses MediaPipe’s hand tracking to detect swipes and movements.
* Simple Gameplay: Track falling fruits with your hands and slice them to earn points.
* Live Feedback: Real-time display of score and remaining lives.

## How to Run:

1. Clone the repository:
```
  git clone https://github.com/Geethasri16/Swipe_and_Slice.git
```
2. Navigate to the project directory:

   ```
   cd swipe-and-slice
   ```
3. Install the requirements:

   ```
   pip install -r requirements.txt
   ```
4. Run the game:

   ```
   python slice_and_dice.py
   ```
5. Press `q` to quit the game.

## Contribution:

Feel free to fork this repository and submit pull requests. Contributions are welcome for adding new features, improving the game, or fixing bugs.



