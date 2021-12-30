import config.config_browser as config_browser
import config.config_env as config_env
import config.config_date as config_date
import auto_absen

config_browser.browser.get(config_env.link)

if((config_date.today != 'sabtu' or config_date.today != 'minggu') and config_env.is_active == 'true'):
    # login
    auto_absen.login_access()

    if config_date.dateNow.hour == 8:
        if(config_date.dateNow.minute == 00):
            # checkin
            auto_absen.checkin()
    else:
        if(config_date.dateNow.minute == 00):
            # checkout
            auto_absen.checkout()

config_browser.browser.close()

