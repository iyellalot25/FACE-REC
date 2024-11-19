# Real-Time Face Recognition Project  

## Overview  
This project implements a real-time face recognition system using Python and powerful libraries such as OpenCV and face_recognition. It detects and recognizes faces from a live video feed or pre-recorded video, providing a practical solution for authentication and surveillance.

## Features  
- **Face Detection**: Identifies faces in a video stream in real-time.  
- **Face Recognition**: Matches detected faces against a pre-defined database of known individuals.  
- **Scalability**: Supports adding new faces to the database dynamically.  

## Libraries Used  
- **OpenCV (cv2)**: For handling video streams and image processing.  
- **face_recognition**: For accurate and efficient face detection and recognition.  
- **NumPy (np)**: For efficient numerical computations.  
- **os**: For managing directories and files.  

## Installation  
1. Clone this repository:  
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```  
2. Install the required libraries:  
   ```bash
   pip install opencv-python face-recognition numpy
   ```  

## How It Works  
1. **Face Encoding**: Pre-processes images of known individuals and generates encodings.  
2. **Real-Time Recognition**: Detects faces from a live video feed and compares them against the stored encodings.  
3. **Output**: Displays the video feed with recognized names .  

## Running the Project  
1. Place images of known individuals in the `TRAIN` directory with filenames as their names (e.g., `john_doe.jpg`).  
2. Run the script:  
   ```bash
   python face_recognition.py
   ```  
3. The script will start the video feed and perform real-time recognition.  

## Project Structure  
```
.
├── TRAIN/          # Directory containing images of known individuals
├── face_recognition.py   # Main script for real-time face recognition
└── README.md             # Project documentation
```

## Future Improvements  
- Add a GUI for user interaction.  
- Integrate with a database for storing and retrieving face data.  
- Optimize for low-end devices.  

## Acknowledgments  
This project was inspired by the capabilities of OpenCV and the face_recognition library. Thanks to the developers for providing such powerful tools for computer vision.  

## License  
This project is licensed under the MIT License. Feel free to modify and use it as needed.  

---
```
