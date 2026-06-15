import random  # 랜덤 적 선택, 공격력 배율 계산, 메시지 출력을 위해 필요

# ==========================================
# 1. 데이터 구조 설계 (2차원 리스트 및 메시지)
# ==========================================
monsters = [
    ["에니악", 60, 5],
    ["골든 레코드", 100, 10],
    ["깊은 생각", 200, 25]
]

# 퀴즈 데이터: [질문, 선택지1, 선택지2, 선택지3, 정답 번호, 정답메시지, 오답메시지, 대미지배율]
quiz_pool = [
    ["대한민국의 수도는 어디일까요?", "1. 부산", "2. 서울", "3. 인천", "2", "이건 맞춰야지요.", "잘못 누른거죠?", 3],
    ["파이썬에서 출력을 할 때 사용하는 함수는?", "1. input()", "2. print()", "3. type()", "2", "print(Hello, World!), 이건 아시죠?", "수행평가는 어떻게 보셨죠?", 5],
    ["다음 중 숫자가 아닌 자료형은?", "1. 문자열(str)", "2. 정수(int)", "3. 실수(float)", "1", "문자열은 이름부터 문자열이죠.", "혹시 정수랑 실수가 뭔지 모르시나요?", 5],
    ["반복문을 중간에 멈추게 하는 키워드는?", "1. continue", "2. pass", "3. break", "3", "continue는 반복문 안에서 건너뛰기, pass는 코드를 실행하지 않습니다.", "영어 공부를 하셔야 겠네요...", 3],
    ["조건을 비교할 때 사용하는 제어문은?", "1. for", "2. if", "3. while", "2", "조건문 if!", "for와 while은 반복문입니다.", 5],
    ["삶, 우주, 그리고 모든 것에 대한 궁극적인 질문의 해답은?", "1. Cogito ergo sum.", "2. 빛이 있으라", "3. 42", "3", "당신은 지구인가요?", "두뇌 풀가동!", 60],
    ["황조가는 누가 썼는가?", "1. 유리왕", "2. 황조", "3. 가", "1", "문학 교과서에 나오죠.", "오타인가요? 키보드 좀 잘 보셔야 겠네요.", 3],
    ["<퍼셉트론>의 저자는?", "1. 앨런 튜링", "2. 얀 르쿤", "3. 마빈 민스키", "3", "찍은 건 아니죠?", "까먹을 때도 됐죠.", 10],
    ["<소설가 구보 씨의 일일>의 등장인물이 아닌 것은?", "1. 구보 씨", "2. 옛 동무", "3. 윤 직원", "3", "낼 문제가 생각이 안 나기 시작했어요.", "윤 직원은 <태평천하>의 등장인물입니다.", 5],
    ["Python은 무슨 뜻일까요?", "1. 직공", "2. 호숫가", "3. 비단뱀", "3", "세 보이는 이름이죠.", "문제 아이디어 있나요?", 10],
    ["다음 중 프로그래밍 언어의 종류가 아닌 것은?", "1. Joker", "2. C", "3. Java", "1", "Why are you so serious?", "프로그래밍 언어는 많아요.", 10],
    ["세계 최초의 컴퓨터는?", "1. 콜로서스", "2. 에니악", "3. 매킨토시", "1", "사실 이것도 정답이 아니라네요...", "에니악이라고 생각하셨나요?", 10],
    ["가장 무거운 원소는?", "1. 납", "2. 오가네손", "3. 우라늄", "2", "주변에 주기율표 외우는 인간이 있다면 맨날 듣는답니다!", "이건 몰라도 돼요. 정말로요.", 30],
    ["다음 중 2학년 6반 2학기의 원반 과목이 아닌 것은?", "1. 화학반응의 세계", "2. 세포와 물질대사", "3. 인공지능과 기초", "3", "6반은 이과반이랍니다.", "정보 한 번 더 들을래요?", 10],
["광교고등학교는 어디에 있는가?", "1. 보스턴", "2. 수원", "3. 로테르담", "2", "광교는 수원에 있습니다.", "지도 좀 봐요.", 0]
]

# ==========================================
# 2. 기능별 함수 분리 설계 (모듈화)
# ==========================================

# [함수 1] 상태 출력 함수
def show_status(p_name, p_hp, p_potions, m_name, m_hp):
    """현재 플레이어와 몬스터의 상태를 보여주는 함수"""
    print("\n" + "=" * 40)
    print(f"🤠 {p_name}의 HP: {p_hp} | 🧪 남은 포션: {p_potions}개")
    print(f"👾 {m_name}의 HP: {m_hp}")
    print("=" * 40)


# [함수 2] 플레이어 턴 처리 함수
def player_turn(player_name, player_hp, player_base_atk, player_potions, max_hp, monster_hp):
    """플레이어의 턴 행동(공격/회복)을 받아 연산하고 결과를 반환하는 함수"""
    print(f"\n🟢 [{player_name}의 턴] 행동을 선택하세요.")
    print("1. 일반 공격 (기본 공격력에 무작위 배율 적용)")
    print("2. 회복 포션 사용 (HP 20 회복)")
    
    player_choice = input("선택 (1 또는 2): ")
    
    if player_choice == "1":
        # 난수로 플레이어 기본 공격력에 배율(0.8 ~ 1.5배) 계산
        rate = round(random.uniform(0.8, 1.5), 1)  # 소수점 첫째자리까지
        damage = int(player_base_atk * rate)
        monster_hp -= damage
        print(f"⚔️ {player_name}의 공격! {rate}배의 대미지({damage})를 입혔습니다!")
        
    elif player_choice == "2":
        if player_potions > 0:
            player_hp += 20
            # 만약 회복한 체력이 최대 체력을 넘어가면, 최대 체력으로 고정!
            if player_hp > max_hp:
                player_hp = max_hp
            player_potions -= 1
            print(f"🧪 포션을 사용했습니다! HP가 회복되었습니다. (현재 HP: {player_hp}/{max_hp})")
        else:
            print("❌ 포션이 부족합니다! 회복에 실패하여 이번 턴을 낭비했습니다.")
            
    else:
        # 엉뚱한 입력 시 턴 스킵
        print("⚠️ 잘못된 입력입니다! 허점을 보여 플레이어 턴이 스킵됩니다.")
        
    # 변경된 값을 메인 흐름으로 다시 돌려줌 (Return)
    return player_hp, player_potions, monster_hp


# [함수 3] 적(몬스터) 턴 처리 함수 (방어 퀴즈)
# 💡 [수정] monster_hp를 매개변수에 추가하여 함수 안에서 인지할 수 있게 했습니다.
def enemy_turn(monster_name, monster_atk, player_hp, monster_hp, current_quiz):
    """적의 공격에 대응하는 퀴즈를 출제하고, 채점 결과에 따라 플레이어와 몬스터의 체력을 연산해 반환하는 함수"""
    print(f"\n🔴 [{monster_name}의 턴] {monster_name}(이)가 공격해옵니다! 문제를 맞춰 방어하세요!")
    print(f"📝 [방어 퀴즈] {current_quiz[0]}")
    print(f"{current_quiz[1]}   {current_quiz[2]}   {current_quiz[3]}")
    
    user_choice = input("정답 번호를 입력하세요 (1~3): ")
    correct_answer = current_quiz[4]
    
    if user_choice == correct_answer:
        print(f"\n정답! {current_quiz[5]}")
        # 정답 시 난이도 배율 수치만큼 몬스터에게 역으로 대미지를 줌
        monster_hp -= current_quiz[7]
        print(f"💥 카운터 어택! 퀴즈 정답 보너스로 {monster_name}에게 {current_quiz[7]}의 대미지를 입혔습니다!")
    else:
        print(f"\n틀렸습니다... {current_quiz[6]}")  
        player_hp -= monster_atk 
        print(f" {monster_name}에게 {monster_atk}만큼 피해를 입었습니다.")
        
    # 계산된 두 캐릭터의 체력을 모두 돌려줍니다.
    return player_hp, monster_hp


# ==========================================
# 3. 메인 게임 흐름 제어 함수
# ==========================================
def main():
    print("🎮 JRPG 퀴즈 배틀 게임에 오신 것을 환영합니다!")
    player_name = input("당신의 이름을 입력하세요: ")
    
    print("\n🔥 게임 난이도를 선택하세요.")
    print("1. 노말 모드 (HP 50, ATK 10, 포션 2개)")
    print("2. 하드 모드 (HP 30, ATK 7, 포션 1개)")
    mode = input("선택 (1 또는 2): ")
    
    if mode == "2":
        print("💀 하드 모드가 활성화되었습니다! 신중하게 퀴즈를 푸세요.")
        player_hp = 30
        max_hp = 30  # 최대 체력 기억
        player_base_atk = 7
        player_potions = 1
    else:
        print("🟢 노말 모드가 활성화되었습니다.")
        player_hp = 50
        max_hp = 50  # 최대 체력 기억
        player_base_atk = 10
        player_potions = 2
            
    # 게임을 시작하기 전에 퀴즈 리스트의 순서를 무작위로 섞어버립니다!
    random.shuffle(quiz_pool)
    
    # 랜덤으로 적 선택
    enemy = random.choice(monsters)
    monster_name = enemy[0]
    monster_hp = enemy[1]
    monster_atk = enemy[2]
    
    print(f"\n📢 야생의 [{monster_name}](이)가 나타났다! (HP: {monster_hp} / ATK: {monster_atk})")
    
    quiz_index = 0
    
    # 두 캐릭터 모두 살아있는 동안 전투 반복
    while player_hp > 0 and monster_hp > 0:
        # [기능 호출 1] 현재 상태 출력
        show_status(player_name, player_hp, player_potions, monster_name, monster_hp)
        
        # [기능 호출 2] 플레이어 턴 처리 함수 호출 및 결과 반영
        player_hp, player_potions, monster_hp = player_turn(
            player_name, player_hp, player_base_atk, player_potions, max_hp, monster_hp
        )
        
        # 플레이어 턴이 끝난 후 적이 쓰러졌는지 즉시 확인
        if monster_hp <= 0:
            break
            
                    
        # 💡 [수정] 적 턴 함수를 호출할 때 monster_hp도 보내고, 리턴 값도 2개 다 받아옵니다.
        player_hp, monster_hp = enemy_turn(
            monster_name, monster_atk, player_hp, monster_hp, quiz_pool[quiz_index]
        )
        
        # 다음 턴을 위해 퀴즈 인덱스 증가
        quiz_index += 1
        if quiz_index >= len(quiz_pool):
            print("\n🔄 모든 문제를 풀었습니다! 문제를 새로 섞어 출제합니다.")
            random.shuffle(quiz_pool)
            quiz_index = 0  



    # ==========================================
    # 4. 최종 승패 판정
    # ==========================================
    print("\n💥 전투 종료! 💥")
    if monster_hp <= 0:
        print(f"🎉 승리했습니다! {monster_name}을(를) 물리쳤습니다!")
    elif player_hp <= 0:
        print(f"💀 패배했습니다... {monster_name}에게 당했습니다.")


if __name__ == "__main__":
    main()  # 💡 한 번만 호출되도록 수정했습니다.


