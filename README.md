# flipTheSwitch
Files needed to be able to remotely switch between Windows and Linux 

The updated write up/Instructions/video instructions for this project can be found on my web page https://fazalali.me/blog/remotely-change-os-while-dual-booting-windows-and-linux/
Here is an archive of the above. 

**Remotely change OS while Dual Booting Windows and Linux**

Ever since I started dual booting Windows and Linux, the lack of flexibility has bothered me. If I am out but want to work on my projects, I needed to have my computer running Linux. If I wanted to use something like Steam Link to play my Windows games, I needed to have my computer running Windows. After some head scratching and furious typing, I found my solution.

**Note:** This requires prior setup. If you are in a situation where you need to switch operating systems right now, you may be able to follow the steps and set it up remotely – but there are a lot of problems (depending on your machine) that can occur which might require physical access.

**TLDR / Table of contents:**
1. Install Grub2Win on your Windows machine.
2. Download the files from github here and set them up according to the “File setup” section.
3. Mount your Windows partition on boot
4. Enjoy???
--

**1. Install Grub2Win on your Windows Machine.**
1. Download, install, and setup Grub2Win (SourceForge Link)
2. Ensure that your C: drive now has a folder named “grub2”

Reboot and check if you can use Grub2Win to boot into either OS correctly.

**Why Grub2Win?** Unfortunately, the boot loader of choice, GRUB, won’t cut it. Linux can easily edit Windows files but Windows cannot easily edit Linux files. For this set up to work, you need to be able to edit files no matter what filesystem they are in. Until Windows supports the Linux filesystem, this is the only way I was able to get it to work.

**2. File Setup**
Once you have Grub2Win installed, the rest of the setup just involves editing some files and saving them in specific places. To download the files, go to my github repo here.

I have organized them so they are easier to recognize. The following bold text represents the folder name (from the files you just downloaded) and the part after the hypen (“-“) is where you would put them.

**Grub2 Files** – put these in your “grub2” folder that was created when you installed Grub2Win. It should be in “C:/grub2/” if you didn’t change the defaults.

**Linux Files** – There’s only one file here called “make it windows.sh”. You can put this on your Linux desktop or wherever you like. This is script you call when you want to remotely change OS

**Windows Files** – Again, there’s only one file here called “make it linux.bat”. You can also put this on your Windows desktop.

(Optional: If you’d like to make it all pretty, you can checkout the “optional” sub directories in “Linux Files” and “Windows Files”.)

**3. Mount Windows partition on when your Linux distro boots**

Windows has weird features like “fast startup” that mess with dual booting. You need to turn off fast startup and hibernation in order for Linux to correctly mount your Windows partition. You can find the steps on how to do that here.

Once you have fast startup/hibernation disabled, you can set up your Linux distro to always mount your Windows partition on startup using fstab. You can find the steps on how to do that here. Remember, you need to auto mount your Windows partition.

After you have done that, while still in Linux, go to your mounted Windows partition and try creating a folder. If you can, it means you can successfully write to your Windows partition (YAY).

**4. That’s it.**
That’s it. You should now be able to use the “make it windows.sh” and “make it linux.bat” scripts to remotely (or even if you are physically present) change your Operating System. If you’d like to make it a little prettier looking, you can follow the instructions in the “optional” sub directories as mentioned before BUT even without it you are all good to go.

If you have any problems following this guide, please let me know via email or by creating a github issue. I will also be making a video on setting this up and I shall update this post when I do. Thank you and have fun!
