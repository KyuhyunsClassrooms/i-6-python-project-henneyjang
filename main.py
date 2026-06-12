# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 
# 프로젝트 주제: 

import random  # 랜덤으로 적을 뽑기 위해 필요한 모듈

# ==========================================
# 1. 데이터 구조 설계 (2차원 리스트)
# ==========================================
# 몬스터 데이터: [이름, 체력, 공격력]
monsters = [
    ["네이버", "30", "10"],
    ["구글", "60", "15"],
    ["은하수를 여행하는 히치하이커를 위한 안내서", "120", "100"]
]

# 퀴즈 데이터: [질문, 선택지1, 선택지2, 선택지3, 정답 번호]
# 전투가 이어질 수 있도록 문제를 충분히 많이 준비했습니다.
quiz_pool = [
    ["대한민국의 수도는 어디일까요?", "1. 부산", "2. 서울", "3. 인천", "2", "정답입니다!","
    ["파이썬에서 출력을 할 때 사용하는 함수는?", "1. input()", "2. print()", "3. type()", "2"],
    ["다음 중 숫자가 아닌 자료형은?", "1. 문자열(str)", "2. 정수(int)", "3. 실수(float)", "1"],
    ["반복문을 중간에 멈추게 하는 키워드는?", "1. continue", "2. pass", "3. break", "3"],
    ["조건을 비교할 때 사용하는 제어문은?", "1. for", "2. if", "3. while", "2"],
    ["리스트에 요소를 맨 뒤에 추가하는 함수는?", "1. pop()", "2. insert()", "3. append()", "3"]
]

# ==========================================
# 2. 함수 정의 (기능별 분리)
# ==========================================
def show_status(p_name, p_hp, m_name, m_hp):
    """현재 플레이어와 몬스터의 HP 상태를 보여주는 함수"""
    print("\n" + "=" * 40)
    print(f"🤠 {p_name}의 HP: {p_hp}")
    print(f"👾 {m_name}의 HP: {m_hp}")
    print("=" * 40)

# ==========================================
# 3. 메인 게임 흐름
# ==========================================
def main():
    print("🎮 JRPG 퀴즈 배틀 게임에 오신 것을 환영합니다!")
    player_name = input("당신의 이름을 입력하세요: ")
    player_hp = 50
    
    # [조건 반영] 두세 종류의 적 중 랜덤하게 하나를 선택 (random.choice 활용)
    enemy = random.choice(monsters)
    monster_name = enemy[0]
    monster_hp = enemy[1]
    monster_atk = enemy[2]
    
    print(f"\n📢 야생의 [{monster_name}](이)가 나타났다! (HP: {monster_hp} / ATK: {monster_atk})")
    
    # 퀴즈를 순서대로 내기 위한 인덱스 변수
    quiz_index = 0
    
    # [조건 반영] 사용자나 적의 체력이 0 이하가 될 때까지 전투 반복 (while문)
    while player_hp > 0 and monster_hp > 0:
        show_status(player_name, player_hp, monster_name, monster_hp)
        
        # 준비된 문제를 다 썼을 경우를 대비한 예외 처리
        if quiz_index >= len(quiz_pool):
            print("무승부 어떻게 한 거죠? 안 될텐데...")
            break
            
        # 현재 차례의 퀴즈 가져오기
        current_quiz = quiz_pool[quiz_index]
        print(f"📝 [문제] {current_quiz[0]}")
        print(f"{current_quiz[1]}   {current_quiz[2]}   {current_quiz[3]}")
        
        user_choice = input("옳은 선택지의 번호를 입력하세요 (1~3): ")
        correct_answer = current_quiz[4]
        
        # ----------------------------------------------------
        # 📌 [네가 채워야 할 부분] 조건문(if-else) 작성하기
        # ----------------------------------------------------
        # 1. 만약 user_choice 가 correct_answer 와 같다면?
        #    - 적의 체력(monster_hp)을 일정 수치(예: 15)만큼 감소시키고 메시지 출력하기
        if user_choice == correct_answer:
            print(current_quiz[5])
            monster_hp -= current_quiz[7]
        else:
            print(current_quiz[6])  
            player_hp -= monster_atk
        # 2. 정답이 아니라면? (else)
        #    - 사용자의 체력(player_hp)을 적의 공격력(monster_atk)만큼 감소시키고 메시지 출력하기
        # ----------------------------------------------------
        
        
       #pass
        
        # 다음 문제를 내기 위해 인덱스 1 증가
        quiz_index += 1
        
    # ==========================================
    # 4. 최종 승패 판정
    # ==========================================
    print("\n💥 전투 종료! 💥")
    if monster_hp <= 0:
        print(f"🎉 승리했습니다! {monster_name}을(를) 물리쳤습니다!")
    elif player_hp <= 0:
        print(f"💀 패배했습니다... {monster_name}에게 당했습니다.")

if __name__ == "__main__":
    main()