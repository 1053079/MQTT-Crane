using HiveMQtt.Client.Options;
using Wex1.Elephant.Spreader.Core;


    var mqttService = new Wex1.Elephant.Spreader.ConsoleApp.Services.Mqtt.MqttService();

    

    await mqttService.SubscribeToTopic("output/positionSpreader");

    
    Console.WriteLine("Listening for messages. Press any key to exit.");
    Console.ReadKey();

