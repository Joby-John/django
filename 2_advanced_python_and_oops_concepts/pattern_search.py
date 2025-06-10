
def patternFinder(txt, pat):
    patIndex = txt.find(pat)

    while(patIndex >= 0):
        print(patIndex)
        patIndex = txt.find(pat, patIndex+1)


if __name__ == "__main__":
    patternFinder("AAAAA", "AAA")
