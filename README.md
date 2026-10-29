# The Living Ofrenda: Local Memory Vault

An air-gapped, multimodal memory vault built for the Hacktoberfest Ghost in the Machine Challenge. 

The Living Ofrenda is a completely private, offline web application where users can place a photo of a departed loved one, share a cherished memory, and receive a customized, poetic celebration of life. 

It runs entirely locally on consumer hardware (tested on an AMD Ryzen 5 5600G with no discrete GPU).

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


### 3. Install Python Dependencies
Clone this repository to your computer, open your terminal inside the folder, and install the required libraries:
```bash
pip install -r requirements.txt
