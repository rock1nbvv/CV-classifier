from word import words_model
import random

codebook = words_model.words_15
var01 = [list(codebook['word'].keys())[random.randrange(0, 4)] for _ in range(50)]
var02 = [list(codebook['word'].keys())[random.randrange(0, 4)] for _ in range(50)]
var03 = [list(codebook['word'].keys())[random.randrange(0, 4)] for _ in range(50)]
var04 = [list(codebook['word'].keys())[random.randrange(0, 4)] for _ in range(50)]
var05 = [list(codebook['word'].keys())[random.randrange(5, 10)] for _ in range(50)]
var06 = [list(codebook['word'].keys())[random.randrange(6, 10)] for _ in range(50)]
var07 = [list(codebook['word'].keys())[random.randrange(1, 4)] for _ in range(50)]
var08 = [list(codebook['word'].keys())[random.randrange(5, 8)] for _ in range(50)]
var09 = [list(codebook['word'].keys())[random.randrange(11, 15)] for _ in range(50)]
var10 = [list(codebook['word'].keys())[random.randrange(12, 15)] for _ in range(50)]
var11 = [list(codebook['word'].keys())[random.randrange(12, 15)] for _ in range(50)]
var12 = [list(codebook['word'].keys())[random.randrange(12, 15)] for _ in range(50)]

for i in range(50):
    print(var01[i] + "," + var02[i] + "," + var03[i] + "," + var04[i] + "," + var05[i] + "," + var06[i] + "," + var07[
        i] + "," + var08[i] + "," + var09[i] + "," + var10[i] + "," + var11[i] + "," + var12[i] + ",Developer")
print("")
