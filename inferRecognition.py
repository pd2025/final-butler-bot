from roboflow import Roboflow
import cv2

rf = Roboflow(api_key="sBjnK2nsooh1jA9mXNRS")
project = rf.workspace().project("butlerbot")
model = project.version(4).model

# Open video capture
cap = cv2.VideoCapture(0)  # Use 0 for webcam or provide video file path

frame_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_counter += 1

    # Perform inference on the frame
    results = model.predict(frame, confidence=78, overlap=30).json()

    # Process and print results
    if results['predictions']:
        for prediction in results['predictions']:
            print(f"Frame: {frame_counter}")
            print(f"  Detected: {prediction['class']}")
            print(f"  Confidence: {prediction['confidence']:.2f}")
            print(f"  Bounding Box:")
            print(f"    x: {prediction['x']}")
            print(f"    y: {prediction['y']}")
            print(f"    width: {prediction['width']}")
            print(f"    height: {prediction['height']}")
            
            # Check for additional attributes if they exist
            if 'attributes' in prediction:
                print("  Additional Attributes:")
                for attr, value in prediction['attributes'].items():
                    print(f"    {attr}: {value}")
            print("--------------------")
    else:
        print(f"Frame: {frame_counter}, No detections")
        print("--------------------")

    # Display the frame (optional)
    cv2.imshow('Video', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
