def match_found(regex, sentence: str) -> bool:
    return bool(regex.search(sentence))


def test_regex(regex, sentences):
    test_case = {}
    for line in sentences:
        print(line)
        sentence, valid = line.strip().split(",")
        test_case[sentence] = bool(valid)
    for sentence, valid in test_case.items():
        result = match_found(regex, sentence)
        assert result == valid
