from modules.voting import voting
from modules.utils import log_code
from modules.selectors import select_region, select_institution
from modules.config import driver, INSTITUTION_NAME, REGION_NAME
from modules.captcha import captcha

def main():

    try:
        captcha()
        select_region(driver, REGION_NAME)
        select_institution(driver, INSTITUTION_NAME)
        for _ in range(50):
            voting()
            log_code()
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
