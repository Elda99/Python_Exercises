def shkr_medha(stringa):
    shkr_medha = 0
    for shkronja in stringa[0:4]:
        if shkronja.upper() == shkronja:
            shkr_medha += 1
    if shkr_medha >= 2:
        return stringa.upper()
    return stringa
print(shkr_medha('Program'))
print(shkr_medha('ProgRam'))
print(shkr_medha('PrOgram'))