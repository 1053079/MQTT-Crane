using HiveMQtt.Client;
using HiveMQtt.Client.Events;
using HiveMQtt.Client.Options;
using Wex1.Elephant.Liveviewer.Services.Interfaces.Mqtt;

namespace Wex1.Elephant.Liveviewer.Services.Mqtt
{
    public class MqttService : IMqttService
    {
        public async Task<HiveMQClient> CreateMqttClient()
        {
            var options = new HiveMQClientOptions
            {
                UserName = LiveviewerConstants.MqttUserName,
                Password = LiveviewerConstants.MqttPassword,
                Port = LiveviewerConstants.MqttPort,
                Host = LiveviewerConstants.MqttClusterUrl,
                UseTLS = true,
            };

            var mqttClient = new HiveMQClient(options);
            await mqttClient.ConnectAsync().ConfigureAwait(false);
            return mqttClient;
        }
    }
}
