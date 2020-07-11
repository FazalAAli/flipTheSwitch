#ubuntu to windows
import os
if os.path.exists("grub-windows.cfg"):
    os.rename("grub.cfg", "grub-ubuntu.cfg")
    os.rename("grub-windows.cfg", "grub.cfg")