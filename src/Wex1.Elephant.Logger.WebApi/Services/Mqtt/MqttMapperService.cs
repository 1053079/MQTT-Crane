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
            }
        }

        private async Task HandleNewInputPayload(OnMessageReceivedEventArgs e)
        {
            switch (e.PublishMessage.Topic)
            {
                case "inputs/joystick":
                    await HandeNewJoystickInput(e.PublishMessage.Payload);
                    break;
            }
        }

        private async Task HandeNewJoystickInput(byte[]? payload)
        {
            var joystickInput = JsonSerializer.Deserialize<JoyStickDto>(payload);

            var newActionLog = new ActionLog
            {
                Id = ObjectId.GenerateNewId(),
                Component = "Joystick",
                EventType = "Action",
                Description = $"The Joystick moved {joystickInput.Direction} at a {joystickInput.Speed} and the spreader lock is {joystickInput.IsLocked}"
            };

            _mqttClient.PublishAsync("logger/actions",JsonSerializer.Serialize(newActionLog)).ConfigureAwait(false);
        }
    }
}
