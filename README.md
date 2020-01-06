# Home Made Robot Arm
I wanted to create a wireless robot arm out of things I could find in my apartment. Then I realized I had nothing in my apartment and made it out of cardboard, popsicle sticks and hot glue. 

## List of Material and Tools:
- Raspberry pi 3 B (cana kit) 
- 5 ULN2003 driver board and stepper motor kit (amazon) 
- 4 AA battery holder (amazon)
- jute rope (hobby lobby)
- popsicle sticks (hobby lobby)
- cardboard (hobby lobby)
- 8 pack AA batteries (walgreens)
- Topelek hot melt glue gun (amazon)
- female to female jumper wires (amazon)
- tomato paste can (walmart? I think lol)
- straws (random food place)


## General Notes: 
### Motor Stuff
-  The stepper motor moves in full steps. For this to work, the coils have to be  energized in a particular order. I found this by looking at the stepper datasheet [here](http://eeshop.unl.edu/pdf/Stepper+Driver.pdf). 
- I also adapted this persons code [here]( https://tutorials-raspberrypi.com/how-to-control-a-stepper-motor-with-raspberry-pi-and-l293d-uln2003a/). But I had to switch libraries because RPi.GPIO wasnt being maintained and I had issues connecting to the PI.
- I simply adapted to a different library and created a class to simplify controlling multiple motors

### Controller Stuff
- [This](https://github.com/RetroPie/RetroPie-Setup/wiki/PS4-Controller) was good general reading for using a PS4 controller for non PS4 stuff.
- [This](https://pimylifeup.com/raspberry-pi-playstation-controllers/) was a great a write up for setting up the controller. 
- [This Stack Overflow answer]( https://stackoverflow.com/questions/46557583/how-to-identify-which-button-is-being-pressed-on-ps4-controller-using-pygame) had the button mappings which was helpful
- [This](https://html5gamepad.com/) allowed me to read the live values of the axes on the remote without having to fill up my command line.
