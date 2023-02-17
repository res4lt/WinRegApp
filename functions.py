import winreg

def deactive_device(): # Bilgisayara takılan USB depolama cihazlarının algılanmamasını sağlar!
    h_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Services\\USBSTOR", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(h_key, "Start", 0, winreg.REG_DWORD, 4)
    winreg.CloseKey(h_key)
def active_device(): # Bilgisayara takılan USB depolama cihazlarının algılanma durumunu aktif duruma getirir!
    h_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Services\\USBSTOR", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(h_key, "Start", 0, winreg.REG_DWORD, 3)
    winreg.CloseKey(h_key)
def active_firewall(): # Windows güvenlik duvarını aktif duruma getirir!
    h_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\ControlSet001\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(h_key, "EnableFirewall", 0, winreg.REG_DWORD, 1)
    winreg.CloseKey(h_key)
def deactive_firewall(): # Windows güvenlik duvarını devre dışı bırakmanızı sağlar!
    h_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\ControlSet001\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(h_key, "EnableFirewall", 0, winreg.REG_DWORD, 0)
    winreg.CloseKey(h_key)
'''
def execute(): # Başlangıç da yürütülmek istenen program.
    h_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(h_key, "RegWinApp", 0, winreg.REG_SZ, '"dosyasının yolu."')
    winreg.CloseKey(h_key)
'''

