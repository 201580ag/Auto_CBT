import json
import base64
from getpass import getpass

def encrypt_password(password):
    encrypted_password = base64.b64encode(password.encode()).decode()
    return encrypted_password

def main():
    # 사용자로부터 비밀번호 입력 받기
    password = getpass("비밀번호를 입력하세요(입력시 비밀번호 안 보임): ")

    # 비밀번호를 암호화
    encrypted_password = encrypt_password(password)

    # JSON 파일 업데이트
    with open('./config/config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
        config['비밀번호'] = encrypted_password

    with open('./config/config.json', 'w', encoding='utf-8') as file:
        json.dump(config, file, indent=4, ensure_ascii=False)

    print("비밀번호가 성공적으로 저장되었습니다.")

if __name__ == "__main__":
    main()
