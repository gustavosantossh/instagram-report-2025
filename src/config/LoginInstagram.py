import json


class LoginInstagram:

    @staticmethod
    def login(By, EC, wait, config):

        login_username_input = wait.until((EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[1]/div[1]/div/label/input"))))

        login_password_input = wait.until((EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[1]/div[2]/div/label/input"))))

        login_username_input.clear()
        login_password_input.clear()
        login_username_input.send_keys(config['username'])
        login_password_input.send_keys(config['password'])

        singIn_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[1]/div[3]/button")))
        singIn_button.click()

        login_save = wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/section/div/button")))
        login_save.click()
