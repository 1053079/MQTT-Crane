using HiveMQtt.Client;

namespace Wex1.Elephant.Liveviewer.Services.Interfaces.Mqtt
{
    public interface IMqttService
    {
        Task<HiveMQClient> CreateMqttClient();
    }
}
