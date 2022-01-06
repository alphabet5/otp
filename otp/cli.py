
def get_or_set_password(service, username):
    import keyring
    creds = keyring.get_password(service, username)
    if creds is None:
        import tkinter as tk
        from tkinter.simpledialog import askstring
        root = tk.Tk()
        root.withdraw()
        password = askstring('Password', 'Enter password:', show="*")
        import getpass
        keyring.set_password(service,
                             username,
                             password) # getpass.getpass('Enter the password for ' + service + ', username:' + username + ':'))
        creds = keyring.get_password(service, username)
    return creds


def main():
    import pyotp
    import datetime
    import pyautogui
    import sys
    from urllib.parse import parse_qs, urlparse
    try:
        otp_name = sys.argv[1]
        otp_url = get_or_set_password('otp', otp_name)
        secret = parse_qs(urlparse(otp_url).query)['secret'][0]
        totp = pyotp.TOTP(secret)
        totp.interval - datetime.datetime.now().timestamp() % totp.interval
        pyautogui.typewrite(totp.now())
    except:
        import traceback
        from tkinter import messagebox
        messagebox.showerror("Error", message=traceback.format_exc())
