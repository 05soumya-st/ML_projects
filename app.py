import streamlit as st
import cv2
import numpy as np
import joblib
from PIL import Image
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd

@st.cache_resource
def load_model_and_encoder():
    model = joblib.load("model.pkl")
    encoder = joblib.load("label_encoder.pkl")
    print('*'*20, type(encoder))
    return model, encoder

@st.cache_data
def load_test_data():
    X_test = joblib.load("X_test.pkl")
    y_test = joblib.load("y_test.pkl")
    return X_test, y_test

def extract_color_histogram(img):
    hsv_img = cv2.cvtColor(img.astype("uint8"), cv2.COLOR_RGB2HSV)
    hist = cv2.calcHist([hsv_img], [0, 1, 2], None, [8, 8, 8],
                        [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist

# --- UI Setup ---
st.set_page_config(page_title="Tomato Leaf Disease Classifier")
st.title("🍅 Tomato Leaf Disease Prediction")

# Exit and session control
if "show_upload" not in st.session_state:
    st.session_state.show_upload = True

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

if st.button("❌ Exit App"):
    st.session_state.show_upload = False

if not st.session_state.show_upload:
    st.warning("👋 The app has been closed. Refresh the page to restart.")
    st.stop()

# Load model and data
model, encoder = load_model_and_encoder()
X_test, y_test = load_test_data()

# Initialize session state for uploader key if not present
if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = "uploader_1"

# File uploader with dynamic key
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], key=st.session_state.uploader_key)

def extract_color_histogram(image, bins=(8, 8, 8)):
    # Convert image to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Compute histogram and normalize
    hist = cv2.calcHist([hsv], [0, 1, 2], None, bins, [0, 180, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist

if uploaded_file is not None:
    # Read image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Display image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Extract features and predict
    features = extract_color_histogram(image).reshape(1, -1)
    prediction = model.predict(features)
    predicted_class = encoder.inverse_transform(prediction)[0]

    st.success(f"🌿 Predicted Disease: **{predicted_class}**")

    # Optionally show performance metrics
    if st.checkbox("Show Model Performance"):
        y_pred = model.predict(X_test)
        test_img = X_test[46]
        print(model.predict(test_img.reshape(1,-1)))
        report_dict = classification_report(y_test, y_pred, target_names=encoder.classes_, output_dict=True)
        accuracy = accuracy_score(y_test, y_pred)
         # Filter out irrelevant classes and low-score classes
        rows = []
        for label, metrics in report_dict.items():
            if label in ['accuracy', 'macro avg', 'weighted avg']:
                continue
            precision = metrics['precision']
            recall = metrics['recall']
            f1 = metrics['f1-score']
            support = metrics['support']
        
            # Include only if F1-score > 0 (or use another threshold if you prefer)
            if f1 > 0:
                rows.append({
                    'Class': label,
                    'Precision': round(precision, 2),
                    'Recall': round(recall, 2),
                    'F1-Score': round(f1, 2),
                    'Support': int(support)
                })
        
        # Create DataFrame
        metrics_df = pd.DataFrame(rows)
        
        # Show in Streamlit
        import streamlit as st
        st.subheader("📊 Filtered Class-wise Performance Metrics")
        st.dataframe(metrics_df, use_container_width=True)

    # Reset uploader with a button
    if st.button("🔁 Upload Another Image"):
        # Change the key to reset uploader
        st.session_state.uploader_key = f"uploader_{np.random.randint(10000)}"
        st.rerun()
