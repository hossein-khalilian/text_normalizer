import re

from .utils.persian_numbers2text import replace_numbers_with_persian_words

replacements = {
    "أ": "ا",
    "إ": "ا",
    "آ": "آ",
    "ٱ": "ا",
    "ء": "",
    "ؤ": "و",
    "ى": "ی",
    "ي": "ی",
    "ة": "ه",
    "ۀ": "ه",
    "ۆ": "و",
    "ڵ": "ل",
    "ێ": "ی",
    "ە": "ه",
    "ڤ": "و",
    "\u200d": "\u200c",
    "\u200e": "\u200c",
    "\u200f": "\u200c",
    "\ufeff": "\u200c",
}


def persian_normalizer(text):
    for src, dest in replacements.items():
        text = text.replace(src, dest)

    allowed_pattern = re.compile(
        r"[^"
        r"ئآابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"
        r"a-zA-Z"
        r"0-9۰-۹"
        r'.,:!?\'"()\[\]{}\-–—'
        r"٪،؛«»؟%&+=/"
        r"\s\u200c"
        r"]"
    )
    text = allowed_pattern.sub("", text)
    text = re.sub(r"[ ]{2,}", " ", text)
    text = re.sub(r"[\u200c]{2,}", "\u200c", text)

    persian_digits = "۰۱۲۳۴۵۶۷۸۹"
    english_digits = "0123456789"
    for pd, ed in zip(persian_digits, english_digits):
        text = text.replace(pd, ed)

    text = text.strip()

    return text.strip()


def persian_normalizer_no_punc(text):

    for src, dest in replacements.items():
        text = text.replace(src, dest)

    allowed_pattern = re.compile(
        r"[^" r"ئآابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی" r"a-zA-Z" r"0-9۰-۹" r"\s\u200c" r"]"
    )
    text = allowed_pattern.sub("", text)
    text = re.sub(r"[ ]{2,}", " ", text)
    text = re.sub(r"[\u200c]{2,}", "\u200c", text)

    persian_digits = "۰۱۲۳۴۵۶۷۸۹"
    english_digits = "0123456789"
    for pd, ed in zip(persian_digits, english_digits):
        text = text.replace(pd, ed)

    return text.strip()


def persian_normalizer_no_punc_with_digit_replacement(text):

    for src, dest in replacements.items():
        text = text.replace(src, dest)

    allowed_pattern = re.compile(
        r"[^"
        r"ئآابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"
        r"a-zA-Z"
        r"0-9۰-۹"
        r"\s"
        r"\u200c"
        r"]"
    )
    text = allowed_pattern.sub("", text)
    text = re.sub(r"[ ]{2,}", " ", text)
    text = re.sub(r"[\u200c]{2,}", "\u200c", text)
    text = replace_numbers_with_persian_words(text)

    return text.strip()


def persian_normalizer_no_punc_no_digit(text):

    for src, dest in replacements.items():
        text = text.replace(src, dest)

    allowed_pattern = re.compile(
        r"[^" r"ئآابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی" r"a-zA-Z" r"\s" r"\u200c" r"]"
    )
    text = allowed_pattern.sub("", text)
    text = re.sub(r"[ ]{2,}", " ", text)

    return text.strip()


def normalize_persian_halfspace(text):
    zwnj = "\u200c"

    # Rule 1: می + verb
    text = re.sub(r"\bمی(?=[\u0600-\u06FF]{2,})", f"می{zwnj}", text)

    # Rule 2: نمی + verb
    text = re.sub(r"\bنمی(?=[\u0600-\u06FF]{2,})", f"نمی{zwnj}", text)

    # Rule 3: noun + ها (plural)
    text = re.sub(r"(?<=[\u0600-\u06FF])ها\b", f"{zwnj}ها", text)
    text = re.sub(r"(?<=[\u0600-\u06FF])های\b", f"{zwnj}های", text)

    # Rule 4: noun/adjective + ی (sometimes compound forms)
    text = re.sub(r"(?<=[\u0600-\u06FF])یی\b", f"{zwnj}یی", text)

    # Rule 5: avoid double ZWNJ if already there
    text = re.sub(f"{zwnj}+", zwnj, text)

    text = re.sub(r"(?<=[\u0600-\u06FF])ه(?=ی\b)", f"ه{zwnj}", text)

    return text
