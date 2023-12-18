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
using Wex1.Elephant.Logger.Core.Dto.MqttInputs;
using Wex1.Elephant.Spreader.Core.Dto;

namespace Wex1.Elephant.Spreader.ConsoleApp.Services.Mqtt
{
    public class MqttService : IMqttService
    {
        public HiveMQClient _mqttClient { set; get; }
        private Spreaders _spreader = new Spreaders();

        
        private Container _container = new Container();
        
        // coordinaten sts-kraan gebied
        readonly double _minStsX = 345;
        readonly double _maxStsX = 425;
        readonly double _minStsY = 190;
        readonly double _maxStsY = 300;
       
        // coordinaten boot gebied
        readonly double _minBoatX = 200;
        readonly double _maxBoatX = 300;
        readonly double _minBoatY = 150;
        readonly double _maxBoatY = 300;
       
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

                _spreader.Sensor = new Sensor();
                _container.PositionX = 230.0;
                _container.PositionY = 245.0;
                


                _spreader.PositionX = positionValues.PositionX;

                _spreader.PositionY = positionValues.PositionY;
               
                //_spreader.PositionZ = positionValues[2];
                //container starting position : 110 - 150 X || 185-200 Y 
                if (_spreader.PositionX >= _container.PositionX && _spreader.PositionX <= (_container.PositionX + 40)
                    && _spreader.PositionY >= _container.PositionY && _spreader.PositionY <= (_container.PositionY + 15) 
                   )
                {
                    _spreader.Sensor.DetectedContainer = true;

                    await PublishSensorStatus(true);


                }
                else
                {
                    await PublishSensorStatus(false);
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
                var payloadData = JsonSerializer.Deserialize<JoyStickDto>(payload);

                if (payloadData.IsLocked == true)
                {

                    if (_spreader.Sensor.DetectedContainer && (bool)payloadData.IsLocked &&
                        _spreader.PositionX >= _minBoatX && _spreader.PositionX <= _maxBoatX &&
                        _spreader.PositionY >= _minBoatY && _spreader.PositionY <= _maxBoatY
                        )
                    {
                        _spreader.Lock = true;
                        await PublishLockStatus(true,true);
                    }
                   
                }
                else if (payloadData.IsLocked == false)
                {
                    
                    if (_spreader.Sensor.DetectedContainer == false && _spreader.PositionX >= _minStsX
                        && _spreader.PositionX <= _maxStsX
                        && _spreader.PositionY >= _minStsY
                        && _spreader.PositionY <= _maxStsY
                      )
                    {
                        _spreader.Lock = false;
                        await PublishLockStatus(false,false);
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
            var sensorValueDto = new SensorValueDto();

            if (detectedContainer)
            {
                sensorValueDto.SensorValue = true;
            }
            else
            {
                sensorValueDto.SensorValue = false;
            }

            string json = JsonSerializer.Serialize(sensorValueDto);
           
                await _mqttClient.PublishAsync("outputs/sensorSpreader", json);
           

        }
        public async Task PublishLockStatus(bool isLocked, bool hasContainer)
        {
            LockStatusDto lockStatus = new LockStatusDto
            {
                HasContainer = hasContainer,
                IsLocked = isLocked
            };

            string jsonMessage = JsonSerializer.Serialize(lockStatus);

            await _mqttClient.PublishAsync("outputs/actionSpreader", jsonMessage);
        }


    }
}
