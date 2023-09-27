text = input("Enter Text:")

def main():
    sentences = 0
    words = 1
    letters = 0
    text_len = len(text)
    
    for i in range(text_len):
        if text[i] == ' ':
            words += 1
        elif text[i] == '.' or text[i] == '!' or text[i] == '?':
            sentences += 1
        elif (text[i] >= chr(64) and text[i] <= chr(90)
            or text[i] >= chr(96) and text[i] <= chr(123)):
                letters += 1

    l = float(av_letters(letters, words))
    s = float(av_sentences(sentences, words))
    index = float(formula(l, s))
    
    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print("Grade {}".format(int(round(index))))
                

def av_letters(letters, words):
    return float(letters) / float(words) * 100.0

def av_sentences(sentences, words):
    return float(sentences) / float(words) * 100.0

def formula(letters, sentences):
    return 0.0588 * float(letters) - 0.295 * float(sentences) - 15.8

main()
