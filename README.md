# RasperrYún

Scripts and patches to run the Yún bridge libraries on Raspberry Pi on Debian based operating systems (later also Banana Pi). Currently only Debian Wheezy is supported.

This repository will be deleted when everything is cleaned up and moved to https://github.com/mschlenker/nuage! Nuage moves to serial upload instead of bitbanging GPIO to use SPI to program the AVR, thus leaving SPI unconnected.

Tested: 

* Console
* Mailbox
* File Write
* Simple web interface for getting/setting variables

Missing:

* Reset the AVR upon reboot
* Blink some LED during sketch upload
* Automatically detect different AVRs add boot time

