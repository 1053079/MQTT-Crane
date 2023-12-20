using HiveMQtt.Client;
using HiveMQtt.Client.Events;
using HiveMQtt.Client.Options;
using MongoDB.Bson;
using System.Text.Json;
using Wex1.Elephant.Logger.Core;
using Wex1.Elephant.Logger.Core.Dto.MqttInputs;
using Wex1.Elephant.Logger.Core.Entities;
using Wex1.Elephant.Logger.Core.Interfaces.Mqtt;

namespace Wex1.Elephant.Logger.WebApi.Services.Mqtt
{
    public class MqttMapperService : IMqttMapperService
    {
        private HiveMQClient _mqttClient;
        public MqttMapperService()
        {
            var options = new HiveMQClientOptions
            {
                UserName = Constants.MqttUserName,
                Password = Constants.MqttPassword,
                Port = Constants.MqttPort,
                Host = Constants.MqttClusterUrl,
                UseTLS = true,
            };

            CreateMqttClient(options);
        }

        public async Task CreateMqttClient(HiveMQClientOptions options)
        {
            _mqttClient = new HiveMQClient(options);
            await _mqttClient.ConnectAsync().ConfigureAwait(false);
            _mqttClient.OnMessageReceived += Client_OnMessageReceived;
            await _mqttClient.SubscribeAsync("inputs/#");
            await _mqttClient.SubscribeAsync("outputs/#");
            await _mqttClient.SubscribeAsync("positions/#");
            await _mqttClient.SubscribeAsync("speeds/#");
        }
        public void Client_OnMessageReceived(object? sender, OnMessageReceivedEventArgs e)
        {
            HandleMessageAsync(e);
        }

        public async Task HandleMessageAsync(OnMessageReceivedEventArgs e)
        {
            switch (e.PublishMessage.Topic)
            {
                case var topic when topic.StartsWith("inputs/"):
                    await HandleNewInputPayload(e);
                    break;
                case var topic when topic.StartsWith("outputs/"):
                    await HandleNewOutputPayload(e);
                    break;
                case var topic when topic.StartsWith("positions/"):
                    await HandleNewPositionPayload(e);
                    break;
                case var topic when topic.StartsWith("speeds/"):
                    await HandleNewSpeedPayload(e);
                    break;
            }
        }

        private Task HandleNewSpeedPayload(OnMessageReceivedEventArgs e)
        {
            throw new NotImplementedException();
        }

        private Task HandleNewPositionPayload(OnMessageReceivedEventArgs e)
        {
            throw new NotImplementedException();
        }

        private async Task HandleNewOutputPayload(OnMessageReceivedEventArgs e)
        {
            switch(e.PublishMessage.Topic)
            {
                case "outputs/motorCrane":
                    await HandleNewMotorCraneOutput(e.PublishMessage.Payload);
                    break;
                case "outputs/motorHoist":
                    await HandleNewMotorHoistOutput(e.PublishMessage.Payload);
                    break;
                case "outputs/motorCabin":
                    await HandleNewMotorCabinOutput(e.PublishMessage.Payload);
                    break;
                case "outputs/positionSpreader":
                    await HandleNewSpreaderPositionOutput(e.PublishMessage.Payload);
                    break;
                case "outputs/actionSpreader":
                    await HandleNewActionSpreaderOutput(e.PublishMessage.Payload);
                    break;
                case "outputs/sensorSpreader":
                    await HandleNewSensorSpreaderOutput(e.PublishMessage.Payload);
                    break;
                

            }
        }

        private async Task HandleNewSensorSpreaderOutput(byte[]? payload)
        {
            var sensorSpreader = JsonSerializer.Deserialize<SensorSpreaderDto>(payload);
            var actionLog = new ActionLog
            {
                Id = ObjectId.GenerateNewId(),
                Component = "Spreader",
                EventType = "Action",
                Description = $"{(sensorSpreader.sensorValue ? "The sensor has detected a container" : "The sensor has not detected a conatiner")}",
                EventTimeStamp = DateTime.UtcNow
            };
            _mqttClient.PublishAsync("logger/actions", JsonSerializer.Serialize(actionLog));
        }

        private async Task HandleNewActionSpreaderOutput(byte[]? payload)
        {
            var spreaderAction = JsonSerializer.Deserialize<ActionSpeaderDto>(payload);
            var actionLog = new ActionLog
            {
                Id = ObjectId.GenerateNewId(),
                Component = "Spreader",
                EventType = "Action",
                Description = $"The spreader is {(spreaderAction.IsLocked ? "Locked" : "UnLocked")} and {(spreaderAction.HasContainer ? "has a container" : "has no container")}",
                EventTimeStamp = DateTime.UtcNow
            };
            _mqttClient.PublishAsync("logger/actions", JsonSerializer.Serialize(actionLog));
        }

        private async Task HandleNewSpreaderPositionOutput(byte[]? payload)
        {
            var positionSpreader = JsonSerializer.Deserialize<PositionDto>(payload);
            var position = new List<double> { positionSpreader.X, positionSpreader.Y };
            var positionLog = new PositionLog
            {
                Id = ObjectId.GenerateNewId(),
                Component = "Spreader",
                EventType = "Position",
                Position = position,
                Description = $"The current position of the spreader is X:{positionSpreader.X}Y:{positionSpreader.Y}",
                EventTimeStamp = DateTime.UtcNow
            };
            
            _mqttClient.PublishAsync("logger/positions", JsonSerializer.Serialize(positionLog));
        }

        private async Task HandleNewMotorCabinOutput(byte[]? payload)
        {
            var motorCrane = JsonSerializer.Deserialize<motorDto>(payload);
            var actionLog = new ActionLog
            {
                Id = ObjectId.GenerateNewId(),
                Component = "MotorCabin",
                EventType = "Action",
                Description = $"The motor for the cabin is moving {motorCrane.Direction} at a {motorCrane.Speed} speed",
                EventTimeStamp = DateTime.UtcNow
            };

            _mqttClient.PublishAsync("logger/actions", JsonSerializer.Serialize(actionLog));
        }

        private async Task HandleNewMotorHoistOutput(byte[]? payload)
        {
            var motorCrane = JsonSerializer.Deserialize<motorDto>(payload);
            var actionLog = new ActionLog
            {
                Id = ObjectId.GenerateNewId(),
                Component = "MotorHoist",
                EventType = "Action",
                Description = $"The motor for the hoist is moving {motorCrane.Direction} at a {motorCrane.Speed} speed",
                EventTimeStamp = DateTime.UtcNow
            };

            _mqttClient.PublishAsync("logger/actions", JsonSerializer.Serialize(actionLog));
        }

        private async Task HandleNewMotorCraneOutput(byte[]? payload)
        {
            var motorCrane = JsonSerializer.Deserialize<motorDto>(payload);
            var actionLog = new ActionLog
            {
                Id = ObjectId.GenerateNewId(),
                Component = "MotorCrane",
                EventType = "Action",
                Description = $"The motor for the crane is moving {motorCrane.Direction} at a {motorCrane.Speed} speed",
                EventTimeStamp = DateTime.UtcNow
            };

            _mqttClient.PublishAsync("logger/actions", JsonSerializer.Serialize(actionLog));
        }

        private async Task HandleNewInputPayload(OnMessageReceivedEventArgs e)
        {
            switch (e.PublishMessage.Topic)
            {
                case "inputs/joystick":
                    await HandleNewJoystickInput(e.PublishMessage.Payload);
                    break;
                case "inputs/cabinEmergencyButton":
                    await HandleNewCabinEmergencyButton(e.PublishMessage.Payload);
                    break;
            }
        }

        private async Task HandleNewCabinEmergencyButton(byte[]? payload)
        {
            var CabinEmergencyBtn = JsonSerializer.Deserialize<EmergencyButtonDto>(payload);

            var newActionLog = new ActionLog
            {
                Id = ObjectId.GenerateNewId(),
                Component = "CabinEmergencyButton",
                EventType = "Action",
                Description = CabinEmergencyBtn.IsPressed ? "Cabin emergency button was engaged." : "Cabin emergency button was unengaged.",
                EventTimeStamp = DateTime.UtcNow
            };

            _mqttClient.PublishAsync("logger/actions", JsonSerializer.Serialize(newActionLog)).ConfigureAwait(false);
        }

        private async Task HandleNewJoystickInput(byte[]? payload)
        {
            var joystickInput = JsonSerializer.Deserialize<JoyStickDto>(payload);
            var newActionLog = new ActionLog
            {
                Id = ObjectId.GenerateNewId(),
                Component = "Joystick",
                EventType = "Action",
                Description = $"The Joystick moved {joystickInput.Direction} at a {joystickInput.Speed} and the spreader lock is {(joystickInput.IsLocked ? "Locked" : "Unlocked")}.",
                EventTimeStamp = DateTime.UtcNow

            };

            _mqttClient.PublishAsync("logger/actions", JsonSerializer.Serialize(newActionLog)).ConfigureAwait(false);
        }

    }
}
