# Transulation-tool

-------- Project Overview :

The Language Translation Tool is a beginner‑friendly web application that allows users to translate text between multiple languages. It combines a simple frontend interface with a Flask backend powered by the Google Translate API (googletrans library).
This project demonstrates how to:
Build a clean and interactive user interface with HTML, CSS, and JavaScript.
Connect the frontend to a Python backend using REST APIs.
Integrate external services (translation APIs) to process user input.
Handle JSON requests/responses between client and server.

-------- Features:

Text Input: Users can type any text they want to translate.
Language Selection: Dropdown menus to choose source and target languages (English, Telugu, Hindi, French, etc.).
Instant Translation: Translated text is displayed immediately after clicking the button.
Error Handling: Displays error messages if translation fails.
Optional Enhancements:
Copy translated text to clipboard.
Text‑to‑speech playback of translated text.

-------- Tech Stack :

Frontend: HTML, CSS, JavaScript
Backend: Python (Flask framework)
Translation API: Google Translate (googletrans library)
Optional Libraries: gTTS for text‑to‑speech

------- Project Structure :

translation-tool/
│── app.py          # Flask backend
│── templates/
│    └── index.html # Frontend UI

-------- How It Works :

Frontend (index.html)
   -> User enters text and selects source/target languages.
   -> JavaScript sends a POST request to the backend (/translate).

Backend (app.py)
  -> Flask receives the request and extracts text + language codes.
  -> googletrans processes the translation.
  -> Flask returns the translated text as JSON.
Frontend Output
JavaScript displays the translated text in the output area.
