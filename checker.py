import requests
import time
import logging

def setup_logger():
    logger = logging.getLogger('website_checker')
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('website_checker.log')
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

def check_website(url):
    logger.info(f"Checking website: {url}")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logger.info(f"{url} is up and running.")
        else:
            logger.warning(f"{url} is down with status code {response.status_code}.")
            error_message = f"The site {url} is down with status code {response.status_code}."
            if response.content:
                error_message += f"\nResponse Content: {response.content.decode('utf-8')}"
            logger.error(error_message)
    except requests.exceptions.RequestException as e:
        logger.error(f"{url} is down with an exception: {str(e)}.")

if __name__ == "__main__":
    website_url = "https://www.example.com/"

    logger = setup_logger()

    while True:
        try:
            logger.info("===================================")  
            check_website(website_url)
        except Exception as e:
            logger.error(f"An error occurred while checking the website: {str(e)}")
        
        time.sleep(3600)
