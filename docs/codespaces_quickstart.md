# Codespaces 빠른 시작 안내

## 1. 템플릿으로 내 저장소 만들기

1. 선생님이 공유한 GitHub 템플릿 저장소에 들어갑니다.
2. `Use this template` 버튼을 누릅니다.
3. `Create a new repository`를 선택합니다.
4. 저장소 이름을 선생님 안내에 맞게 작성합니다.
5. `Create repository from template`를 누릅니다.

## 2. Codespace 열기

1. 내가 만든 저장소로 이동합니다.
2. 초록색 `Code` 버튼을 누릅니다.
3. `Codespaces` 탭을 선택합니다.
4. `Create codespace on main`을 누릅니다.
5. 브라우저에서 VS Code 화면이 열릴 때까지 기다립니다.

## 3. main.py 실행하기

터미널에서 다음 명령을 입력합니다.

```bash
python main.py
```

터미널이 보이지 않으면 상단 메뉴에서 다음을 선택합니다.

```text
Terminal → New Terminal
```

## 4. 파일 저장하기

파일을 수정한 뒤에는 다음을 누릅니다.

```text
Ctrl + S
```

## 5. GitHub에 반영하기

매 차시 끝에는 다음을 합니다.

```text
1. 왼쪽 Source Control 아이콘 클릭
2. 메시지 입력 예: 1차시 작업 완료
3. Commit 클릭
4. Sync Changes 클릭
```

터미널로 할 때는 다음 명령을 사용합니다.

```bash
git add .
git commit -m "class progress"
git push
```

## 6. Codespace 멈추기

수업이 끝나면 Codespace를 Stop 합니다.

```text
GitHub → Codespaces → 내 Codespace → Stop
```

브라우저 창만 닫으면 Codespace가 계속 켜져 있을 수 있습니다.

## 7. 최종 제출

선생님 안내에 따라 저장소 링크 또는 ZIP 파일을 제출합니다.

ZIP 파일 내려받기:

```text
GitHub 저장소 페이지 → Code → Download ZIP
```
