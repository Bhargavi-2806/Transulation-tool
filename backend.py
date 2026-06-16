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
