using HiveMQtt.Client;
using HiveMQtt.Client.Events;
using HiveMQtt.Client.Options;
using Wex1.Elephant.Spreader.Core;
using Wex1.Elephant.Spreader.Core.Interfaces.Mqtt;
using Wex1.Elephant.Logger.Core.Entities;
using MongoDB.Bson.IO;
using System.Text;
using System.Text.Json;
using System.Diagnostics;
using Wex1.Elephant.Spreader.Core.Entities;
using System.Net.Sockets;
using Amazon.Util.Internal;

namespace Wex1.Elephant.Spreader.ConsoleApp.Services.Mqtt
{
    public class MqttService : IMqttService
    {
        public HiveMQClient _mqttClient { set; get; }
        private Spreaders _spreader = new Spreaders();
        public MqttService()
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

            _mqttClient.OnMessageReceived += _mqttClient_OnMessageReceived;
            _mqttClient.AfterConnect += AfterConnectHandler;
            await _mqttClient.ConnectAsync().ConfigureAwait(false);
            await SubscribePositionSpreader();
            await SubscribeJoystick();



        }
        void AfterConnectHandler(object? sender, AfterConnectEventArgs eventArgs)
        {
            Console.WriteLine("connected");
        }

        public void _mqttClient_OnMessageReceived(object? sender, OnMessageReceivedEventArgs e)
        {
            HandleMessageAsync(e);
        }
        public async Task HandleMessageAsync(OnMessageReceivedEventArgs e)
        {
            if (e.PublishMessage.Topic == "outputs/positionSpreader")
            {
                var payload = e.PublishMessage.PayloadAsString;
                Console.WriteLine(payload);
                double positionValue = double.Parse(payload);
                if (positionValue == 0.0)
                {
                    _spreader.Sensor.DetectedContainer = true;

                    if (_spreader.Sensor.DetectedContainer)
                    {

                        await PublishSensorStatus(true);
                    }
                    else
                    {
                        await PublishSensorStatus(false);
                    }
                }

            }
            else if (e.PublishMessage.Topic == "outputs/actionSpreader")
            {
                var payload = e.PublishMessage.PayloadAsString;
                Console.WriteLine(payload);
            }
            else if (e.PublishMessage.Topic == "inputs/joystick")
                    {
                
                var payload = e.PublishMessage.PayloadAsString;
                Console.WriteLine(payload);
                var payloadData = JsonSerializer.Deserialize<Dictionary<string, object>>(payload);

                if (payloadData.TryGetValue("lock", out var lockValue) && (bool)lockValue)
                {
                    
                    if (_spreader.Sensor.DetectedContainer && (bool)lockValue)
                    {
                        await PublishLockStatus(true);
                    }
                    else
                    {
                        await PublishLockStatus(false);
                    }
                }
            }
             }


        public async Task SubscribeToTopic(string topic)
        {

            if (_mqttClient is not null && _mqttClient.IsConnected())
            {

                await _mqttClient.SubscribeAsync(topic);

            }

        }
        public async Task SubscribePositionSpreader()
        {


            await SubscribeToTopic("outputs/positionSpreader");


        }
        public async Task SubscribeJoystick()
        {


            await SubscribeToTopic("outputs/inputsJoystick");
        }


            public async Task PublishSensorStatus(bool detectedContainer)
        {
            if (detectedContainer)
            {
                await _mqttClient.PublishAsync("outputs/sensorSpreader", $"Sensor has detected a container");
            }
            else
            {
                await _mqttClient.PublishAsync("outputs/sensorSpreader", $"Sensor could not detect a container");
            }

        }
        public async Task PublishLockStatus(bool locked)
        {
            if (locked)
            {
                await _mqttClient.PublishAsync("outputs/actionSpreader", $"Lock is in use");
            }
            else
            {
                await _mqttClient.PublishAsync("outputs/actionSpreader", $"Lock is not in use");
            }
        }
       

        }
}
