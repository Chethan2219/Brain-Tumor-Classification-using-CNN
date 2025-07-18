Brain Tumor Classification using CNN
  Author : Chethan T
🧠 Overview
This project combines deep learning and web development to create an MRI brain tumor classification system. It begins with a Jupyter Notebook (tumor-classification-cnn.ipynb) that preprocesses MRI data and builds a robust Convolutional Neural Network (CNN) for classifying brain tumors. CNNs were chosen for their proven success in identifying spatial features in medical images, offering excellent performance for MRI analysis.

The trained model is then deployed in a user-friendly web interface using Flask, allowing real-time predictions on test MRI scans. This demonstrates the potential of deep learning for practical, real-world medical applications.

🚀 Features
Jupyter Notebook: End-to-end model development with preprocessing, training, evaluation, and visualization.

Flask Web App: A clean web interface to visualize model predictions on test MRI images using the trained CNN.

Data Augmentation: Used TensorFlow’s ImageDataGenerator for better generalization and reducing overfitting.

🛠 Technologies Used
Backend: Flask

Deep Learning: TensorFlow, Keras

Data Handling & Visualization: NumPy, Pandas, Matplotlib, Seaborn

Image Processing: PIL

Others: Logging, Exception Handling

🧹 Data Preprocessing
Dataset: MRI Brain Tumor Dataset from Kaggle

Preprocessing Steps:

Resizing and normalizing images

Augmentation (rotation, zoom, flip)

Splitting into training and test sets

🧠 CNN Model Architecture
Sequential CNN with 8 convolutional layers and max pooling

Final softmax output layer for multi-class classification

3.7M+ trainable parameters using Adamax optimizer and categorical cross-entropy loss

Classes: Glioma, Meningioma, No Tumor, Pituitary

📊 Model Evaluation
Evaluated on training, validation, and test sets

Achieved high classification accuracy

Includes confusion matrix, classification report, and prediction visualizations

🌐 Web App Deployment
Built using Flask for real-time prediction on test images

Successfully deployed on Render with optimizations for free-tier memory limits

Logging and exception handling included for better debugging

🔄 Planned Enhancements
User Image Upload: Allow users to upload MRI scans for prediction (requires server upgrade)

Improved UI: Better interactivity and loading indicators

Scalability: Preparing for higher usage load with better resource management

💡 Key Learnings
Practical application of CNNs in medical imaging

Full-stack workflow: Data science to web deployment

Debugging, optimization, and cloud deployment (Render.com)

UI/UX design considerations under constrained environments

🧪 Run the Project Locally
🔧 Prerequisites
    Python 3.11
    pip
    Jupyter Notebook
    Internet access for dataset download

📓 Running the Notebook
    Download dataset from Kaggle
    Place it in the appropriate folder in the project directory
 Launch:

    jupyter notebook
 Open tumor-classification-cnn.ipynb

🌐 Running Flask App
  Clone the repo:

    git clone https://github.com/chethan-t/brain-tumor-classification-cnn.git
    cd brain-tumor-classification-cnn
Install dependencies:

    pip install -r requirements.txt
Run the app:

    python app.py
Visit: http://127.0.0.1:5000
