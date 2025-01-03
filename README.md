# Smart_Attendance_System
![Screenshot (62)](https://github.com/tripti033/Smart_Attendance_System/assets/107789391/d192c30b-c59e-43a2-b10f-25f0adeb51c7)


![Screenshot (627)](https://github.com/tripti033/Smart_Attendance_System/assets/107789391/6de3d62d-7da1-4088-adde-3e1316008c00)

This project implements an AI-based attendance system utilizing the Local Binary Patterns Histogram (LBPH) algorithm for face recognition. LBPH is a simple yet effective algorithm for facial feature extraction, especially suitable for controlled environments, making it ideal for attendance systems.  

## About Face Recognition  
Face recognition involves identifying or verifying a person from a facial image. It has two key tasks:  
- **Face Detection:** Locating faces within an image.  
- **Face Recognition:** Using the detected facial regions to recognize individual identities.  

Our system uses LBPH to recognize faces for automatic attendance marking.  

## The LBPH Algorithm  
Local Binary Patterns Histogram (LBPH) is a texture operator that labels pixels by comparing each pixel to its neighbors, creating a binary pattern. It has four primary parameters:  
- **Radius:** Defines the circular local binary pattern radius, typically set to 1.  
- **Neighbors:** Number of sample points around the central pixel, usually 8.  
- **Grid X and Grid Y:** Defines the grid dimensions, affecting the histogram size.  

### Steps of the LBPH Algorithm:  
1. **Parameter Selection:** Set radius, neighbors, and grid dimensions.  
2. **Training:** Use a dataset of labeled facial images to train the model.  
3. **LBP Operation:** Convert each pixel’s neighborhood into a binary pattern, creating an intermediate image.  
4. **Histogram Extraction:** Divide the image into grids, compute histograms, and concatenate them.  
5. **Face Recognition:** Compare histograms of the input image with stored histograms using distance metrics (e.g., Euclidean distance).  

LBPH is provided by the OpenCV library, supporting multiple languages, including C++ and Python, making it versatile for AI projects. You can also find an LBPH implementation in Go on [GitHub](https://github.com/kelvins/lbph).  

##Video Explaination


https://github.com/user-attachments/assets/d336ab9b-ec68-47da-b214-b93a30062515



## Contributions  
Feel free to contribute to improving this project!
