using MongoDB.Bson.Serialization;
using Wex.Elephant.Logger.Infrastructure.Repositories;
using Wex1.Elephant.Logger.Core.Entities;
using Wex1.Elephant.Logger.Core.Interfaces.Mqtt;
using Wex1.Elephant.Logger.Core.Interfaces.Repositories;
using Wex1.Elephant.Logger.Core.Interfaces.Services;
using Wex1.Elephant.Logger.Core.Interfaces.Services.CrudService;
using Wex1.Elephant.Logger.WebApi.Services;
using Wex1.Elephant.Logger.WebApi.Services.CrudServices;
using Wex1.Elephant.Logger.WebApi.Services.Mqtt;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

BsonClassMap.RegisterClassMap<BaseLog>(classMap =>
{
    classMap.AutoMap();
    classMap.MapMember(log => log.EventTimeStamp).SetElementName("timestamp");
    classMap.MapMember(log => log.EventType).SetElementName("type");
    classMap.MapMember(log => log.Component).SetElementName("component");
    classMap.MapMember(log => log.Description).SetElementName("description");
});

BsonClassMap.RegisterClassMap<SpeedLog>(classMap =>
{
    classMap.MapMember(log => log.Speed).SetElementName("speed");
});

BsonClassMap.RegisterClassMap<PositionLog>(classMap =>
{
    classMap.MapMember(log => log.Position).SetElementName("position");
});

//Dependency injection
//Other services
builder.Services.AddHttpContextAccessor();
builder.Services.AddSingleton<IUriService>(options =>
{
    var accessor = options.GetRequiredService<IHttpContextAccessor>();
    var request = accessor.HttpContext.Request;
    var uri = string.Concat(request.Scheme, "://", request.Host.ToUriComponent());
    return new UriService(uri);
});
builder.Services.AddSingleton<IMqttService, MqttService>();

//Repositories
builder.Services.AddTransient<IErrorLogRepository, ErrorLogRepository>();
builder.Services.AddTransient<ISpeedLogRepository, SpeedLogRepository>();
builder.Services.AddTransient<IActionLogRepository, ActionLogRepository>();
builder.Services.AddTransient<IPositionLogRepository, PositionLogRepository>();

//Crud Services
builder.Services.AddTransient<IErrorLogCrudService, ErrorLogsCrudService>();
builder.Services.AddTransient<ISpeedLogCrudService, SpeedLogsCrudService>();
builder.Services.AddTransient<IActionLogCrudService, ActionLogsCrudService>();
builder.Services.AddTransient<IPositionLogCrudService, PositionLogCrudService>();


var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.Services.GetRequiredService<IMqttService>();

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();
app.Run();
