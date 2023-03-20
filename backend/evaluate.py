import numpy as np

import words_model, lwa, word


def get_grade(grades):
    codebook = words_model.words_15
    W = []  # how many times each word is used
    for item in codebook['word'].keys():
        W.append(grades.count(item))  # count list W

    print(grades)
    print(W)

    h = min(
        item['lmf'][-1] for item in codebook['word'].values())  # take minimal from all last elements for each grade
    m = 50  # max grade in variable
    intervals_umf = lwa.alpha_cuts_intervals(m)  # upper membership function
    intervals_lmf = lwa.alpha_cuts_intervals(m, h)  # lower membership function

    res_y_umf = lwa.y_umf(intervals_umf, codebook, W)
    res_y_lmf = lwa.y_lmf(intervals_lmf, codebook, W)

    res_word = lwa.constract_dit2fs(np.arange(*codebook['x']), intervals_lmf, res_y_lmf, intervals_umf, res_y_umf)
    # res_word.plot()

    sm = []
    for title, fou in codebook['word'].items():
        sm.append((
            title,
            res_word.similarity_measure(word.Word(None, codebook['x'], fou['lmf'], fou['umf']))
        ))

    return max(sm, key=lambda item: item[1])
