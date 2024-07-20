from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from time import sleep
#Code to test on a google form
link = "https://forms.gle/WT68aV5UnPajeoSc8"

driver = webdriver.Chrome(service=Service('./chromedriver-linux64/chromedriver'))


def automateGoogleForm(link):
  dataList = ['Sujit Kumar', 7052070747,'raos92249@gmail.com', 277001, '15-08-2002', 'Male','GNFPYC']
  elClass = "whsOnd"
  elAdClass = "KHxj8b"
  submitClass = "l4V7wb"
  driver.get(link)
  try:
    WebDriverWait(driver,15).until(
      expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME,elClass)),
      )

    
    formElements = driver.find_elements(By.CLASS_NAME,elClass)
    # print(formElements[0].accessible_name)
    
    for index,el in enumerate(formElements):
      print("Index:",index)
      el.send_keys(dataList[index])
      print("Input Field Description : ",el.accessible_name)
      sleep(0.5)
      # if(el.accessible_name=='Type this code: GNFPYC Required question'):
      #   el.send_keys("GNFPYC")

      

    WebDriverWait(driver,15).until(
      expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME,elAdClass))
    )

    
    # for elAd in formAdElement:
    #   elAd.send_keys("Mau Up")
    #   print("\n\n Address Form Description is: ",formAdElement)

    driver.execute_script("document.getElementsByClassName('KHxj8b tL9Q4c')[0].value='Chandpur Bijnor'")
    driver.execute_script("document.getElementsByClassName('KHxj8b tL9Q4c')[0].dispatchEvent(new Event('input', { bubbles: true }))")
   
    WebDriverWait(driver,15).until(
      expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME,submitClass))
    )

    sleep(2)
    driver.execute_script("document.getElementsByClassName('l4V7wb Fxmcue')[0].click()")

    submitBtn = driver.find_elements(By.CLASS_NAME,submitClass)
    print("Form Submitted")
    sleep(2)
  except TimeoutException as te:
    print("Time out Exception Occured",te)
  except ElementNotInteractableException as e:
    print("Interacting with element before it is loaded cause Interactable error")
  finally:
    print("Exited....")
    driver.quit()





automateGoogleForm(link)

