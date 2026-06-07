# 자주 생기는 오류와 해결법

## 1. input()으로 받은 값이 숫자로 계산되지 않아요

`input()`으로 받은 값은 문자열입니다. 숫자로 계산하려면 `int()`를 사용하세요.

```python
age = int(input("나이 입력: "))
```

## 2. IndentationError가 나요

들여쓰기가 맞지 않는 오류입니다. if, for, def 다음 줄은 들여쓰기해야 합니다.

```python
if score >= 60:
    print("PASS")
```

## 3. 리스트 인덱스 오류가 나요

리스트 인덱스는 0부터 시작합니다.

```python
items = ["a", "b", "c"]
print(items[0])  # a
print(items[2])  # c
```

## 4. 함수가 실행되지 않아요

함수는 정의만 해서는 실행되지 않습니다. 반드시 호출해야 합니다.

```python
def hello():
    print("안녕")

hello()
```

## 5. return과 print가 헷갈려요

`print()`는 화면에 출력합니다. `return`은 함수 밖으로 값을 돌려줍니다.

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)
```

## 6. main.py가 실행되지 않아요

터미널 위치와 파일 이름을 확인하세요.

```bash
python main.py
```

## 7. 수정한 내용이 GitHub 저장소에 안 보여요

Commit과 Sync를 했는지 확인하세요.

```text
Ctrl + S → Commit → Sync Changes
```
