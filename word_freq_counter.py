##Python programme for word frequency counter 

txt = input("Enter a string: ")
words = txt.split()

def word_freq_cntr(txt):
    freq = {}
    for i in words:
        if i in freq:
            freq[i] = freq[i] + 1
        else:
            freq[i] = 1
    return freq

if __name__ == "__main__":
    print(word_freq_cntr(txt))