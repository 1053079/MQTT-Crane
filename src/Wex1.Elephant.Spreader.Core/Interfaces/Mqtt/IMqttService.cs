using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using HiveMQtt.Client;
using HiveMQtt.Client.Events;
using HiveMQtt.Client.Options;
using System.Diagnostics;
using System.Text.Json;

namespace Wex1.Elephant.Spreader.Core.Interfaces.Mqtt
{
    public interface IMqttService
    {

        Task CreateMqttClient(HiveMQClientOptions options);
        Task SubscribeJoystick();
        Task SubscribePositionSpreader();

        Task PublishSensorStatus(bool detectedContainer);
        Task PublishLockStatus(bool locked , bool hascontainer);
        public void _mqttClient_OnMessageReceived(object? sender, OnMessageReceivedEventArgs e);
        Task HandleMessageAsync(OnMessageReceivedEventArgs e);
    }
}
