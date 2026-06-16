# -------Transulation-tool------

## Project Overview :

The Language Translation Tool is a beginner‑friendly web application that allows users to translate text between multiple languages. It combines a simple frontend interface with a Flask backend powered by the Google Translate API (googletrans library).
This project demonstrates how to:
Build a clean and interactive user interface with HTML, CSS, and JavaScript.
Connect the frontend to a Python backend using REST APIs.
Integrate external services (translation APIs) to process user input.
Handle JSON requests/responses between client and server.

## Features:

Text Input: Users can type any text they want to translate.
Language Selection: Dropdown menus to choose source and target languages (English, Telugu, Hindi, French, etc.).
Instant Translation: Translated text is displayed immediately after clicking the button.
Error Handling: Displays error messages if translation fails.
Optional Enhancements:
Copy translated text to clipboard.
Text‑to‑speech playback of translated text.

## Tech Stack :

Frontend: HTML, CSS, JavaScript
Backend: Python (Flask framework)
Translation API: Google Translate (googletrans library)
Optional Libraries: gTTS for text‑to‑speech

##  Project Structure :

translation-tool/
│── app.py          # Flask backend
│── templates/
│    └── index.html # Frontend UI

## How It Works :

### Frontend (index.html)
   -> User enters text and selects source/target languages.
   -> JavaScript sends a POST request to the backend (/translate).

### Backend (app.py)
  -> Flask receives the request and extracts text + language codes.
  -> googletrans processes the translation.
  -> Flask returns the translated text as JSON.
Frontend Output
JavaScript displays the translated text in the output area.


 ## Supported Languages and Codes

When using this tool, enter the **language code** (short form), not the full name.  
Here’s the complete list supported by `deep-translator`:

| Language | Code |
|----------|------|
| Afrikaans | af |
| Albanian | sq |
| Amharic | am |
| Arabic | ar |
| Armenian | hy |
| Assamese | as |
| Aymara | ay |
| Azerbaijani | az |
| Bambara | bm |
| Basque | eu |
| Belarusian | be |
| Bengali | bn |
| Bhojpuri | bho |
| Bosnian | bs |
| Bulgarian | bg |
| Catalan | ca |
| Cebuano | ceb |
| Chichewa | ny |
| Chinese (Simplified) | zh-CN |
| Chinese (Traditional) | zh-TW |
| Corsican | co |
| Croatian | hr |
| Czech | cs |
| Danish | da |
| Dhivehi | dv |
| Dogri | doi |
| Dutch | nl |
| English | en |
| Esperanto | eo |
| Estonian | et |
| Ewe | ee |
| Filipino | tl |
| Finnish | fi |
| French | fr |
| Frisian | fy |
| Galician | gl |
| Georgian | ka |
| German | de |
| Greek | el |
| Guarani | gn |
| Gujarati | gu |
| Haitian Creole | ht |
| Hausa | ha |
| Hawaiian | haw |
| Hebrew | iw |
| Hindi | hi |
| Hmong | hmn |
| Hungarian | hu |
| Icelandic | is |
| Igbo | ig |
| Ilocano | ilo |
| Indonesian | id |
| Irish | ga |
| Italian | it |
| Japanese | ja |
| Javanese | jw |
| Kannada | kn |
| Kazakh | kk |
| Khmer | km |
| Kinyarwanda | rw |
| Konkani | gom |
| Korean | ko |
| Krio | kri |
| Kurdish (Kurmanji) | ku |
| Kurdish (Sorani) | ckb |
| Kyrgyz | ky |
| Lao | lo |
| Latin | la |
| Latvian | lv |
| Lingala | ln |
| Lithuanian | lt |
| Luganda | lg |
| Luxembourgish | lb |
| Macedonian | mk |
| Maithili | mai |
| Malagasy | mg |
| Malay | ms |
| Malayalam | ml |
| Maltese | mt |
| Maori | mi |
| Marathi | mr |
| Meiteilon (Manipuri) | mni-Mtei |
| Mizo | lus |
| Mongolian | mn |
| Myanmar | my |
| Nepali | ne |
| Norwegian | no |
| Odia (Oriya) | or |
| Oromo | om |
| Pashto | ps |
| Persian | fa |
| Polish | pl |
| Portuguese | pt |
| Punjabi | pa |
| Quechua | qu |
| Romanian | ro |
| Russian | ru |
| Samoan | sm |
| Sanskrit | sa |
| Scots Gaelic | gd |
| Sepedi | nso |
| Serbian | sr |
| Sesotho | st |
| Shona | sn |
| Sindhi | sd |
| Sinhala | si |
| Slovak | sk |
| Slovenian | sl |
| Somali | so |
| Spanish | es |
| Sundanese | su |
| Swahili | sw |
| Swedish | sv |
| Tajik | tg |
| Tamil | ta |
| Tatar | tt |
| Telugu | te |
| Thai | th |
| Tigrinya | ti |
| Tsonga | ts |
| Turkish | tr |
| Turkmen | tk |
| Twi | ak |
| Ukrainian | uk |
| Urdu | ur |
| Uyghur | ug |
| Uzbek | uz |
| Vietnamese | vi |
| Welsh | cy |
| Xhosa | xh |
| Yiddish | yi |
| Yoruba | yo |
| Zulu | zu |


## Example Run :

Enter text to translate: hii this is a translation tool
Enter source language code (e.g., en for English): en
Enter target language code (e.g., te for Telugu): te
Translated Text: హాయ్ ఇది ఒక అనువాద సాధనం
