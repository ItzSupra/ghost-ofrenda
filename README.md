# The Living Ofrenda: Local Memory Vault

**Description**
An air-gapped, multimodal memory vault built for the Hacktoberfest Ghost in the Machine Challenge. 

The Living Ofrenda is a completely private, offline web application where users can place a photo of a departed loved one, share a cherished memory, and receive a customized, poetic celebration of life. It runs entirely locally on consumer hardware (tested on an AMD Ryzen 5 5600G with no discrete GPU).

## Features
* **Zero Cloud APIs:** Memories and family photos never leave your hard drive. 
* **Multimodal Vision:** Uses the Moondream model to look at uploaded photos and understand their context locally.
* **Offline Text Processing:** Uses the Llama 3.2 model to weave traditional, respectful Dia de los Muertos poetry.
* **CSS and Vector Art:** Features native, flickering SVG candles and CSS-aged Polaroid effects without needing external image files.

## Dependencies
This project requires Python and the following packages:
* streamlit (version 1.39.0 or higher)
* ollama (version 0.3.3 or higher)
* Pillow (version 11.0.0 or higher)

You will also need the Ollama software installed on your machine to serve the local models.

## How to Run the Application

### 1. Install Prerequisites
You must have Python and Ollama installed on your system.

### 2. Pull the Local Models
Open your terminal and download the required lightweight models into Ollama:
```bash
ollama run llama3.2:3b
ollama run moondream

```

Type `/bye` to exit the Ollama prompt after each model finishes downloading.

### 3. Install Python Dependencies

Clone this repository to your computer, open your terminal inside the folder, and install the required libraries:

```bash
pip install -r requirements.txt

```

### 4. Start the Application

Run this command in your terminal:

```bash
streamlit run app.py

```

The application will open in your browser at `http://localhost:8501`. You can now disconnect from the internet to test its air-gapped capabilities.

## How to Use the Altar

1. **Approach the Altar:** Once the application is running in your terminal, open your web browser and navigate to `http://localhost:8501`.
2. **Name the Departed:** On the left side of the screen under "The Memory", type the name of the person you wish to honor in the first text box.
3. **Leave an Offering:** In the second box, type out physical offerings they would appreciate, such as a favorite meal, a specific flower, or a beloved song.
4. **Share a Story:** In the larger text area, write a specific, cherished memory you hold of them.
5. **Place a Photograph:** Click the file uploader to select an image of your loved one. As soon as it uploads, the application will automatically apply a vintage sepia filter and frame it like an aged Polaroid resting on the screen.
6. **Light the Candle:** Click the purple "Light the Candle" button on the right side of the screen.
7. **Read the Tribute:** Wait a few moments while the local models securely process the image and your written words. A custom, poetic celebration of their life will appear on the right side, styled as a physical parchment letter.

## Why Open Innovation Matters Here

A closed API approach would fundamentally break the trust required for an application dealing with grief and memory. By utilizing optimized open-weight models, we ensure absolute data sovereignty. No intimate photos or family stories are sent to corporate servers to be logged or used for future data harvesting. Furthermore, because the application runs locally, this memorial tool is permanent. It will continue to function years from now regardless of whether a service provider deprecates an endpoint.
