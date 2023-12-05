# st-2324-1-d-wx1-t7-2324-wx1-elephant
st-2324-1-d-wx1-t7-2324-wx1-elephant created by GitHub Classroom
# Logger
## Api endpoints
- **Api/Errors** -> returns a paged list of all error logs

## MqttService
### Description
The MqttService has to subscribe to all the Logger/{LogType} Mqtt endpoints. one it receives a message it will filter what LogType it is and create a new log in the matching collection and upload this to the database.
### Payload
#### *Error log payload*
**Property Names** | TimeStamp | EventType | Component | Description
-------------- | --------- | --------- | --------- | ----------
**Data Type** | DateTime | string | string | string

