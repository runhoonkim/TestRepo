# 자동 예약 함수
def auto_reservation():
    import pyautogui
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    import time

    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)

    # URL 접속
    driver = webdriver.Chrome(options=options)
    url = "https://www.airport.co.kr/gimpo/cms/frCon/index.do?MENU_ID=1970&CONTENTS_NO=1&pRetUrl=%2Fgimpo%2Fcms%2FfrCon%2Findex.do%3FMENU_ID%3D2470"
    driver.get(url)


    # 아이디, 비밀번호 입력
    driver.find_element(By.NAME, "sUserId").send_keys("YOUR_ID")
    driver.find_element(By.NAME, "sUserPw").send_keys("YOUR_PASSWORD")

    # 로그인 버튼 클릭
    driver.find_element(By.CSS_SELECTOR, ".sbtn.red").click()

    # 이용신청 화면 이동
    time.sleep(0.1)
    driver.find_element(By.LINK_TEXT, "이용신청").click()

    # 등록 버튼 클릭
    time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, ".btnC.btn_reg").click()

    # 체크박스 클릭
    time.sleep(0.1)
    driver.find_element(By.ID, "ck_01").click()
    driver.find_element(By.ID, "ck_02").click()

    # 제목 입력
    reg_subject = "농구장 사용신청합니다."
    driver.find_element(By.CSS_SELECTOR, ".inp_t").send_keys(reg_subject)

    # 내용 입력
    reg_contents = """
    사용시설: 농구장(반코트, 풀코트)
    이름 : 000
    소속 : 예시) 공사 취미회(축구회,야구회), 공사직원, 자회사 직원, 지역주민(서울 강서구, 경기도 김포시 등)
    ※ 사원증 및 신분증 지참 필수
    연락처 : 000-0000-0000
    사용인원: 00명
    사용일시 : 일자 : 0000. 00. 00. 시간 : 00:00 ~ 00:00
    ※ 최소 1시간~3시간(30분 단위 적용가능)
    ※ 이용 가능 시간 오전 6시 ~ 오후 9시 30분(일요일 : 09:00~17:30)
    차량번호 :
    """ # 내용 변경 필요
    driver.find_element(By.CSS_SELECTOR, ".inp_area").clear()
    driver.find_element(By.CSS_SELECTOR, ".inp_area").send_keys(reg_contents)

    # 저장 버튼 클릭
    driver.find_element(By.CSS_SELECTOR, ".btnC.goSave").click()

    # 팝업 저장 버튼 클릭
    time.sleep(1)
    pyautogui.click(1040,189)
    time.sleep(1)
    pyautogui.click(1137,184)

    time.sleep(5)
    driver.quit()

# 매주 금요일 오전 9시마다 함수 실행
import schedule
schedule.every().friday.at("09:00:00").do(auto_reservation())