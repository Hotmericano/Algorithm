"""
풀이 폴더를 훑어서 README.md의 풀이 목록을 자동으로 만든다.

폴더 구조:
    프로그래머스/<레벨>/<문제번호>. <제목>/<풀이 파일>     예) 프로그래머스/Lv1/12940. 최대공약수와 최소공배수/solution.py
    백준/<티어>/<문제번호>. <제목>/<풀이 파일>             (2026년 4월 서비스 종료, 기존 풀이 보관용)

문제 폴더에 README.md가 있고 그 안에 "### 분류" 아래 한 줄이 있으면 분류 칸에 표시한다. (없어도 됨)
README.md의 AUTO-START ~ AUTO-END 사이만 새로 쓰고, 나머지 부분은 그대로 둔다.
"""

import re
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

START = "<!-- AUTO-START -->"
END = "<!-- AUTO-END -->"

LANGUAGES = {
    ".py": "Python", ".c": "C", ".cpp": "C++", ".java": "Java",
    ".js": "JavaScript", ".kt": "Kotlin", ".sql": "SQL",
}

# 백준 티어
BOJ_TIERS = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Ruby"]
BOJ_LEVELS = ["V", "IV", "III", "II", "I"]
BOJ_EMOJI = {
    "Bronze": "🟤", "Silver": "⚪", "Gold": "🟡",
    "Platinum": "🟢", "Diamond": "🔵", "Ruby": "🔴",
}


def nfc(text):
    """맥에서 올라온 한글(자모 분리)을 일반 한글로 합친다."""
    return unicodedata.normalize("NFC", text)


def clean(text):
    """폴더 이름에 들어간 특수 공백(BaekjoonHub의 U+2005 등)을 일반 공백으로 바꾼다."""
    return re.sub(r"\s+", " ", text).strip()


def read_problem(folder):
    """문제 폴더 하나에서 공통 정보를 뽑는다. 풀이 파일이 없으면 None."""
    match = re.match(r"(\d+)\.\s*(.+)", nfc(folder.name))
    if not match:
        return None

    codes = [f for f in folder.iterdir() if f.suffix in LANGUAGES]
    if not codes:
        return None

    text = ""
    readme = folder / "README.md"
    if readme.exists():
        text = nfc(readme.read_text(encoding="utf-8"))
    tag_match = re.search(r"### 분류\s*\n+(.+)", text)

    return {
        "number": int(match.group(1)),
        "title": clean(match.group(2)),
        "group": nfc(folder.parent.name),  # Lv1, Silver 등
        "tags": tag_match.group(1).strip() if tag_match else "",
        "language": ", ".join(sorted({LANGUAGES[f.suffix] for f in codes})),
        "path": quote(nfc(folder.relative_to(ROOT).as_posix())),
        "readme": text,
    }


def collect(platform_dir):
    problems = []
    for folder in sorted((ROOT / platform_dir).glob("*/*")):
        if folder.is_dir():
            problem = read_problem(folder)
            if problem:
                problems.append(problem)
    return problems


# ===== 프로그래머스 =====
def level_number(group):
    """'Lv1', 'Lv. 1', 'lv1' → 1"""
    m = re.search(r"(\d+)", group)
    return int(m.group(1)) if m else -1


def programmers_section(problems):
    lines = ["## 💻 프로그래머스", ""]
    if not problems:
        return lines + ["아직 푼 문제가 없어요.", ""]

    counts = Counter(level_number(p["group"]) for p in problems)
    summary = " · ".join(f"Lv.{lv} {counts[lv]}문제" for lv in sorted(counts, reverse=True))
    lines += [
        f"총 **{len(problems)}문제** ({summary})",
        "",
        "| 레벨 | 번호 | 제목 | 분류 | 언어 | 풀이 |",
        "|---|---|---|---|---|---|",
    ]
    problems.sort(key=lambda p: (-level_number(p["group"]), p["number"]))
    for p in problems:
        url = f"https://school.programmers.co.kr/learn/courses/30/lessons/{p['number']}"
        lines.append(
            f"| Lv.{level_number(p['group'])} | [{p['number']}]({url}) | {p['title']} "
            f"| {p['tags']} | {p['language']} | [보기]({p['path']}) |"
        )
    return lines + [""]


# ===== 백준 (보관용) =====
def boj_tier(problem):
    """BaekjoonHub README의 [Silver II] 같은 표시에서 티어와 단계를 읽는다."""
    head = re.search(r"\[(\w+)\s+(I{1,3}|IV|V)\]", problem["readme"])
    if head:
        return head.group(1), head.group(2)
    return problem["group"], ""


def boj_rank(problem):
    tier, level = boj_tier(problem)
    t = BOJ_TIERS.index(tier) if tier in BOJ_TIERS else -1
    lv = BOJ_LEVELS.index(level) if level in BOJ_LEVELS else -1
    return t * 10 + lv


def boj_section(problems):
    if not problems:
        return []

    counts = Counter(boj_tier(p)[0] for p in problems)
    summary = " · ".join(
        f"{BOJ_EMOJI[t]} {t} {counts[t]}" for t in reversed(BOJ_TIERS) if counts[t]
    )
    lines = [
        "## 📦 백준 (보관)",
        "",
        "> 백준 온라인 저지는 2026년 4월 서비스를 종료해서 문제 링크는 걸지 않았어요.",
        "",
        f"총 **{len(problems)}문제** ({summary})",
        "",
        "<details>",
        "<summary>목록 펼치기</summary>",
        "",
        "| 티어 | 번호 | 제목 | 분류 | 언어 | 풀이 |",
        "|---|---|---|---|---|---|",
    ]
    problems.sort(key=lambda p: (-boj_rank(p), p["number"]))
    for p in problems:
        tier, level = boj_tier(p)
        label = f"{BOJ_EMOJI.get(tier, '')} {tier} {level}".strip()
        lines.append(
            f"| {label} | {p['number']} | {p['title']} | {p['tags']} "
            f"| {p['language']} | [보기]({p['path']}) |"
        )
    return lines + ["", "</details>", ""]


def main():
    programmers = collect("프로그래머스")
    boj = collect("백준")

    body = programmers_section(programmers) + boj_section(boj)
    generated = START + "\n" + "\n".join(body).rstrip() + "\n" + END

    old = README.read_text(encoding="utf-8") if README.exists() else "# Algorithm\n"
    if START in old and END in old:
        new = old.split(START)[0] + generated + old.split(END)[1]
    else:
        new = old.rstrip() + "\n\n" + generated + "\n"

    README.write_text(new, encoding="utf-8")
    print(f"README 갱신 완료: 프로그래머스 {len(programmers)}문제, 백준 {len(boj)}문제")


if __name__ == "__main__":
    main()