# Retinal Health Checker 🧑‍⚕️

This project is a web application that classifies retinal images as either **Healthy** or **Unhealthy** using a deep learning model. The model was trained on three datasets (FLoRI21, FIRE, and EyePACS) to detect retinal health. Built with Flask for the web interface, the app allows users to upload retinal images and receive instant health feedback.

## Table of Contents
1. [Features](#features)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Running the App](#running-the-app)

## Features
- Upload retinal images to classify as **Healthy** or **Unhealthy**.
- Real-time feedback based on a deep learning model.
- Simple and user-friendly interface built with Flask and Bootstrap.
- Based on image reconstruction loss (MSE) for determining retinal health.

## Technologies
- **Flask**: Web framework for building the application.
- **PyTorch**: For creating and training the deep learning model.
- **Torchvision**: For data transformations and image processing.
- **Bootstrap**: For the responsive web interface.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/retinal-health-checker.git
   cd retinal-health-checker
python -m venv venv

### Running the App
Explain how to run the application.

```markdown

## Running the App

1. Run the Flask app:
   ```bash
   flask run

Open a browser and navigate to http://127.0.0.1:5000/

Upload an image and get the retinal health classification.

### 7. **Model Overview**
Briefly explain how the model works.

```markdown
## Model Overview

The model is a **Convolutional Autoencoder (CAE)**, trained to reconstruct retinal images. The key insight is that healthy retinas can be reconstructed well, while unhealthy retinas lead to higher reconstruction loss (MSE). The model architecture consists of:

- **Encoder**: Extracts features using convolutional layers.
- **Decoder**: Reconstructs the image using transpose convolution layers.
