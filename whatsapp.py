from selenium import webdriver
import os
import time
def banner():
 print('''
  SPAM WHATSAPP by Ridho Code
  ''')
def main():
 driver = webdriver.Chrome()
 driver.get('https://web.whatsapp.com/')
 inputan(driver)
 
 lagi = input('lagi? y/n : ')
 while lagi == 'y':
 	inputan(driver)
 else:
 	print('Terimakasih')

def inputan(driver):
 name = input('Masukan Nama target atau Nama Group : ')
 msg = input('Pesan anda : ')
 count = int(input('Jumlah pesan: '))

 input('Spam sekarang... ')
 try:
   user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
   user.click()
 
 # The classname of message box may vary.
   msg_box = driver.find_element_by_class_name('DuUXI')
 except Exception as e:
   raise
 else:
   pass
 finally:
   pass

 
  
 for i in range(count):
  msg_box.send_keys(msg)
  # The classname of send button may vary.
  # time.sleep(0.3)
  try:
  	button = driver.find_element_by_class_name('_2Ujuu')
  	button.click()
  except Exception as e:
  	pass
  else:
  	pass
  finally:
  	pass
 
 print('Berhasil!')
 time.sleep(1)	
banner()
main()
