class ReportMap:
    @staticmethod
    def report(By, EC, wait):
        for x in range(0,40):
            more = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/section/main/div/header/section[2]/div/div/div[3]/div/div")))
            more.click()

            report_button = wait.until(EC.presence_of_element_located((By.XPATH,"//button[contains(., 'Denunciar')]")))

            report_button.click()

            report_account = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(., 'Denunciar conta')]")))
            report_account.click()

            report_account_type = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(., 'Está publicando conteúdo que não deveria estar no Instagram')]")))
            report_account_type.click()


            report_type = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(., 'Suicídio, automutilação ou distúrbios alimentares')]")))
            report_type.click()

            report_type_2 = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(., 'Suicídio ou automutilação')]")))
            report_type_2.click()

            close = wait.until(EC.presence_of_element_located((By.XPATH,"//button[contains(., 'Fechar')]")))
            close.click()