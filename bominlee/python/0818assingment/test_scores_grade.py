## testcase first


def test_scores_grade():
    assert scores_grade([{'국어': 100}], '국어') == "A"
    assert scores_grade([{'국어': 20, '영어': 50, '수학': 70}], '영어') == "C"
    assert scores_grade([{'국어': 65, '영어': 50, '수학': 10}], '국어') == "C"
    assert scores_grade([{'국어': 20, '영어': 50, '수학': 40}], '수학') == "D" ## 문제 이상해. 20초과면 D학점이겠지???
