using Wex1.Elephant.Logger.Core.Dto.ErrorLogs;
using Wex1.Elephant.Logger.Core.Dto.SpeedLogs;
using Wex1.Elephant.Logger.Core.Entities;

namespace Wex1.Elephant.Logger.WebApi.Wrappers.Mapper
{
    public static class DtoMapper
    {
        public static ErrorLogResponseDto MapToDto(this ErrorLog errorLog)
        {
            return new ErrorLogResponseDto
            {
                Id = errorLog.Id.ToString(),
                EventTimeStamp = errorLog.EventTimeStamp,
                EventType = errorLog.EventType,
                component = errorLog.Component,
                Description = errorLog.Description
            };
        }

        public static IEnumerable<ErrorLogResponseDto> MapToDto(this IEnumerable<ErrorLog> errorLogs)
        {
            return errorLogs.Select(el => el.MapToDto());
        }

        public static SpeedLogResponseDto MapToDto(this SpeedLog speedLog)
        {
            return new SpeedLogResponseDto
            {
                Id = speedLog.Id.ToString(),
                EventTimeStamp = speedLog.EventTimeStamp,
                EventType = speedLog.EventType,
                component = speedLog.Component,
                Description = speedLog.Description,
                Speed = speedLog.Speed
            };
        }

        public static IEnumerable<SpeedLogResponseDto> MapToDto(this IEnumerable<SpeedLog> speedLogs)
        {
            return speedLogs.Select(sl => sl.MapToDto());
        }

    }
}
