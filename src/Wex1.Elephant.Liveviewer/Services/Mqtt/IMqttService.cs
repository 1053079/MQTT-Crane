using HiveMQtt.Client;
using HiveMQtt.Client.Events;
using HiveMQtt.Client.Options;

namespace Wex1.Elephant.Liveviewer.Services.Mqtt
{
    public interface IMqttService
    {
        Task<HiveMQClient> CreateMqttClient();
    }
}
