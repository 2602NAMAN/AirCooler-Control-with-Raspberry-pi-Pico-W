# Smart-Cooler
Hello, I uses a Air Cooler at home for cooling my room in summer. It was around 7-8 years old and have 3-knobs for controlling the Fan, Pump, Swing functions in the cooler.

So, I wanted it to make control remotely by the help of some micro-controller, by the help of that want to control it 3 main function with the help of relays and add a timer to turn on or off it. There was a raspberry pi pico w lying around it uses micropython(lighter version of python) so i decided to use that. I made a simple web server which there are some buttons and timers.

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
There are some flaw in this as it was made by single person. (One known error is only one timer will work at a time). You and download and use it for your purpose.

Feel free to ask any queries or suggestion, I would appreciate any bug fix like I mentioned one above. 
