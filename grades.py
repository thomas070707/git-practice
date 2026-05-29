# gradebook v1.1 — 2주차 실습 시작
SUBJECTS = ["국어", "영어", "수학", "과학탐구"]

# converter.py
# 점수를 학점으로 변환하는 모듈

GRADE_SCALE = [
    (95, "A+"), (90, "A"),  (85, "B+"),
    (80, "B"),  (75, "C+"), (70, "C"),
    (65, "D+"), (60, "D"),  (0,  "F")
]


def convert_to_grade(score):
    """점수를 학점 문자열로 변환한다."""
    for threshold, grade in GRADE_SCALE:
        if score >= threshold:
            return grade
    return "F"


def print_grades(scores):
    """각 과목의 학점을 출력한다."""
    print("\n" + "=" * 30)
    print("       학점 결과")
    print("=" * 30)
    for subject, score in scores.items():
        grade = convert_to_grade(score)
        print(f"  {subject:<10} {score:>5.1f}점  {grade}")
    print("=" * 30)


def get_scores():
    """4개 과목의 점수를 입력받아 딕셔너리로 반환한다."""
    scores = {}
    print("과목별 점수를 입력하세요 (0~100).\n")

    for subject in SUBJECTS:
        while True:
            try:
                score = float(input(f"{subject} 점수: "))
                if 0 <= score <= 100:
                    scores[subject] = score
                    break
                else:
                    print("  → 0에서 100 사이의 점수를 입력하세요.")
            except ValueError:
                print("  → 숫자를 입력하세요.")

    return scores

def calculate_average(scores):
    """점수 딕셔너리를 받아 평균을 반환한다."""
    if not scores:
        return 0.0
    return sum(scores.values()) / len(scores)

def print_result(scores, average):
    """점수와 평균을 보기 좋게 출력한다."""
    print("\n" + "=" * 30)
    print("       성적 결과")
    print("=" * 30)
    for subject in SUBJECTS:
        print(f"  {subject:<10} {scores[subject]:>6.1f}점")
    print("-" * 30)
    print(f"  {'평균':<10} {average:>6.1f}점")
    print("=" * 30)


def find_highest_lowest(scores):
    """최고점과 최저점 과목을 반환한다."""
    highest = max(SUBJECTS, key=lambda s: scores[s])
    lowest  = min(SUBJECTS, key=lambda s: scores[s])
    return highest, lowest

if __name__ == "__main__":
    scores = get_scores()
    average = calculate_average(scores)
    print_result(scores, average)

    highest, lowest = find_highest_lowest(scores)
    print(f"\n최고점: {highest} ({scores[highest]:.1f}점)")
    print(f"최저점: {lowest} ({scores[lowest]:.1f}점)")