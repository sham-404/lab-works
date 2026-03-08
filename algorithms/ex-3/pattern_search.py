def pattern_search(text, pattern):
    pat_len = len(pattern)

    for i in range(len(text) - pat_len + 1):
        if text[i: pat_len + i] == pattern:
            return i
    
    return -1

text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

idx = pattern_search(text, pattern)
print(f"Pattern found at idx {idx}" if idx != -1 else "Pattern not found")
