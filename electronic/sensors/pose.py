# # navigation.py
# import numpy as np
# import cv2



# def navigate_to_goal(goal):
#     # Implement SLAM and path planning logic
#     pass

import cv2
import numpy as np

frame_width = 1280
frame_height = 720

# Open video captures
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

cap1.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

if not cap1.isOpened() or not cap2.isOpened():
    print("Error: Could not open video streams.")
    cap1.release()
    cap2.release()
    exit()

# Camera matrices and distortion coefficients
left_camera_matrix = np.array([[1231.2624, 0.0, 623.937802],
                               [0.0, 1248.92337, 381.563295],
                               [0.0, 0.0, 1.0]])

left_dist_coeffs = np.array([-0.171258074, 3.68086343, 0.0231561412, -0.00185566113, -18.8284582])

R1 = np.eye(3, dtype=np.float32)
P1 = np.hstack((left_camera_matrix, np.zeros((3, 1), dtype=np.float32)))

right_camera_matrix = np.array([[1231.2624, 0.0, 623.937802],
                                [0.0, 1248.92337, 381.563295],
                                [0.0, 0.0, 1.0]])

right_dist_coeffs = np.array([-0.171258074, 3.68086343, 0.0231561412, -0.00185566113, -18.8284582])

R2 = np.eye(3, dtype=np.float32)
P2 = np.hstack((right_camera_matrix, np.zeros((3, 1), dtype=np.float32)))

while True:
    # Read frames from both cameras
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print("Error: Could not read frames from cameras.")
        break

    # Convert frames to grayscale
    left_img = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    right_img = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    if left_img.shape != right_img.shape:
        print("Error: Left and right images have different sizes.")
        print(f"Left img shape: {left_img.shape}")
        print(f"Right img shape: {right_img.shape}")
        break

    # Rectify images
    left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_dist_coeffs, R1, P1, left_img.shape[::-1], cv2.CV_32FC1)
    right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_dist_coeffs, R2, P2, right_img.shape[::-1], cv2.CV_32FC1)

    rectified_left = cv2.remap(left_img, left_map1, left_map2, cv2.INTER_LINEAR)
    rectified_right = cv2.remap(right_img, right_map1, right_map2, cv2.INTER_LINEAR)

    # Detect and compute features
    sift = cv2.SIFT_create()
    keypoints_left, descriptors_left = sift.detectAndCompute(rectified_left, None)
    keypoints_right, descriptors_right = sift.detectAndCompute(rectified_right, None)

    # Match features using FLANN
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(descriptors_left, descriptors_right, k=2)

    # Apply ratio test
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    # Draw matches
    img_matches = cv2.drawMatches(rectified_left, keypoints_left, rectified_right, keypoints_right, good_matches, None)
    cv2.imshow('Matches', img_matches)

    # Stereo block matching to produce disparity map
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(rectified_left, rectified_right).astype(np.float32) / 16.0

    # Display disparity map
    disparity_display = (disparity - disparity.min()) / (disparity.max() - disparity.min())
    cv2.imshow('Disparity', disparity_display)

    # Example focal length and baseline
    focal_length = left_camera_matrix[0, 0]  # Assuming focal lengths of both cameras are equal
    baseline = 0.01  

    # Avoid division by zero
    disparity[disparity == 0] = 0.1
    disparity[disparity == -1] = 0.1

    # Convert disparity to depth map
    depth_map = focal_length * baseline / disparity

    # Extract matched points
    pts_left = np.float32([keypoints_left[m.queryIdx].pt for m in good_matches])
    pts_right = np.float32([keypoints_right[m.trainIdx].pt for m in good_matches])

    # Check if there are enough points for findEssentialMat
    if len(pts_left) >= 5 and len(pts_right) >= 5:
        # Calculate essential matrix
        E, mask = cv2.findEssentialMat(pts_left, pts_right, focal=focal_length, pp=(left_camera_matrix[0, 2], left_camera_matrix[1, 2]))
        # print("Essential Matrix Shape:", E.shape)
        # print("Essential Matrix:", E)

        # Recover pose
        if E.shape == (3, 3):  # Ensure E is 3x3
            _, R, t, mask = cv2.recoverPose(E, pts_left, pts_right, focal=focal_length, pp=(left_camera_matrix[0, 2], left_camera_matrix[1, 2]))
            print("Current Pos:\n", t)
        else:
            print("Error: Essential matrix is not 3x3")
    else:
        print("Not enough points for findEssentialMat")

    if cv2.waitKey(1) == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
