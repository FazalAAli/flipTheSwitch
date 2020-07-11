#windows to ubuntu
import os
if os.path.exists("grub-ubuntu.cfg"):
    os.rename("grub.cfg", "grub-windows.cfg")
    os.rename("grub-ubuntu.cfg", "grub.cfg")