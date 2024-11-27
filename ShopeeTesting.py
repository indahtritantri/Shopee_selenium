from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_with_email(driver, email, password):
    driver.get("https://shopee.co.id/buyer/login")
    
    try:
        login_key_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "loginKey"))
        )
        login_key_input.send_keys(email)
        print(f"Login: Email/Nomor Telepon '{email}' diisi.")

        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        
        password_input.send_keys(password)
        print(f"Login: Password '{password}' diisi.")
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "b5aVaf"))
        )
        login_button.click()
        print("Login: Tombol 'Log in' diklik.")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "K9Pfb"))
        )
        
        print("Login berhasil! Verifikasi Akun.")
    except Exception as e:
        print(f"Error pada login: {e}")

def login_with_phone(driver, phone_number):
    driver.get("https://shopee.co.id/buyer/login/otp")
    
    try:
        login_key_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "phone"))
        )

        login_key_input.send_keys(phone_number)
        print(f"Login dengan Nomor Telepon: Nomor '{phone_number}' diisi.")
        
        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "b5aVaf"))
        )
        next_button.click()
        print("Login dengan Nomor Telepon: Tombol 'Berikutnya' diklik.")
        
        send_to_whatsapp_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'b5aVaf') and contains(@class, 'PVSuiZ') and contains(@class, 'mo3UMT')]"))
        )
        send_to_whatsapp_button.click()
        print("Tombol 'Kirim ke WhatsApp' diklik.")
        
        print("Captcha muncul. Silakan selesaikan captcha secara manual.")
        
        otp_input = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.CLASS_NAME, "w_Qhj0"))
        )
        print("Captcha terverifikasi, halaman untuk memasukkan OTP muncul.")

        otp = input("Masukkan OTP yang diterima: ")
        otp_input.send_keys(otp)
        print("Login dengan Nomor Telepon: OTP diisi.")
        
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "b5aVaf"))
        )
        submit_button.click()
        print("Login dengan Nomor Telepon: Tombol 'Kirim' diklik.")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "K9Pfb"))
        )
        print("Login berhasil! Halaman beranda Shopee muncul.")
    except Exception as e:
        print(f"Error pada login dengan nomor telepon: {e}")
    driver.get("https://shopee.co.id/buyer/login/otp")
    
    try:
        login_key_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "phone"))
        )
        login_key_input.send_keys(phone_number)
        print(f"Login dengan Nomor Telepon: Nomor '{phone_number}' diisi.")

        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "b5aVaf"))
        )
        next_button.click()
        print("Login dengan Nomor Telepon: Tombol 'Berikutnya' diklik.")

        try:
            send_to_whatsapp_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'b5aVaf') and contains(@class, 'PVSuiZ') and contains(@class, 'mo3UMT')]"))
            )
            send_to_whatsapp_button.click()
            print("Tombol 'Kirim ke WhatsApp' diklik.")
        except Exception as e:
            print("Tombol 'Kirim ke WhatsApp' tidak ditemukan atau tidak perlu diklik.")
        try:
            captcha_element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "SJQ12T"))
            )
            print("Captcha ditemukan. Silakan selesaikan captcha secara manual.")
            
            WebDriverWait(driver, 60).until(
                EC.invisibility_of_element(captcha_element)
            )
            print("Captcha terverifikasi. Lanjut ke OTP.")
        except Exception as e:
            print("Captcha tidak ditemukan atau tidak perlu diselesaikan.")
        3
        otp_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "w_Qhj0"))
        )
        print("Halaman untuk memasukkan OTP muncul.")

        otp = input("Masukkan OTP yang diterima: ")
        otp_input.send_keys(otp)
        print("Login dengan Nomor Telepon: OTP diisi.")
        
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "b5aVaf"))
        )
        submit_button.click()
        print("Login dengan Nomor Telepon: Tombol 'Kirim' diklik.")
  
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "K9Pfb"))
        )
        print("Login berhasil! Halaman beranda Shopee muncul.")
    except Exception as e:
        print(f"Error pada login dengan nomor telepon: {e}")
    driver.get("https://shopee.co.id/buyer/login/otp")
    
    try:
        login_key_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "phone"))
        )
        
        login_key_input.send_keys(phone_number)
        print(f"Login dengan Nomor Telepon: Nomor '{phone_number}' diisi.")
        

        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "b5aVaf"))
        )
        next_button.click()
        print("Login dengan Nomor Telepon: Tombol 'Berikutnya' diklik.")
        
        try:
            send_to_whatsapp_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'b5aVaf') and contains(@class, 'PVSuiZ') and contains(@class, 'mo3UMT')]"))
            )
            send_to_whatsapp_button.click()
            print("Tombol 'Kirim ke WhatsApp' diklik.")
        except Exception as e:
            print("Tombol 'Kirim ke WhatsApp' tidak ditemukan atau tidak perlu diklik.")
    
        try:
            captcha_frame = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'captcha')]"))
            )
            print("Captcha ditemukan. Silakan selesaikan captcha.")
        
            WebDriverWait(driver, 60).until(
                EC.invisibility_of_element(captcha_frame)
            )
            print("Captcha terverifikasi. Lanjut ke OTP.")
        except Exception as e:
            print("Captcha tidak ditemukan atau tidak perlu diselesaikan.")
        
        otp_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "w_Qhj0")) 
        )
        print("Halaman untuk memasukkan OTP muncul.")

        otp = input("Masukkan OTP yang diterima: ")
        otp_input.send_keys(otp)
        print("Login dengan Nomor Telepon: OTP diisi.")

        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "b5aVaf"))
        )
        submit_button.click()
        print("Login dengan Nomor Telepon: Tombol 'Kirim' diklik.")
    
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "K9Pfb")) 
        )
        print("Login berhasil! Halaman beranda Shopee muncul.")
    except Exception as e:
        print(f"Error pada login dengan nomor telepon: {e}")
    driver.get("https://shopee.co.id/buyer/login/otp")
    
    try:
        login_key_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "phone"))
        )
        
        login_key_input.send_keys(phone_number)
        print(f"Login dengan Nomor Telepon: Nomor '{phone_number}' diisi.")

        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "b5aVaf"))
        )
        next_button.click()
        print("Login dengan Nomor Telepon: Tombol 'Berikutnya' diklik.")
        
        try:
            send_to_whatsapp_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'b5aVaf') and contains(@class, 'PVSuiZ') and contains(@class, 'mo3UMT')]"))
            )
            send_to_whatsapp_button.click()
            print("Tombol 'Kirim ke WhatsApp' diklik.")
        except Exception as e:
            print("Tombol 'Kirim ke WhatsApp' tidak ditemukan atau tidak perlu diklik.")
 
        otp_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "w_Qhj0"))
        )
        print("Halaman untuk memasukkan OTP muncul.")

        otp = input("Masukkan OTP yang diterima: ")
        otp_input.send_keys(otp)
        print("Login dengan Nomor Telepon: OTP diisi.")
        
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "b5aVaf"))
        )
        submit_button.click()
        print("Login dengan Nomor Telepon: Tombol 'Kirim' diklik.")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "K9Pfb"))
        )
        print("Login berhasil! Halaman beranda Shopee muncul.")
    except Exception as e:
        print(f"Error pada login dengan nomor telepon: {e}")

def register_with_phone(driver, phone_number):
    """Registrasi menggunakan nomor telepon."""
    driver.get("https://shopee.co.id/buyer/signup")
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "phone"))
        ).send_keys(phone_number)
        print(f"Nomor telepon '{phone_number}' diisi.")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "b5aVaf"))
        ).click()
        print("Tombol 'Berikutnya' diklik.")

        agree_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Setuju')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", agree_button) 
        agree_button.click()
        print("Tombol 'Setuju' diklik.")

        send_to_whatsapp_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Kirim ke WhatsApp')]"))
        )
        send_to_whatsapp_button.click()
        print("Tombol 'Kirim ke WhatsApp' diklik.")
        
        print("Captcha muncul. Silakan selesaikan captcha secara manual.")

        otp = input("Masukkan OTP yang diterima: ")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "otp"))
        ).send_keys(otp)
        print("OTP diisi.")

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "b5aVaf"))
        )
        submit_button.click()
        print("Login dengan Nomor Telepon: Tombol 'Kirim' diklik.")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "K9Pfb"))
        )
        print("Registrasi berhasil!")
    except Exception as e:
        print(f"Error pada proses registrasi: {e}")

def register_with_google(driver):
    """Registrasi Shopee menggunakan akun Google tanpa input manual email dan password."""
    driver.get("https://shopee.co.id/buyer/signup")
    
    try:
        google_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "z3yqC5"))
        )
        google_button.click()
        print("Tombol 'Lanjutkan dengan Google' diklik.")
        
        driver.switch_to.window(driver.window_handles[0])  # Pastikan fokus kembali ke tab Shopee
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "signup-complete"))
        )
        print("Registrasi dengan akun Google berhasil!")
    
    except Exception as e:
        print(f"Error pada registrasi dengan Google: {e}")

if __name__ == "__main__":
    driver = webdriver.Chrome()
    
    try:
        print("Pilih opsi:")
        print("1. Login dengan email dan password")
        print("2. Login dengan nomor telepon")
        print("3. Registrasi dengan nomor telepon")
        print("3. Registrasi dengan emial/telepon dan password")
        
        choice = input("Masukkan pilihan (1/2/3/4): ")

        if choice == "1":
            email = input("Masukkan email: ")
            password = input("Masukkan password: ")
            login_with_email(driver, email, password)
        elif choice == "2":
            phone_number = input("Masukkan nomor telepon: ")
            login_with_phone(driver, phone_number)
        elif choice == "3":
            phone_number = input("Masukkan nomor telepon: ")
            register_with_phone(driver, phone_number)
        elif choice == "4":
             register_with_google(driver)
        else:
            print("Pilihan tidak valid.")
    finally:
        driver.quit()
