import cv2
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from ultralytics import YOLO
from PIL import Image, ImageTk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from concurrent.futures import ThreadPoolExecutor

# Load YOLOv8 models (Fire detection model and Accident detection model)
fire_model = YOLO(r"E:\COLLEGE  AND OTHER DOCUMENTS\accident detection 8-10-24\FinalFire12\detect\train\weights\best.pt")  # Fire detection model
accident_model = YOLO(r"E:\COLLEGE  AND OTHER DOCUMENTS\accident detection 8-10-24\runs 5-2-2025\detect\train2\weights\best.pt")  # Accident detection model

cap = None  # Video capture object
fire_detected = False  # Flag for fire detection
accident_detected = False  # Flag for accident detection

# Email configuration for alerts
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "**"  # Replace with your email
SENDER_PASSWORD = "**"  # Replace with your email password
FIRE_BRIGADE_EMAIL = "**"  # Replace with the actual fire brigade email
HOSPITAL_EMAIL = "**"  # Replace with actual hospital email
POLICE_EMAIL = "**"  # Replace with actual police email

# Function to send alert for fire detection
def send_fire_alert():
    global fire_detected
    if fire_detected:
        return  # Avoid sending multiple alerts
    
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = FIRE_BRIGADE_EMAIL
        msg['Subject'] = "Fire Detected Alert!"
        body = "Alert! A fire has been detected in the monitored video feed. Immediate action is required."
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, FIRE_BRIGADE_EMAIL, msg.as_string())
        server.quit()
        fire_detected = True  # Set the flag to avoid sending multiple alerts
    except Exception as e:
        print(f"Error sending fire alert: {e}")

# Function to send alert for accident detection
def send_accident_alert():
    global accident_detected
    if accident_detected:
        return  # Avoid sending multiple alerts

    try:
        subject = "Accident Detected Alert"
        body = "An accident has been detected. Please take immediate action."
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = ", ".join([HOSPITAL_EMAIL, POLICE_EMAIL])
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, [HOSPITAL_EMAIL, POLICE_EMAIL], msg.as_string())
        server.quit()
        accident_detected = True  # Set the flag to avoid sending multiple alerts
    except Exception as e:
        print(f"Error sending accident alert: {e}")

# Function to detect fire in the frame
def detect_fire(frame):
    results = fire_model(frame)
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            class_id = int(box.cls[0])
            
            if class_id == 0:  # Fire class
                label = f"Fire {conf:.2f}"
                color = (0, 0, 255)  # Red for fire
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                
                send_fire_alert()  # Send alert if fire is detected
    return frame

# Function to detect accidents in the frame with confidence threshold
def detect_accident(frame):
    CONFIDENCE_THRESHOLD = 0.43  # Set the confidence threshold for accident detection

    results = accident_model(frame)
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            class_id = int(box.cls[0])
            
            if class_id == 0 and conf >= CONFIDENCE_THRESHOLD:  # Apply confidence threshold
                label = f"Accident {conf:.2f}"
                color = (0, 0, 255)  # Red for accident
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                
                send_accident_alert()  # Send alert if accident is detected
    return frame

# Function to preprocess the frame for YOLO model
def preprocess_frame(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

# Function to play video and detect both fire and accidents
def play_video():
    global cap
    ret, frame = cap.read()

    if ret:
        # Preprocess the frame for both models
        processed_frame = preprocess_frame(frame)

        # Detect fire and accidents in parallel
        with ThreadPoolExecutor() as executor:
            fire_future = executor.submit(detect_fire, frame)
            accident_future = executor.submit(detect_accident, frame)

            # Wait for both detections to complete
            frame = fire_future.result()
            frame = accident_future.result()

        # Convert frame to RGB and display on Tkinter
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        lbl_video.imgtk = imgtk
        lbl_video.configure(image=imgtk)

    lbl_video.after(10, play_video)

# Function to start video playback
def start_video():
    global cap
    video_path = filedialog.askopenfilename(title="Select Video", filetypes=[("Video Files", "*.mp4 *.avi *.mov")])
    
    if video_path:
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            messagebox.showerror("Error", "Unable to open video file.")
        else:
            play_video()

# Function to stop video playback
def stop_video():
    global cap
    if cap:
        cap.release()
        cap = None
        lbl_video.config(image='')  # Clear the video display

# Initialize Tkinter window
root = tk.Tk()
root.title("Fire and Accident Detection")
root.geometry("800x600")  # Set the window size

# Add a background image
bg_image = Image.open(r"E:\COLLEGE  AND OTHER DOCUMENTS\accident-identifier-and-alert.jpg")  # Replace with your background image path
bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
bg_image = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Create a custom style for buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)

# Create a frame for the video display
video_frame = ttk.Frame(root)
video_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Video display label
lbl_video = ttk.Label(video_frame)
lbl_video.pack(fill=tk.BOTH, expand=True)

# Create a frame for the buttons
button_frame = ttk.Frame(root)
button_frame.pack(fill=tk.X, padx=10, pady=10)

# Button to start video selection and playback
btn_start = ttk.Button(button_frame, text="Start Video", command=start_video)
btn_start.pack(side=tk.LEFT, padx=5, pady=5)

# Button to stop video playback
btn_stop = ttk.Button(button_frame, text="Stop Video", command=stop_video)
btn_stop.pack(side=tk.RIGHT, padx=5, pady=5)

# Run the Tkinter main loop
root.mainloop()