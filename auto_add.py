import pyautogui
import time
from random import randint

def add_post(x):
    for i in range(x):
        text = f"post = Post(title = 'Post {i+1}', content = 'post {i+1} content', user_id = {randint(1,3)})"
        pyautogui.typewrite(text)
        pyautogui.press('enter')
        time.sleep(0.05)
        pyautogui.typewrite(f"with current_app.current_app_context():\n\tdb.session.add(post)\n\tdb.session.commit()")
        time.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.press('enter')
        time.sleep(0.2)


def add_user(x):
    for i in range(x):
        text = f"user = User(username = 'Test.User.{i}', email = 'test.user.{i}@email.com', password = 'password')"
        pyautogui.typewrite(text)
        pyautogui.press('enter')
        time.sleep(0.2)
        pyautogui.typewrite(f"with current_app.current_app_context():\n\tdb.session.add(user)\n\tdb.session.commit()")
        time.sleep(0.2)
        pyautogui.press('enter')
        pyautogui.press('enter')

        cursor_pos = pyautogui.position()
        if cursor_pos.x == 0 and cursor_pos.y == 0:
            exit()

if __name__ == "__main__":
    time.sleep(5)
    add_post(30)