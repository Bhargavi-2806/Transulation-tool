from deep_translator import GoogleTranslator

def translate_text(text, source_lang, target_lang):
    try:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"Error: {str(e)}"
    except Exception:
        return (" Please use language codes (e.g., en for English, te for Telugu). See README for full list.")


if __name__ == "__main__":
    text = input("Enter text to translate: ")
    source_lang = input("Enter source language code (e.g., en for English): ")
    target_lang = input("Enter target language code (e.g., fr for French): ")
    result = translate_text(text, source_lang, target_lang)
    print(f"Translated Text: {result}")
from flask import Flask, send_file, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def home():
    # Serve your frontend.html file
    return send_file("frontend.html")

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get("text")
    source_lang = data.get("sourceLang")
    target_lang = data.get("targetLang")

    try:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return jsonify({"translatedText": translated})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

