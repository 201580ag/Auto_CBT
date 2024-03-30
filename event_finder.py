import json

# 기능사 종목을 저장한 파일 경로
file_path = "./config/기능사 종목.json"
config_file_path = "./config/config.json"

# 사용자로부터 입력 받기
input_subject = input("검색할 기능사 종목을 입력하세요: ")

# 기능사 종목 검색
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)
    code = data.get(input_subject)

# 찾은 코드를 config.json 파일에 저장
if code:
    with open(config_file_path, "r", encoding="utf-8") as config_file:
        config_data = json.load(config_file)
        config_data["기능사 종목"] = code

    with open(config_file_path, "w", encoding="utf-8") as config_file:
        json.dump(config_data, config_file, indent=4, ensure_ascii=False)

    print(f"'{input_subject}'의 코드 '{code}'가 config.json 파일에 저장되었습니다.")
else:
    print(f"'{input_subject}'에 대한 정보를 찾을 수 없습니다.")
