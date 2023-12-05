![Image](https://i.imgur.com/qmpedG0.png)
The image above is an example of publishing data to the MQTT broker.  
It successfully connects and publishes data to the MQTT broker.

## Issues/User Stories
- Create the logic for the joystick [8] | [Screenshot of issue](https://i.imgur.com/mGofE4w.png)
- Update Joystick to use variable speed [3] | [Screenshot of issue](https://i.imgur.com/DJFMqq8.png)


## Requirements

These Python packages are required for running:

    
    pip install paho-mqtt
    pip install keyboard
    

## Description

The main purpose of this script is to capture Keyboard input and send them to the MQTT broker. Together with speed controls, spreader locks/unlocks, this is an important part of the project.

## Crane movements and spreader lock/unlock

- **W**
- **A**
- **S**
- **D**
- **Up Arrow**
- **Down Arrow**
- **Enter:** Toggle lock/unlock spreader

## Speed control of the crane with shift/ctrl

The speed of movement is determined by additional keys:

- **Shift:** Fast speed
- **Ctrl:** Slow speed

## MQTT Publishing

The script publishes MQTT messages with the following payload:

```json
{
    "movement": "current_movement",
    "speed": "current_speed",
    "lock": true_or_false
}
