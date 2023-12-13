using HiveMQtt.Client.Options;
using Wex1.Elephant.Spreader.Core;


    var mqttService = new Wex1.Elephant.Spreader.ConsoleApp.Services.Mqtt.MqttService();



await mqttService.SubscribeJoystick();
await mqttService.SubscribePositionSpreader();
await mqttService.SubscribeToTopic("outputs/sensorSpreader");


Console.WriteLine("Listening for messages. Press any key to exit.");
    Console.ReadKey();

