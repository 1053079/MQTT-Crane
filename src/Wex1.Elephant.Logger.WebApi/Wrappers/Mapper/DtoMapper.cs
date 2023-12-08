using Wex1.Elephant.Logger.Core.Dto.Actionlogs;
using Wex1.Elephant.Logger.Core.Dto.ErrorLogs;
using Wex1.Elephant.Logger.Core.Dto.PositionLogs;
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
                Component = errorLog.Component,
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
                Component = speedLog.Component,
                Description = speedLog.Description,
                Speed = speedLog.Speed
            };
        }

        public static IEnumerable<SpeedLogResponseDto> MapToDto(this IEnumerable<SpeedLog> speedLogs)
        {
            return speedLogs.Select(sl => sl.MapToDto());
        }

        public static ActionLogResponseDto MapToDto(this ActionLog actionLog)
        {
            return new ActionLogResponseDto
            {
                Id = actionLog.Id.ToString(),
                EventTimeStamp = actionLog.EventTimeStamp,
                EventType = actionLog.EventType,
                Component = actionLog.Component,
                Description = actionLog.Description
            };
        }

        public static IEnumerable<ActionLogResponseDto> MapToDto(this IEnumerable<ActionLog> actionLogs)
        {
            return actionLogs.Select(al => al.MapToDto());
        }

        public static PositionLogResponseDto MapToDto(this PositionLog positionLog)
        {
            return new PositionLogResponseDto
            {
                Id = positionLog.Id.ToString(),
                EventTimeStamp = positionLog.EventTimeStamp,
                EventType = positionLog.EventType,
                Component = positionLog.Component,
                Description = positionLog.Description,
                PositionX = positionLog.Position[0],
                PositionY = positionLog.Position[1],
                PositionZ = positionLog.Position[2]
            };
        }

        public static IEnumerable<PositionLogResponseDto> MapToDto(this IEnumerable<PositionLog> positionLogs)
        {
            return positionLogs.Select(pl => pl.MapToDto());
        }

    }
}
