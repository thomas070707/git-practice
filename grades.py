# gradebook v1.0 — 1주차 실습 완료
SUBJECTS = ["국어", "영어", "수학", "과학탐구"]

# file_io.py
# 점수를 파일로 저장하고 불러오는 모듈

import os

DATA_FILE = "data/scores.txt"


def save_scores(scores):
    """점수 딕셔너리를 파일에 저장한다."""
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for subject, score in scores.items():
            f.write(f"{subject},{score}\n")
    print(f"점수가 {DATA_FILE}에 저장되었습니다.")


def load_scores():
    """파일에서 점수를 불러와 딕셔너리로 반환한다."""
    if not os.path.exists(DATA_FILE):
        print("저장된 점수 파일이 없습니다.")
        return {}
    scores = {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            subject, score = line.strip().split(",")
            scores[subject] = float(score)
    return scores

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