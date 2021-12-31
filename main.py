import config.config_browser as config_browser
import config.config_env as config_env
import config.config_date as config_date
import auto_absen
import time

config_browser.browser.get(config_env.link)

config_browser.browser.set_window_position(-10000,0)

def run():
    if((config_date.today != 'sabtu' or config_date.today != 'minggu') and config_env.is_active == 'true'):
        if config_date.dateNow.hour == 8 and config_date.dateNow.minute == 00:
            # login
            auto_absen.login_access()
            
            # checkin
            auto_absen.checkin()
        else:
            if(config_date.dateNow.hour == 5 and config_date.dateNow.minute == 00):
                # login
                auto_absen.login_access()
                
                # checkout
                auto_absen.checkout()

while True:
    time.sleep(5)
    
    run()





