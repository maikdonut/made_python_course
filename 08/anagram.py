"256 возможных символов ASCII"
M = 256


def compare(text: list, pattern: list, length: int = M):
    "Сравнение списков по значениям"
    for i in range(length):
        if text[i] != pattern[i]:
            return False
    return True


def find_anagrams(text: str, pattern: str):
    "Нахождение всех позиций анаграммы pattern в строке text"
    t_len = len(text)
    p_len = len(pattern)
    cnt_text = [0] * M
    cnt_pat = [0] * M
    res = []
    for i in range(p_len):
        cnt_text[ord(text[i])] += 1
        cnt_pat[ord(pattern[i])] += 1
    for i in range(p_len, t_len):
        if compare(cnt_text, cnt_pat):
            res.append(i - p_len)
        cnt_text[ord(text[i])] += 1
        cnt_text[ord(text[i - p_len])] -= 1
    if compare(cnt_text, cnt_pat):
        res.append(t_len - p_len)
    return res
