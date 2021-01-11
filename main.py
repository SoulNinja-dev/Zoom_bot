import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime



def sign_in(meetingID, pswd):
	subprocess.call(["C:/Users/Aadhithyan Suresh/AppData/Roaming/Zoom/bin/Zoom.exe"])
	time.sleep(2)

	join_btn = pyautogui.locateCenterOnScreen('join.png')
	pyautogui.moveTo(join_btn)
	pyautogui.click()

	time.sleep(0.3)
	pyautogui.write(meetingID)

	joinbtn2 = pyautogui.locateCenterOnScreen('joinbtn.png')
	pyautogui.moveTo(joinbtn2)
	pyautogui.click()

	time.sleep(2)
	pyautogui.write(pswd)
	meetingjoin = pyautogui.locateCenterOnScreen('joinmeeting.png')

	pyautogui.moveTo(meetingjoin)
	pyautogui.click()
	
df = pd.read_csv('D:/python_projects/zoom_api/timings.csv')

while True:
	now = datetime.now().strftime("%H:%M")
	if now in str(df['timings']):

		row = df.loc[df['timings'] == now]
		m_id = str(row.iloc[0,1])
		m_pass = str(row.iloc[0,2])

		sign_in(m_id,m_pass)
		time.sleep(12)
		print('i gottu in homie')