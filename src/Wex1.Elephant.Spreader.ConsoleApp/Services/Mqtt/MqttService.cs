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
using MongoDB.Bson;
using Wex1.Elephant.Spreader.Core.SpreaderPositionDto;

namespace Wex1.Elephant.Spreader.ConsoleApp.Services.Mqtt
{
    public class MqttService : IMqttService
    {
        public HiveMQClient _mqttClient { set; get; }
        private Spreaders _spreader = new Spreaders();
        private Container _container = new Container();
        // coordinaten sts-kraan gebied
        readonly double _minStsX = 200;
        readonly double _maxStsX = 315;
        readonly double _minStsY = 0;
        readonly double _maxStsY = 145;
        // coordinaten boot gebied
        readonly double _minBoatX = 80;
        readonly double _maxBoatX = 180;
        readonly double _minBoatY = 0;
        readonly double _maxBoatY = 200;
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

                SpreaderPositionDto positionValues = JsonSerializer.Deserialize<SpreaderPositionDto>(payload);

                _spreader.PositionX = positionValues.PositionX;
                _spreader.PositionY = positionValues.PositionY;
                //_spreader.PositionZ = positionValues[2];
                //container starting position : 110 - 150 X || 185-200 Y
                if (_spreader.PositionX >= _container.PositionX && _spreader.PositionX <= (_container.PositionX + 40)
                    && _spreader.PositionY >= _container.PositionY && _spreader.PositionY <= (_container.PositionY + 15))
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
                else
                {
                    _spreader.Sensor.DetectedContainer = false;
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
                    
                    if (_spreader.Sensor.DetectedContainer && (bool)lockValue && 
                        _spreader.PositionX >= _minBoatX && _spreader.PositionX <= _maxBoatX &&
                        _spreader.PositionY >= _minBoatY && _spreader.PositionY >= _maxBoatY )
                    {
                        _spreader.Lock = true;
                        await PublishLockStatus(true);
                    }
                    else if (_spreader.Sensor.DetectedContainer = false || _spreader.PositionX >= _minStsX 
                        && _spreader.PositionX <= _maxStsX 
                        && _spreader.PositionY >= _minStsY 
                        && _spreader.PositionY >= _maxStsY)
                    {
                        _spreader.Lock = false;
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


            await SubscribeToTopic("inputs/joystick");
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
