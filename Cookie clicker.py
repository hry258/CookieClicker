
from selenium import webdriver
import tkinter as tk, re, threading, sys


class GuiPart:
    def __init__(self, master, endCommand, startCommand, quitCommand):

        play_window = tk.Frame(master=master)
        play_window.pack()

        start_btn = tk.Button(master=play_window, text='Start', command=startCommand, width=25, height=2)
        start_btn.pack(pady=2)
        stop_btn = tk.Button(master=play_window, text='Stop', command=endCommand, width=25, height=2)
        stop_btn.pack(pady=2)
        quit_btn = tk.Button(master=play_window, text='Quit', command=quitCommand, width=25, height=2)
        quit_btn.pack(pady=2)


class ThreadedClient:
    """
    Launch the main part of the GUI and the worker thread.
    """

    browserWindowIsOpen = False

    def __init__(self, master):
        self.master = master

        self.gui = GuiPart(master, self.endApplication, self.startApplication, self.quitApplication)

        self.running = 0
        self.thread1 = threading.Thread(target=self.workerThread1)

    def startApplication(self):
        if not self.browserWindowIsOpen:
            self.browser = webdriver.Chrome("C:\\Python3.8.5\\Scripts\\chromedriver.exe")
            self.browser.get("https://orteil.dashnet.org/cookieclicker/")
            self.browser.set_window_position(2500, 0)
            self.browser.fullscreen_window()
            self.browserWindowIsOpen = True
        if not self.thread1.is_alive():
            self.running = 1
            self.thread1 = threading.Thread(target=self.workerThread1)
            self.thread1.start()

    def endApplication(self):
        self.running = 0

    def quitApplication(self):
        try:
            self.browser.close()
        except:
            pass
        sys.exit(0)

    def workerThread1(self):
        cookie = self.browser.find_element_by_id("bigCookie")

        global xpath_list
        global bool_list
        global all_unlocked

        while self.running:
            cookie.click()
            cookie_number = int(re.match("\d+", (self.browser.find_element_by_xpath("/html/body/div/div[2]/div[15]/div[4]").text)).group())

            while not all_unlocked:
                if not bool_list[0]:
                    if cookie_number >= 100:
                        xpath_list["grandma"] = ["/html/body/div/div[2]/div[19]/div[3]/div[6]/div[3]/div[3]/span[2]", "/html/body/div/div[2]/div[19]/div[3]/div[6]/div[3]"]
                        bool_list[0] = 1
                        # cursor upgrade 100
                        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[19]/div[3]/div[5]/div[1]').click()
                    else:
                        break

                if cookie_number >= 500:
                    try:
                        # Cursor upgrade 500
                        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[19]/div[3]/div[5]/div[2]').click()
                    except:
                        pass
                else:
                    break

                if not bool_list[1]:
                    if cookie_number >= 1100:
                        xpath_list["farm"] = ["/html/body/div/div[2]/div[19]/div[3]/div[6]/div[4]/div[3]/span[2]", "/html/body/div/div[2]/div[19]/div[3]/div[6]/div[4]"]
                        bool_list[1] = 1
                        # grandma upgrade 1.000
                        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[19]/div[3]/div[5]/div[2]').click()
                    else:
                        break

                if cookie_number >= 5000:
                    try:
                        # Grandma upgrade 5.000
                        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[19]/div[3]/div[5]/div[3]').click()
                    except:
                        pass
                else:
                    break

                if not bool_list[2]:
                    if cookie_number >= 12000:
                        xpath_list["mine"] = ["/html/body/div/div[2]/div[19]/div[3]/div[6]/div[5]/div[3]/span[2]", "/html/body/div/div[2]/div[19]/div[3]/div[6]/div[5]"]
                        bool_list[2] = 1
                        # Cursor upgrade 10.000
                        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[19]/div[3]/div[5]/div[4]').click()
                    else:
                        break

                if cookie_number >= 11000:
                    try:
                        # Farm upgrade 11.000
                        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[19]/div[3]/div[5]/div[2]').click()
                    except:
                        pass
                else:
                    break

                if cookie_number >= 50000:
                    try:
                        # Mouse upgrade 50.000
                        self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[19]/div[3]/div[5]/div[4]').click()
                    except:
                        pass
                else:
                    break

                if not bool_list[3]:
                    if cookie_number >= 130000:
                        xpath_list["factory"] = ["/html/body/div/div[2]/div[19]/div[3]/div[6]/div[6]/div[3]/span[2]", "/html/body/div/div[2]/div[19]/div[3]/div[6]/div[6]"]
                        bool_list[3] = 1
                    else:
                        break

                # if not bool_list[4]:   -------handle 'MILLION' keyword------------
                #     if cookie_number >= 1400000:
                #         xpath_list['bank'] = ["/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[7]/div[3]/span[2]", "/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[7]"]
                #         bool_list[4] = 1
                #     else:
                #         break

                break

            for key in xpath_list.keys():
                try:
                    item_price = self.browser.find_element_by_xpath(xpath_list[key][0])
                    if int(re.match("\d+", item_price.text).group()) <= cookie_number:
                        item_button = self.browser.find_element_by_xpath(xpath_list[key][1])
                        item_button.click()
                except:
                    pass


xpath_list = {"cursor": ["/html/body/div/div[2]/div[19]/div[3]/div[6]/div[2]/div[3]/span[2]", "/html/body/div/div[2]/div[19]/div[3]/div[6]/div[2]"]}
bool_list = [0 for i in range(15)]
all_unlocked = False

window = tk.Tk()
positionRight = int(window.winfo_screenwidth()/2 - window.winfo_reqwidth()/2)
positionDown = int(window.winfo_screenheight()/3 - window.winfo_reqheight()/2)
window.title("Cookie clicker mod")
window.geometry(f"{350}x{500}+{positionRight}+{positionDown}")
client = ThreadedClient(window)
window.mainloop()
