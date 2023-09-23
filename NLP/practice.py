from transformers import MarianTokenizer, MarianMTModel

# Initialize the tokenizer and model for the translation pair you want to use.
src_lang = 'en'
tgt_lang = 'in'
model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Input text to be translated
text_to_translate = "Translate this text to French."

# Tokenize the input text
input_ids = tokenizer.encode(text_to_translate, return_tensors="pt")

# Translate the text
with torch.no_grad():
    translation = model.generate(input_ids)

# Decode and print the translated text
translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
print(f"Original Text ({src_lang}): {text_to_translate}")
print(f"Translated Text ({tgt_lang}): {translated_text}")