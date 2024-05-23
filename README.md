# StayFIT App

## Introduction

**StayFIT App** stands at the forefront of fitness technology, representing a paradigm shift in how individuals monitor their workout repetitions with precision and efficacy. Crafted with meticulous attention to detail, this cutting-edge Python application caters to the needs of fitness enthusiasts and athletes alike, offering a seamless and intuitive solution for tracking workout progress.

At its core, StayFIT App prioritizes real-time body posture detection as the cornerstone of its functionality. Leveraging the powerful capabilities of the **OpenCV** library, the application meticulously scrutinizes body postures through a live camera feed, ensuring that users maintain correct form and alignment during their workouts. By analyzing key body landmarks and movements in real-time, StayFIT App provides invaluable feedback to users, empowering them to optimize their exercise routines for maximum effectiveness and safety.



## Features

- **Real-time Body Posture Detection:** Detects and analyzes body postures to ensure correct form during exercises.
- **Automatic Rep Counting:** Counts repetitions accurately based on detected movements.
- **User-friendly Interface:** Interactive and intuitive interface designed for ease of use.
- **Visual Feedback:** Provides visual cues and feedback to guide users during their workouts.
- **Customizable Workouts:** Easily adaptable for various exercises and workout routines.

## How It Works

1. **Camera Feed Capture:** The application captures a real-time video feed from the camera.
2. **Posture Detection:** Utilizing OpenCV, it identifies key body landmarks to determine the user's posture.
3. **Repetition Counting:** Based on the detected movements and postures, the application counts repetitions and provides real-time feedback.
4. **Visual Feedback:** Visual cues and indicators guide the user to maintain correct form and complete each repetition effectively.

## Getting Started

### Prerequisites

- Python 3.8.10
- OpenCV
- Pillow


```python
from BasicPoseModule import PoseModule

# Initialize Pose Module
pose = PoseModule()

# Main loop
while True:
    # Get frame from camera
    frame = capture_frame()
    
    # Perform pose detection
    landmarks = pose.detect_landmarks(frame)
    
    # Count push-ups and provide feedback
    push_up_count = pose.count_push_ups(landmarks)
    pose.display_feedback(frame, push_up_count)
```

![](https://github.com/Abdul-Rehman-Astro/Pushups_by_Abdul/blob/main/Images/Pushup%20counter.png)
![](https://github.com/Abdul-Rehman-Astro/Pushups_by_Abdul/blob/main/Images/Pushup%20counter%202.png)

![alt text](https://google.github.io/mediapipe/images/mobile/pose_tracking_full_body_landmarks.png)



![1](https://github.com/Abdul-Rehman-Astro/Stayfit/blob/main/Project%20photos/3.png)
![2](https://github.com/Abdul-Rehman-Astro/Stayfit/blob/main/Project%20photos/2.png)
![3](https://github.com/Abdul-Rehman-Astro/Stayfit/blob/main/Project%20photos/4.png)
![4](https://github.com/Abdul-Rehman-Astro/Stayfit/blob/main/Project%20photos/5.png)
