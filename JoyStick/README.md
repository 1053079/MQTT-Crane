![Image](https://i.imgur.com/qmpedG0.png)
The image above is an example of publishing data to the MQTT broker.  
It successfully connects and publishes data to the MQTT broker.

## Requirements

These Python packages are required for running:

    
    pip install paho-mqtt
    pip install keyboard
    

## Description

The main purpose of this script is to capture Keyboard input and send them to the MQTT broker. Together with speed controls, spreader locks/unlocks, this is an important part of the project.

## Crane movements and spreader lock/unlock

- **W + A** = forwardLeft
- **W + D** = forwardRight
- **S + A** = backwardLeft
- **S + D** = backwardRight
- **W** = forward
- **A** = left
- **S** = backward
- **D** = right
- **Up Arrow** = up
- **Down Arrow** = down
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