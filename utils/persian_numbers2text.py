import re


def number_to_persian(num):
    units = ["", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه"]
    teens = [
        "ده",
        "یازده",
        "دوازده",
        "سیزده",
        "چهارده",
        "پانزده",
        "شانزده",
        "هفده",
        "هجده",
        "نوزده",
    ]
    tens = ["", "", "بیست", "سی", "چهل", "پنجاه", "شصت", "هفتاد", "هشتاد", "نود"]
    hundreds = [
        "",
        "صد",
        "دویست",
        "سیصد",
        "چهارصد",
        "پانصد",
        "ششصد",
        "هفتصد",
        "هشتصد",
        "نهصد",
    ]

    def three_digit_to_words(n):
        result = []
        h = n // 100
        t = (n % 100) // 10
        u = n % 10

        if h:
            result.append(hundreds[h])
        if t == 1:
            result.append(teens[u])
        else:
            if t:
                result.append(tens[t])
            if u:
                result.append(units[u])

        return " و ".join(result)

    if num == 0:
        return "صفر"

    parts = []
    if num >= 1_000_000:
        millions = num // 1_000_000
        parts.append(number_to_persian(millions) + " میلیون")
        num %= 1_000_000
    if num >= 1_000:
        thousands = num // 1_000
        parts.append(number_to_persian(thousands) + " هزار")
        num %= 1_000
    if num > 0:
        parts.append(three_digit_to_words(num))

    return " و ".join(parts)


def decimal_to_persian_words(number):
    number = float(number)
    if int(number) == number:
        number = int(number)

    int_part = int(number)
    float_str = str(number)

    if "." in float_str:
        decimal_part = float_str.split(".")[1]
        decimal_length = len(decimal_part)
        decimal_value = int(decimal_part)

        powers = {
            1: "دهم",
            2: "صدم",
            3: "هزارم",
            4: "ده‌هزارم",
            5: "صد‌هزارم",
            6: "میلیونیم",
        }

        int_words = number_to_persian(int_part) if int_part != 0 else ""
        dec_words = number_to_persian(decimal_value)
        unit = powers.get(decimal_length, f"ده به توان منفی {decimal_length}")

        if int_words:
            return f"{int_words} و {dec_words} {unit}"
        else:
            return f"{dec_words} {unit}"
    else:
        return number_to_persian(int(number))


def replace_numbers_with_persian_words(text):
    def replacer(match):
        number_str = match.group()
        return decimal_to_persian_words(number_str)

    return re.sub(r"\d+(\.\d+)?", replacer, text)
