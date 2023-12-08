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