using HiveMQtt.Client.Events;
using HiveMQtt.Client.Options;

namespace Wex1.Elephant.Logger.Core.Interfaces.Mqtt
{
    public interface IMqttLoggerService
    {
        Task CreateMqttClient(HiveMQClientOptions options);
        void Client_OnMessageReceived(object? sender, OnMessageReceivedEventArgs e);
        Task HandleMessageAsync(OnMessageReceivedEventArgs e);

    }
}
