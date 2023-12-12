using HiveMQtt.Client;
using HiveMQtt.Client.Events;
using HiveMQtt.Client.Options;

namespace Wex1.Elephant.Liveviewer.Services.Mqtt
{
    public class MqttService : IMqttService
    {
        public async Task<HiveMQClient> CreateMqttClient()
        {
            var options = new HiveMQClientOptions
            {
                UserName = Constants.MqttUserName,
                Password = Constants.MqttPassword,
                Port = Constants.MqttPort,
                Host = Constants.MqttClusterUrl,
                UseTLS = true,
            };

            var mqttClient = new HiveMQClient(options);
            await mqttClient.ConnectAsync().ConfigureAwait(false);
            return mqttClient;
        }
    }
}
