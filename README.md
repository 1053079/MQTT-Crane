# st-2324-1-d-wx1-t7-2324-wx1-elephant
st-2324-1-d-wx1-t7-2324-wx1-elephant created by GitHub Classroom

# LoginDetails
## HiveMq
Email | Username | Password | Cluster Url | Port | Websocket Port
----- | -------- | --------- | ----------- | ---- | -------------
Xander.Van.Boom@Student.howest.be | Admin | hMu4P6L_LAMj8t3 | 2939d3617acc492aa3b3653ac474fdc0.s2.eu.hivemq.cloud | 8883 | 8884
## Mongodb
 Username | Password | ConnectionUrl | ProjectId
 -------- | -------- | ------------ | ---------- 
 Admin | Password | mongodb+srv://Admin:Password@wx1-elephants-mongodb.kizgodk.mongodb.net/?retryWrites=true&w=majority | 656d8b753ec677651f807584
# Database Infrastructure
## Collections
 Errors | Actions | Positions | Speeds
 ------ | ------- | --------- | ------ 
 Id     | Id | Id | Id
 Type   | Type | Type | Type
 Timestamp | Timestamp | Timestamp | Timestamp
 Description | Description | Description | Description
  | | | x, y, z | Speed

# Logger
## Api endpoints
- **Api/Errors** -> returns a paged list of all error logs
- **Api/Speeds** -> returns a paged list of all speed logs
- **Api/Actions** -> returns a paged list of all action logs
- **Api/Positions** -> returns a paged list of all position logs

## MqttService
### Description
The MqttService has to subscribe to all the Logger/{LogType} Mqtt endpoints. one it receives a message it will filter what LogType it is and create a new log in the matching collection and upload this to the database.
### Payloads
#### *Error log payload*
**Property Names** | TimeStamp | EventType | Component | Description
------------------ | --------- | --------- | --------- | ----------
**Data Type** | DateTime | string | string | string
#### *Speed log payload*
**Property Names** | TimeStamp | EventType | Component | Description | Speed
------------------ | --------- | --------- | --------- | ----------- | ----
**Data Type** | DateTime | string | string | string | double
#### *Action log payload*
**Property Names** | TimeStamp | EventType | Component | Description
------------------ | --------- | --------- | --------- | ----------
**Data Type** | DateTime | string | string | string
#### *Position log payload*
**Property Names** | TimeStamp | EventType | Component | Description | Position
------------------ | --------- | --------- | --------- | ----------- | --------
**Data Type** | DateTime | string | string | string | List\<double>(X,Y,Z)
### Payload Examples
- ErrorLog ->
```{"EventTimeStamp":"2023-12-05T10:56:22.9110133Z","EventType":"Error","Component":"joystick","Description":"joystick downwards movement is broken"}```
- SpeedLog ->
```{"EventTimeStamp":"2023-12-05T10:56:22.9110133Z","EventType":"Speed","Component":"HoistMotor","Description":"Moving Up", "Speed":50}```
- PositionLog ->
```{"EventTimeStamp":"2023-12-05T10:56:22.9110133Z","EventType":"Position","Component":"Spreader","Description":"Spreader moved downwards","Position":[15,10,8]}```
- ActionLog ->
```{"EventTimeStamp":"2023-12-05T10:56:22.9110133Z","EventType":"Action","Component":"joystick","Description":"Joystick send a forward movement"}```
# Spreader 
De spreader luistert naar de volgende topics: "inputs/joystick" en "outputs/positionSpreader".
Met het topic outputs/positionSpreader weten we wanneer de sensoren de container detecteren en dus wanneer hij kan locken.
Met het topic inputs/joystick kijken we of de gebruiker de container effectief wil locken, dit gebeurd via volgende payload:
payload = {"movement": movement, "speed": speed, "lock": lock}
De spreader kijkt ook waar hij zich bevind zodat deze niet zomaar kan unlocken boven de zee en dat dit enkel in het doelgerichte gebied (sts-kraan) is.

De topics die de spreader verstuurt zijn twee verschillende --> een voor wanneer hij de sensor van de spreader de container detecteert,
een zodat de spreader kan locken op de container en kan unlocken in het gerichte doelgebied. Hieronder zie je de volgende topics
![Alt text](images/spreaderTopics.png)

 
