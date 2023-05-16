import translators as ts


def translator(content_list, default_language="fr", translate_lanuage="en"):
    # translated_dict={item:ts.translate_text(item,from_language=default_language,to_language=translate_lanuage) for item in content_list}
    translated_dict = {}
    for item in content_list:
        translated_dict[item] = ts.translate_text(item, from_language=default_language, to_language=translate_lanuage)
    return translated_dict


french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
print(translator(french_words))
print(translator(french_words, translate_lanuage="ja"))
