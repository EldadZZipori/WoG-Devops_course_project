from selenium import webdriver
from selenium.common.exceptions import WebDriverException

WEBDRIVER_URL = "./geckodriver"

# this function will test the MainScores flask server.
def test_scores_service(app_url: str) -> bool:
    try:
        firefox_driver = webdriver.Firefox(executable_path=WEBDRIVER_URL)
        firefox_driver.get(app_url)
        score_found = firefox_driver.find_element_by_id("score").text
    
    # this exception can handle all problems rasied by these functions
    except WebDriverException as e:
        print(e)
        return 1

    try:
        score_found_as_int = int(score_found)
    except ValueError as e:
        print("Scores is not an integer")
        return 1

    if score_found_as_int >= 0 and score_found_as_int <=  1000:
        return 0 # means test did not failed
    else:
        return 1 # means test failed
    
    
    



# the main function will return  1 - fail or 0 - pass to indicate test result
if __name__ == "__main__":
    exit(test_scores_service("http://0.0.0.0:8777"))