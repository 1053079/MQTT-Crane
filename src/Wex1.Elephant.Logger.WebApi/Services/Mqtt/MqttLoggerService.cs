using HiveMQtt.Client;
using HiveMQtt.Client.Events;
using HiveMQtt.Client.Options;
using MongoDB.Bson;
using System.Diagnostics;
using System.Text.Json;
using Wex1.Elephant.Logger.Core;
using Wex1.Elephant.Logger.Core.Entities;
using Wex1.Elephant.Logger.Core.Interfaces.Mqtt;
using Wex1.Elephant.Logger.Core.Interfaces.Repositories;

namespace Wex1.Elephant.Logger.WebApi.Services.Mqtt
{
    public class MqttLoggerService : IMqttLoggerService
    {
        private readonly IErrorLogRepository _errorLogRepository;
        private readonly ISpeedLogRepository _speedLogRepository;
        private readonly IActionLogRepository _actionLogRepository;
        private readonly IPositionLogRepository _positionLogRepository;

        protected HiveMQClient _mqttClient { private set; get; }

        public MqttLoggerService(
            IErrorLogRepository errorLogRepository,
            ISpeedLogRepository speedLogRepository,
            IActionLogRepository actionLogRepository,
            IPositionLogRepository positionLogRepository)
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
            _errorLogRepository = errorLogRepository;
            _speedLogRepository = speedLogRepository;
            _actionLogRepository = actionLogRepository;
            _positionLogRepository = positionLogRepository;
        }

        public async Task CreateMqttClient(HiveMQClientOptions options)
        {
            _mqttClient = new HiveMQClient(options);
            await _mqttClient.ConnectAsync().ConfigureAwait(false);
            _mqttClient.AfterConnect += AfterConnectHandler;
            _mqttClient.OnMessageReceived += Client_OnMessageReceived;
            await _mqttClient.SubscribeAsync("logger/errors");
            await _mqttClient.SubscribeAsync("logger/speeds");
            await _mqttClient.SubscribeAsync("logger/actions");
            await _mqttClient.SubscribeAsync("logger/positions");
        }
        public void Client_OnMessageReceived(object? sender, OnMessageReceivedEventArgs e)
        {
            HandleMessageAsync(e);
        }
        void AfterConnectHandler(object? sender, AfterConnectEventArgs eventArgs)
        {
            Debug.WriteLine("connected");
        }

        public async Task HandleMessageAsync(OnMessageReceivedEventArgs e)
        {
            switch (e.PublishMessage.Topic)
            {
                case "logger/errors":
                    await HandleNewErrorLog(e.PublishMessage.Payload);
                    break;
                case "logger/speeds":
                    await HandleNewSpeedLog(e.PublishMessage.Payload);
                    break;
                case "logger/actions":
                    await HandleNewActionLog(e.PublishMessage.Payload);
                    break;
                case "logger/positions":
                    await HandleNewPositionLog(e.PublishMessage.Payload);
                    break;

            }
        }



        private async Task HandleNewErrorLog(byte[]? payload)
        {
            var errorLogInfo = JsonSerializer.Deserialize<ErrorLog>(payload);

            var newErrorLog = new ErrorLog
            {
                Id = ObjectId.GenerateNewId(),
                EventTimeStamp = errorLogInfo.EventTimeStamp,
                Component = errorLogInfo.Component,
                Description = errorLogInfo.Description,
                EventType = errorLogInfo.EventType
            };

            await _errorLogRepository.AddAsync(newErrorLog);
        }
        private async Task HandleNewSpeedLog(byte[]? payload)
        {
            var speedLogInfo = JsonSerializer.Deserialize<SpeedLog>(payload);

            var newSpeedLog = new SpeedLog
            {
                Id = ObjectId.GenerateNewId(),
                EventTimeStamp = speedLogInfo.EventTimeStamp,
                Component = speedLogInfo.Component,
                Description = speedLogInfo.Description,
                EventType = speedLogInfo.EventType,
                Speed = speedLogInfo.Speed
            };

            await _speedLogRepository.AddAsync(newSpeedLog);
        }
        private async Task HandleNewActionLog(byte[]? payload)
        {
            var actionLogInfo = JsonSerializer.Deserialize<ActionLog>(payload);

            var newActionLog = new ActionLog
            {
                Id = ObjectId.GenerateNewId(),
                EventTimeStamp = actionLogInfo.EventTimeStamp,
                Component = actionLogInfo.Component,
                Description = actionLogInfo.Description,
                EventType = actionLogInfo.EventType
            };

            await _actionLogRepository.AddAsync(newActionLog);
        }

        private async Task HandleNewPositionLog(byte[]? payload)
        {
            var positionLogInfo = JsonSerializer.Deserialize<PositionLog>(payload);

            var newPositionLog = new PositionLog
            {
                Id = ObjectId.GenerateNewId(),
                EventTimeStamp = positionLogInfo.EventTimeStamp,
                Component = positionLogInfo.Component,
                Description = positionLogInfo.Description,
                EventType = positionLogInfo.EventType,
                Position = positionLogInfo.Position
            };

            await _positionLogRepository.AddAsync(newPositionLog);
        }
    }
}
