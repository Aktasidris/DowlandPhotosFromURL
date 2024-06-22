#Download one image
from func import dowland_images,get_images
url="https://scontent.cdninstagram.com/v/t51.2885-15/383984498_2488521017981824_8431474509136094190_n.heic?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent.cdninstagram.com&_nc_cat=104&_nc_ohc=Jz-jebpXEZkAX__uXNt&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfB_tgZF8MDC_9DrRz5GBV9Kl_F02YVSMb8N6-F3jgVhzQ&oe=651CD20D&_nc_sid=10d13b"
dowland_images("photos/",url,".jpg")#(save_location,target_url,save_format)
#Downloading all images from a website url and images css tag
from selenium import webdriver
driver = webdriver.Chrome()#You can add path paramether like "./chromedriver.exe"
max_images=50 #downloading 50 images
get_images(driver,max_images)