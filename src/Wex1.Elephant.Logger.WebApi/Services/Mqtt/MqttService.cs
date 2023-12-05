using HiveMQtt.Client;
using HiveMQtt.Client.Events;
using HiveMQtt.Client.Options;
using MongoDB.Bson;
using MongoDB.Bson.IO;
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

        protected HiveMQClient _mqttClient { private set; get; }

        public MqttService(IErrorLogRepository errorLogRepository)
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
        }

        public async Task CreateMqttClient(HiveMQClientOptions options)
        {
            _mqttClient = new HiveMQClient(options);
            await _mqttClient.ConnectAsync().ConfigureAwait(false);
            _mqttClient.AfterConnect += AfterConnectHandler;
            _mqttClient.OnMessageReceived += Client_OnMessageReceived;
            await _mqttClient.SubscribeAsync("Logger/Errors");
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
            //Example of event payload
            //{"EventTimeStamp":"2023-12-05T10:56:22.9110133Z","EventType":"test","Component":"test","Description":"test"}
            switch (e.PublishMessage.Topic)
            {
                case "Logger/Errors":
                    HandleNewErrorLog(e.PublishMessage.Payload);
                    break;
            }

        }

        private async Task HandleNewErrorLog(byte[] payload)
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
    }
}
