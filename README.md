# Smart-Cooler
I have been using an air cooler to cool my room during the summer for the past 7-8 years. The cooler features three control knobs for managing the fan, pump, and swing functions. To modernize this device and enable remote control, I decided to incorporate a microcontroller.

I opted to use a Raspberry Pi Pico W, which runs MicroPython—a lightweight version of Python—since I had one available. My goal was to control the cooler's three main functions using relays and add a timer feature for scheduled operation.

To achieve this, I developed a simple web server with a user interface that includes buttons and timers. This setup allows for remote control and scheduling of the air cooler's fan, pump, and swing functions, providing enhanced convenience and efficiency.


# Hardware Requirements -
1. Raspberry pi pico W
2. Logic Level Shifter (as pico operates on 3.3v and relay operates on 5v, So to convert the 3.3v singals to 5v)
3. 5v Relay (x3 for Fan, Pump, Swing seperate)
4. Some jumper wires
5. 5v volt power adapter (to power pico W)
6. Computer for programming the board (i used Thonny IDE)


## The web server will look like this-

![image](https://github.com/2602NAMAN/Smart-Cooler/assets/113130600/13efec93-9ee7-4451-8725-d6df9587e0fa)

> Here first timer is to turn off all 3 relay off after the given time(hh:mm).

> Then there are 3 button to turn on or off the relays.

> AT the bottom the timer will run in loop to turn on or off the pump (this will help in control the humidity of the room)

## Circuit Diagram- (pretty stright forword)

![image](https://github.com/2602NAMAN/Smart-Cooler/assets/113130600/36ed3e5d-a3b5-473b-abee-c979617a9c57)

## Flaws-
Please note that this project was developed by a single person and may have some flaws. One known issue is that only one timer can function at a time. You are welcome to download and use the system for your purposes.

Feel free to reach out with any queries or suggestions. I would greatly appreciate any assistance with bug fixes, such as resolving the timer issue mentioned above.
