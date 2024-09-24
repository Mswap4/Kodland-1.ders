meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "GHOST": "Yok olmak",
            "CAP": "Yalan olan şeyler",
            "FAKE": "sahte"
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")


if word in meme_dict.keys():
    print(meme_dict[word])
    # Kelime eşleşiyorsa ne yapmalıyız?
else:
    print("kellime sözlükle bulunmuyor")
    # Kelime eşleşmiyorsa ne yapmalıyız?
