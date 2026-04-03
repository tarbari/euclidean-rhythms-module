# Notes for RP2040 development

## Links

- [Tutorial Book](https://rp2040.implrust.com/index.html)
- [Connect USB to WSL](https://learn.microsoft.com/en-us/windows/wsl/connect-usb)

----------

## Installing WSL2 environment

```bash
# Install dependencies
sudo apt install build-essential pkg-config libusb-1.0-0-dev cmake

mkdir embedded && cd embedded

# Clone the Pico SDK
git clone https://github.com/raspberrypi/pico-sdk
cd pico-sdk
git submodule update --init lib/mbedtls
cd ../


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# This step might be unnecessary.. maybe?     #
# We set the variable when building picotool, #
# and when building/flashing RP2040 this is   #
# not needed.                                 #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# Set the environment variable for the Pico SDK
PICO_SDK_PATH=/MY_PATH/embedded/pico-sdk

# Clone the Picotool repository
git clone https://github.com/raspberrypi/picotool

# Build and install picotool
cd picotool
mkdir build && cd build
cmake -DPICO_SDK_PATH=/MY_PATH/embedded/pico-sdk/ ../
make -j8
sudo make install
cd ..

# In picotool cloned directory
sudo cp udev/60-picotool.rules /etc/udev/rules.d/

# Add appropriate target for Rust to build for RP2040
rustup target add thumbv6m-none-eabi
```

----------

## Passing USB from Windows to WSL

See the install instructions in [Links].
Note that `usbipd` is used from PowerShell.

Connect the device to windows (RP2040 must be in BOOTSEL mode) to make it
visible in the usb listings... 

Replace the bus id in the following table with the one you want in case it is
not correct.

Binding requires administrator privileges.

| Command                           | Explanation                           |
| --------------------------------- | ------------------------------------- |
| `usbipd list`                     | List usb devices and their bus id's   |
| `usbipd bind --busid 6-4`         | To make the device attachable to WSL  |
| `usbipd attach --wsl --busid 6-4` | Attach the device to WSL              |
| `usbipd detach --busid 6-4`       | Detach the device. Or just pull plug. | 

In WSL you can do `lsusb` to see devices if necessary.

### Workflow

1. Do code
2. Attach Pico in BOOTSEL mode to USB
3. Make sure it's attachable (list)
4. Attach
5. Flash

----------

## Project Template

`cargo generate --git https://github.com/ImplFerris/rp2040-embassy-template.git --tag v0.1.4`
Alias `generate-embassy`

This will create a new directory. It will also ask if you have a debug probe -
you don't... at least for now.

The template has `.cargo/config.toml` setup so that executing `cargo run`
invokes `picotool` and flashes the program to a pico that is found in the usb
devices. "A pico" is intentionally vague, it probably selects the first that is
found.
