import io, time, requests
from PIL import Image
from selenium.webdriver.common.by import By
def get_images(driver,max_images):#this function is download max_images photos from url
    def scroll(driver):
        scroll_pause_time = 1
        screen_height = driver.execute_script("return window.screen.height;")
        i = 1
        while True:
            driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
            i += 1
            time.sleep(scroll_pause_time)
            scroll_height = driver.execute_script("return document.body.scrollHeight;")
            if (screen_height) * i > scroll_height:
                break
    url = "https://www.pexels.com/tr-tr/"
    driver.get(url)
    images = list()
    while max_images > len(images):
        images = driver.find_elements(By.CLASS_NAME,"MediaCard_image__ljFAl")
        scroll(driver)
    for i, image in enumerate(images):
        if image.get_attribute('src') and 'http' in image.get_attribute('src') and i < (max_images-1):
            dowland_images("photos/", image.get_attribute('src'), str(i) + ".jpg")
def dowland_images(downland_path,url,file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = downland_path+file_name

        with open(file_path, "wb") as f:
            image.save(f, "JPEG")
        print("dowland succses")
    except Exception as e:
        print("error:", e)