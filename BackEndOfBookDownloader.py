import sys
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import os
import urllib.request
import zipfile
import GiveTxt

stop = False


Aubooks = 0
D = 0
txtAubooks = ""

AudioNum = 0
TitelsNum = 1
txtPrint = ""
Titels = ""





urlForDownloadProgramm = 'https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-win64' \
                         '.zip '
urlForYouTubeChannel = "https://www.youtube.com/channel/UC_OiTlg2uvXrAwYL7vetZBg/videos"



def Stop():

    now = datetime.now()
    current_time = now.strftime("%H:%M")
    GiveTxt.Insert(f"[{current_time}] Скачивание завершено")

    exit(0)


def RightPath(Path):
    try:
        os.chdir(Path)
        print(f"Путь '{Path}' указан верно")
        return True
    except:
        print(f"Путь '{Path}' указан неверно")
        return False


def MakeSoft():
    global txtAubooks
    global txtPrint

    os.chdir("C:\\")

    if not os.path.isdir("soft"):
        os.mkdir("soft")

    os.chdir("C:\\soft")

    if not os.path.isdir("BookDownloader"):
        os.mkdir("BookDownloader")

    os.chdir("C:\soft\BookDownloader")

    if "txtPrint.txt" in os.listdir():
        pass
    else:
        txtPrint = open("txtPrint.txt", "w")
        txtPrint.close()

    if "txtAubooks.txt" in os.listdir():
        pass
    else:
        txtAubooks = open("txtAubooks.txt", "w")
        txtAubooks.close()







def DownloadProgramm():
    os.chdir("C:\\soft\\BookDownloader")
    IsHas = os.listdir()
    if "geckodriver-v0.31.0-win64.zip" in IsHas:
        return True

    else:
        urllib.request.urlretrieve(urlForDownloadProgramm, 'C:\\soft\\BookDownloader\\geckodriver-v0.31.0-win64.zip')

    try:

        fantasy_zip = zipfile.ZipFile("C:\\soft\\BookDownloader\\geckodriver-v0.31.0-win64.zip")
        fantasy_zip.extract("geckodriver.exe", "C:\\soft\\BookDownloader\\geckodriver-v0.31.0-win64")
    except:
        return False


def GetDownloadBooks(Path, Txt):
    global Aubooks
    global D
    global txtAubooks
    global txtPrint

    Aubooks = 0
    D = 0

    os.chdir(Path)

    for file in os.listdir():

        os.chdir("C:\soft\BookDownloader")
        txtPrint = open("txtPrint.txt", "a")

        if ".mp3" in file:
            Aubooks += 1
            txtPrint.write(file.replace(".mp3", ""))
            txtPrint.close()

    if Txt == False:
        if Aubooks == 0:
            pass
        else:
            txtAubooks = open("txtAubooks.txt", "a")
            txtAubooks.write(str(Aubooks))
            txtAubooks.close()

        os.chdir("C:\soft\BookDownloader")
        txtAubooks = open("txtAubooks.txt", "r")
        Aubooks = txtAubooks.read()
        txtAubooks.close()


        for i in Aubooks:
            A = int(i)
            for j in i:
                try:
                    B = int(j[+1])
                    C = A + B
                    D += C
                except:
                    D += int(i)


        print(D)
    else:
        pass
    return D



def DownloadBooks(Num, Path, Sort):
    global AudioNum
    global D
    global TitelsNum
    global Titels
    global stop
    global txtPrint

    now = datetime.now()
    current_time = now.strftime("%H:%M")
    GiveTxt.Insert(f"[{current_time}] Загрузка...")

    os.chdir("C:\soft\BookDownloader")
    GetDownloadBooks(Path=Path, Txt=False)

    options = webdriver.FirefoxOptions()
    options.headless = True
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference("media.volume_scale", "0.0")

    s = Service("C:\soft\BookDownloader\geckodriver-v0.31.0-win64\geckodriver.exe")
    driver = webdriver.Firefox(service=s, options=options)

    time.sleep(5)




    driver.get(url=urlForYouTubeChannel)
    time.sleep(5)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    GiveTxt.Insert(f"[{current_time}] Загрузка завершена")



    for i in range(0, int(Num) + D):

        now = datetime.now()
        current_time = now.strftime("%H:%M")
        GiveTxt.Insert(f"[{current_time}] Скачиваю книги...")

        while True:
            try:

                Titels = driver.find_elements(By.XPATH, '//*[@id="video-title-link"]')
                driver.execute_script("arguments[0].scrollIntoView();", Titels[TitelsNum])

                TitelsNum += 1
                break

            except:
                pass

        TitelUrl = Titels[i].get_attribute('href')
        TitelsTexts = Titels[i].text

        if "аудиокнига" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("аудиокнига", "")

        if "Аудиокнига" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("Аудиокнига", "")

        if "." in TitelsTexts:
            TitelsTexts = TitelsTexts.replace(".", "")

        if "Аудиокнига" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("Аудиокнига", "")

        if "аудиспектакль" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("аудиспектакль", "")

        if "фантастика" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("фантастика", "")

        if "слушать" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("слушать", "")

        if "audiobook" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("audiobook", "")

        if "рассказ" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("рассказ", "")

        if "аудиоспектакль" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("аудиоспектакль", "")

        if "мистика" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("мистика", "")

        if "страшная" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("страшная", "")

        if "история" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("история", "")

        if "Читает Гарри Стил" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("Читает Гарри Стил", "")

        if "хорор" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("хорор", "")

        if "Страшная" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("Страшная", "")

        if "киберпанк" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("киберпанк", "")

        if "на ночь" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("на ночь", "")

        if "пришельцы космос" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("пришельцы космос", "")

        if "постапокалипсис" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("постапокалипсис", "")

        if "аудиоспекткль" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("аудиоспекткль", "")

        if "фэнтези" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("фэнтези", "")

        if "онлайн" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("онлайн", "")

        if "аудиокниги" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("аудиокниги", "")

        if "классика" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("классика", "")

        if "классическая литера" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("классическая литера", "")

        if "фэнтези" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("фэнтези", "")

        if "научная" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("научная", "")

        if "слуша" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("слуша", "")

        if "тура" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("тура", "")

        if "/" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("/", "|")

        if "audiobo" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("audiobo", "")

        if "adiobook" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("adiobook", "")

        if " ов" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("ов", "")

        if "audio" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("audio", "")

        if "b" in TitelsTexts:
            TitelsTexts = TitelsTexts.replace("b", "")

        TitelsTexts = TitelsTexts.rstrip()

        TitelsTexts = TitelsTexts + " - Гарри Стил"


        for j in range(5):
            os.chdir("C:\soft\BookDownloader")
            txtPrint = open("txtPrint.txt", "r")
            if TitelsTexts in txtPrint.read():
                txtPrint.close()

            else:

                txtPrint.close()

                AudioNum += 1




                driver.execute_script(f'''window.open("{TitelUrl.replace("youtube", "youtubemz")}","_blank");''')
                driver.switch_to.window(driver.window_handles[1])

                while True:
                    try:

                        time.sleep(10)

                        Failed = driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div/div[2]/div["
                                                               "2]/div/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[3]")\
                            .get_attribute("textContent")

                        if Failed == "Failed":
                            driver.refresh()
                        DownloadFile = driver.find_element(By.XPATH,
                                                           "/html/body/div[1]/section[1]/div/div[2]/div[2]/div/div["
                                                           "2]/div[ "
                                                           "2]/div[ "
                                                           "3]/table/tbody/tr[2]/td[3]/button[1]/a").get_attribute(
                            "href")
                        break


                    except:
                        time.sleep(1)


                if Sort == True:

                    while True:
                        try:
                            urllib.request.urlretrieve(DownloadFile, rf"{Path}/{str(AudioNum)} {TitelsTexts}.mp3")
                            break
                        except exec:
                            print(exec)
                            time.sleep(3)
                else:
                    while True:
                        try:
                            urllib.request.urlretrieve(DownloadFile, rf"{Path}/{TitelsTexts}.mp3")
                            break
                        except exec:
                            print(exec)
                            time.sleep(3)



                driver.close()
                driver.switch_to.window(driver.window_handles[0])

                GetDownloadBooks(Path=Path, Txt=True)

    GetDownloadBooks(Path=Path, Txt=False)

    now = datetime.now()
    current_time = now.strftime("%H:%M")
    GiveTxt.Insert(f"[{current_time}] Было скачано {AudioNum} книг")

    now = datetime.now()
    current_time = now.strftime("%H:%M")
    GiveTxt.Insert(f"[{current_time}] Скачивание завершено")

    exit(0)




            # while not IsTime:
            #     try:
            #
            #         VideoTime = driver.find_element(By.CSS_SELECTOR, f"div.row:nth-child(2)").text
            #         if VideoTime == "":
            #
            #             IsTime = False
            #
            #         else:
            #
            #             IsTime = True
            #     except:
            #
            #         driver.find_element(By.XPATH, '//*[@id="sf_submit"]').click()
            #         time.sleep(5)
            #
            #     VideoTimeNum = int(len(VideoTime))
            #
            #     if VideoTimeNum == 5:
            #
            #         IsTimeLong = False
            #
            #     elif VideoTimeNum == 7:
            #
            #         VideoTime = VideoTime[:1]
            #
            #         if int(VideoTime) >= 2:
            #             IsTimeLong = True
            #
            #     driver.close()
            #     driver.switch_to.window(driver.window_handles[0])
            #
            #     IsTime = False
            #
            #     if IsTimeLong:
            #
            #         pass
            #
            #     else: