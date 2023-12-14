using Wex1.Elephant.Liveviewer.Services;
using Wex1.Elephant.Liveviewer.Services.Interfaces;
using Wex1.Elephant.Liveviewer.Services.Interfaces.Mqtt;
using Wex1.Elephant.Liveviewer.Services.Mqtt;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();


builder.Services.AddTransient<HttpClient>();
//builder.Services.AddScoped<ILogProvider<ErrorLog>, LogProvider<ErrorLog>>();
//builder.Services.AddScoped<IErrorLogCrudService, ErrorLogsCrudService>();
builder.Services.AddTransient<IApiErrorLogProvider, ApiErrorProvider>();
builder.Services.AddTransient<IApiActionLogProvider, ApiActionProvider>();
builder.Services.AddTransient<IApiSpeedLogProvider, ApiSpeedProvider>();
builder.Services.AddTransient<IApiPositionLogProvider, ApiPositionProvider>();

//builder.Services.AddScoped<ILogsRepositorybase<ErrorLog>, ErrorLogRepository>();
builder.Services.AddTransient<IMqttService, MqttService>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();

app.UseStaticFiles();

app.UseRouting();

app.MapBlazorHub();
app.MapFallbackToPage("/_Host");

app.Run();
