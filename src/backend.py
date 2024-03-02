import os
def define_map(init_path):
    let_map = {}
    Images = os.listdir(init_path)
    for i in Images:
        imgPath = init_path + '/' + i
        Letter = imgPath[-9]
        let_map[Letter] = imgPath
    return let_map
def translate_words(sentence):
    w_map = define_map('src/images')
    sentence_by_words = sentence.split(' ')
    for i in sentence_by_words:
        for j in i:
            capitalLetter = j.upper()
            if capitalLetter not in list(w_map.keys()):
                pass
            else:
                print(w_map[capitalLetter])

(translate_words('this is a test!'))