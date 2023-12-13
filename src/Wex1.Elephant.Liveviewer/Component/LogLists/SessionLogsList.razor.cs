using HiveMQtt.Client;
using HiveMQtt.Client.Events;
using Microsoft.AspNetCore.Components;
using System.Text.Json;
using System.Text.Json.Serialization;
using Wex1.Elephant.Liveviewer.Model;
using Wex1.Elephant.Liveviewer.Services.Interfaces.Mqtt;
using Wex1.Elephant.Liveviewer.Services.Mqtt;

namespace Wex1.Elephant.Liveviewer.Component.LogLists
{
    public partial class SessionLogsList
    {
        [Inject]
        protected IMqttService _mqttService { get; set; }

        private HiveMQClient _mqttClient;

        private List<Baselog> _logs = new List<Baselog>();

        protected async override Task OnInitializedAsync()
        {
            _mqttClient = await _mqttService.CreateMqttClient();

            _mqttClient.OnMessageReceived += _mqttClient_OnMessageReceived;
            await _mqttClient.SubscribeAsync("logger/#");
            await base.OnInitializedAsync();
        }

        private async void _mqttClient_OnMessageReceived(object? sender, OnMessageReceivedEventArgs e)
        {
            
            var payloadModel = JsonSerializer.Deserialize<LogPayLoadModel>(e.PublishMessage.Payload);
            
            if (payloadModel is not null)
            {

                var newLog = new Baselog
                {
                    Id = payloadModel.Id.ToString(),
                    Component = payloadModel.Component,
                    Description = payloadModel.Description,
                    Timestamp = payloadModel.Timestamp,
                    Type = payloadModel.Type
                };

                _logs.Add(newLog);
                _logs.Sort((x, y) => y.Timestamp.CompareTo(x.Timestamp));
                await InvokeAsync(StateHasChanged);
            }
        }


    }
}
