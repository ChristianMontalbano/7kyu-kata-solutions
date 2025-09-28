def proper_text(improper_text):
    words = improper_text.split()
    fixed = " ".join(words)
    lowercase = fixed.lower()
    final = lowercase.capitalize()
    return final

def main():
    bad_sentence = "WOW this is REALLY      Amazing"
    fixed_sentence = proper_text(bad_sentence)
    print(fixed_sentence)

main()