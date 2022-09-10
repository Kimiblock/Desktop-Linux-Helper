pkgToInstall='libva-mesa-driver mesa-vdpau gstreamer-vaapi radeontop'
aurToInstall=amf-amdgpu-pro
sudo pacman -Sy
sudo pacman -Syyu
sudo pacman -S ${pkgToInstall}
if [ `pacman -Q | grep yay` ]; then
    yay -S ${aurToInstall}
fi
sudo bash -c 'echo LIBVA_DRIVER_NAME=radeonsi >>/etc/environment'
sudo bash -c 'echo VDPAU_DRIVER=radeonsi >>/etc/environment'
sudo bash -c 'echo GST_VAAPI_ALL_DRIVERS=1 >>/etc/environment'
