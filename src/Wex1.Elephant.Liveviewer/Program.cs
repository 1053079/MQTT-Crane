using Wex1.Elephant.Liveviewer.Services.Mock;
using Wex1.Elephant.Liveviewer.Services.Mqtt;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();
builder.Services.AddScoped<ErrorLogService>();
builder.Services.AddScoped<PositionLogService>();
builder.Services.AddScoped<SpeedLogService>();
builder.Services.AddScoped<ActionLogService>();
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
