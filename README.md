# Minimal PlatformIO prj for TTGO T-Beam SX126x using TTN on AU915

##  Project Demos This:
* Hardware: Lilygo TTGO T-Beam T22 v1.1 (ESP32, LoRaWAN SX1262/SX126x, NOT SX127x) https://github.com/LilyGO/TTGO-T-Beam
* LoRaWAN/TTN Community Stack (v3) registration via ABP
* LoRaWAN frequency for TTN Australia AU915 (SB2, CH 8-15)
* PlatformIO IDE

##  Overcomes challenges:
* Most LMIC libraries dont support SX1262/SX126x
* Little evidence of working tests on AU915

## Thanks to the following for providing the hints for this to work:
* https://github.com/LacunaSpace/basicmac which supports the SX1262/SX126x and provides easy Arduino compatibility
* https://github.com/thomaslaurenson/Dragino_LoRaShield_Node_AU915 for the AU915 secrets
