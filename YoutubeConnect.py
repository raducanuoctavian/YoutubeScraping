from selenium import webdriver


class YoutubeConnect:
    adresa = "http://www.youtube.com"

    def __init__(self, adresa=adresa):
        self.adresa = adresa

    def connect_to_youtube(self):
        # conectare driver chrome
        chrome = webdriver.Chrome()
        print("Driver set")
        # Conectare la pagina youtube
        chrome.get(self.adresa)
        print("Youtube se deschide")
        # Maximize la window-ul deschis
        chrome.maximize_window()
        print("Maximize")
        # Un mic delay sa apuce sa se incarce elementele de JS
        chrome.implicitly_wait(10)
        # Cautarea butonului de I agree pentru cookies
        chrome.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']").click()
        print("Agree cookies")
        # Un mic delay sa apuce sa se incarce elementele de JS
        chrome.implicitly_wait(15)
        # click si pe titlul videoului
        print("Video gasit")
        chrome.find_element_by_xpath("//yt-formatted-string[@id='video-title']").click()
        try:
            skip = chrome.find_element_by_xpath("//button[@class='ytp-ad-skip-button ytp-button']")
            skip.click()
            print("Skipped add")
        except:
            print("nu a fost gasit nici un add/ unskippable add")
        # try:
        #     skip = chrome.find_element_by_xpath("//button[@class='ytp-ad-skip-button ytp-button']")
        #     skip.click()
        #     print("Skipped add")
        # except:
        #     print("nu a fost gasit nici un add/ unskippable add")


