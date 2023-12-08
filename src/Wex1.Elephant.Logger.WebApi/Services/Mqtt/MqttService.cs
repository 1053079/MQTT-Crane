using HiveMQtt.Client;
using HiveMQtt.Client.Events;
using HiveMQtt.Client.Options;
using MongoDB.Bson;
using MongoDB.Driver;
using System.Diagnostics;
using System.Text.Json;
using Wex.Elephant.Logger.Infrastructure.Repositories;
using Wex1.Elephant.Logger.Core;
using Wex1.Elephant.Logger.Core.Entities;
using Wex1.Elephant.Logger.Core.Interfaces.Mqtt;
using Wex1.Elephant.Logger.Core.Interfaces.Repositories;

namespace Wex1.Elephant.Logger.WebApi.Services.Mqtt
{
    public class MqttService : IMqttService
    {
        private readonly IErrorLogRepository _errorLogRepository;
        private readonly ISpeedLogRepository _speedLogRepository;
        private readonly IActionLogRepository _actionLogRepository;
        private readonly IPositionLogRepository _positionLogRepository;

        protected HiveMQClient _mqttClient { private set; get; }

        public MqttService(
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
            errorLogRepository = new ErrorLogRepository();
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
            await _mqttClient.SubscribeAsync("Logger/Errors");
            await _mqttClient.SubscribeAsync("Logger/Speeds");
            await _mqttClient.SubscribeAsync("Logger/Action");
            await _mqttClient.SubscribeAsync("Logger/Positions");
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
                case "Logger/Errors":
                    await HandleNewErrorLog(e.PublishMessage.Payload);
                    break;
                case "Logger/Speeds":
                    await HandleNewSpeedLog(e.PublishMessage.Payload);
                    break;
                case "Logger/Actions":
                    await HandleNewActionLog(e.PublishMessage.Payload);
                    break;
                case "Logger/Positions":
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
