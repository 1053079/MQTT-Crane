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

namespace Wex1.Elephant.Spreader.ConsoleApp.Services.Mqtt
{
    public class MqttService : IMqttService
    {       
        public HiveMQClient _mqttClient { set; get; }
        private Spreaders _spreader;
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
            //await SubscribePositionSpreader();



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
            if (e.PublishMessage.Topic == "output/positionSpreader")
            {
                var payload = e.PublishMessage.PayloadAsString;
                Console.WriteLine(payload);
              

            }
            
        }


        public async Task SubscribeToTopic(string topic)
        {
            
            if (_mqttClient is not null && _mqttClient.IsConnected())
            {
                
                await _mqttClient.SubscribeAsync(topic);

            }
           
        }
        

       
        }
    }
}
