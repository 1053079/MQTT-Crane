using HiveMQtt.Client.Events;
using HiveMQtt.Client.Options;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Wex1.Elephant.Logger.Core.Interfaces.Mqtt
{
    public interface IMqttMapperService
    {
        Task CreateMqttClient(HiveMQClientOptions options);
        void Client_OnMessageReceived(object? sender, OnMessageReceivedEventArgs e);
        Task HandleMessageAsync(OnMessageReceivedEventArgs e);
    }
}
