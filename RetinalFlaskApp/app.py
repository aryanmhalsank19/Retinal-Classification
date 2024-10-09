import os
import torch
from flask import Flask, request, render_template, redirect, url_for, flash
from PIL import Image
from torchvision import transforms

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'  # Save uploads in the static folder for accessibility
app.secret_key = 'your_secret_key'  # Required for flash messages

# Ensure the static/uploads folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Check if MPS (Apple Silicon), GPU, or CPU is available
device = torch.device("mps" if torch.backends.mps.is_available() else ("cuda" if torch.cuda.is_available() else "cpu"))

# Define the model architecture
class RetinalImageModel(torch.nn.Module):
    def __init__(self):
        super(RetinalImageModel, self).__init__()
        self.encoder = torch.nn.Sequential(
            torch.nn.Conv2d(1, 32, kernel_size=3, padding=1),
            torch.nn.BatchNorm2d(32),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2),
            torch.nn.Conv2d(32, 64, kernel_size=3, padding=1),
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2),
            torch.nn.Dropout(0.25)
        )
        self.decoder = torch.nn.Sequential(
            torch.nn.ConvTranspose2d(64, 32, kernel_size=2, stride=2),
            torch.nn.BatchNorm2d(32),
            torch.nn.ReLU(),
            torch.nn.ConvTranspose2d(32, 1, kernel_size=2, stride=2),
            torch.nn.Sigmoid()
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

# Load the model checkpoint
model = RetinalImageModel().to(device)
model.load_state_dict(torch.load('retinal_image_model.pkl', map_location=device))
model.eval()  # Set the model to evaluation mode

# Image transformation
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Grayscale()
])

# Function to make predictions (whether the retina is healthy or not)
def predict_retina_health(image):
    image = transform(image).unsqueeze(0).to(device)  # Add batch dimension and move to device
    with torch.no_grad():
        output = model(image)
    # Simple heuristic: healthy if reconstruction loss is below a threshold
    threshold = 0.05
    loss_fn = torch.nn.MSELoss()
    loss = loss_fn(output, image)
    return "Healthy Retina" if loss < threshold else "Unhealthy Retina"

# Route to display the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle image uploads and classification
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        # Save the uploaded file in the static/uploads folder
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Open the image
        image = Image.open(filepath)

        # Make a prediction using the model
        result = predict_retina_health(image)

        # Render the result page with prediction
        return render_template('result.html', result=result, image_url=url_for('static', filename=f'uploads/{filename}'))
    
    else:
        flash('Invalid file type. Please upload a valid image.')
        return redirect(request.url)

# Helper function to validate file type
def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
