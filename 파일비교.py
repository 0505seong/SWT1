import os
import hashlib

# ── 입력 ──────────────────────────────────────
dir1_name = input("첫 번째 디렉토리 이름: ")
dir2_name = input("두 번째 디렉토리 이름: ")

current_dir = os.getcwd()
dir1_path = os.path.join(current_dir, dir1_name)
dir2_path = os.path.join(current_dir, dir2_name)

if not os.path.isdir(dir1_path) or not os.path.isdir(dir2_path):
    print("오류: 디렉토리를 찾을 수 없습니다.")
    exit(1)

# ── os.scandir()로 파일 정보 수집 ─────────────
# DirEntry 객체를 {이름: entry} 딕셔너리로 저장
# entry.is_file() : 파일만 걸러내기
def scan_files(path):
    """
    scandir()로 디렉토리를 읽어
    { 파일이름: DirEntry객체 } 형태의 딕셔너리를 반환
    """
    result = {}
    for entry in os.scandir(path):      # DirEntry를 하나씩 순회
        if entry.is_file():             # 파일인 항목만 선택
            result[entry.name] = entry  # 이름을 키로 저장
    return result

files1 = scan_files(dir1_path)  # {'a.txt': <DirEntry>, 'b.txt': <DirEntry>, ...}
files2 = scan_files(dir2_path)

# ── 집합(set)으로 파일 이름 비교 ──────────────
names1 = set(files1.keys())   # 딕셔너리의 키(파일명)들을 집합으로 변환
names2 = set(files2.keys())

only_in_1 = names1 - names2   # dir1에만 있는 파일
only_in_2 = names2 - names1   # dir2에만 있는 파일
common    = names1 & names2   # 양쪽 모두 있는 파일

print(f"\n[{dir1_name}] 파일 수: {len(names1)}개")
print(f"[{dir2_name}] 파일 수: {len(names2)}개")

# ── 파일 수가 다를 경우 ────────────────────────
if only_in_1 or only_in_2:
    if only_in_1:
        print(f"\n⚠️  '{dir1_name}'에만 있는 파일: {only_in_1}")
    if only_in_2:
        print(f"⚠️  '{dir2_name}'에만 있는 파일: {only_in_2}")
    exit(1)

print(f"✅ 두 디렉토리 모두 {len(common)}개의 파일 확인. 비교 시작...\n")

# ── 파일 내용 해시 함수 ────────────────────────
def get_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

# ── 이름·크기·내용 비교 ───────────────────────
all_match = True

for name in sorted(common):          # 공통 파일을 이름순으로 순회
    e1 = files1[name]                # DirEntry 객체
    e2 = files2[name]

    # entry.stat() : stat_result 반환 (os.stat() 호출 없이 바로 사용)
    size1 = e1.stat().st_size        # st_size : 파일 크기(바이트)
    size2 = e2.stat().st_size

    size_match   = (size1 == size2)
    content_match = get_hash(e1.path) == get_hash(e2.path)  # e1.path : 전체 경로

    status = "✅ 완전 일치" if (size_match and content_match) else "❌ 차이 있음"
    print(f"[{name}] {status}")
    print(f"  크기: {size1}B vs {size2}B → {'같음' if size_match else '다름'}")
    print(f"  내용: {'같음' if content_match else '다름'}\n")

    if not (size_match and content_match):
        all_match = False

# ── 최종 요약 ─────────────────────────────────
print("══════════════════════════════════")
print("✅ 모든 파일 완전 동일!" if all_match else "❌ 차이 있는 파일 존재!")
print("══════════════════════════════════")