def search(text, pattern):
    pat_len = len(pattern)

    for i in range(len(text) - pat_len + 1):
        if text[i : pat_len + i] == pattern:
            print(f"Pattern found at index: {i}")


search("asasasas", "a")
