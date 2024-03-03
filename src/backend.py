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
    imgpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')
    w_map = define_map(imgpath)
    sentence_by_words = sentence.strip().split(' ')
    print(len(sentence_by_words))
    counter_1 = 0
    arr = []
    for k in range(len(sentence_by_words)):
        arr.append([])
    print(arr)
    for i in sentence_by_words:
        arr[counter_1] = []
        for j in i:
            print(counter_1)
            capitalLetter = j.upper()
            if capitalLetter not in list(w_map.keys()):
                pass
            else:
                arr[counter_1].append((i, w_map[capitalLetter]))
        counter_1 += 1
    print(arr)
    return arr
