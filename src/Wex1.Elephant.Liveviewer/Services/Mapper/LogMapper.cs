using Wex1.Elephant.Liveviewer.Dto;
using Wex1.Elephant.Liveviewer.Model;

namespace Wex1.Elephant.Liveviewer.Services.Mapper
{
    public static class LogMapper
    {
        public static ErrorLog MapToLog(this ErrorDto dto)
        {
            return new ErrorLog
            {
                Id = dto.Id,
                Timestamp = dto.Timestamp,
                Component = dto.Component,
                Description = dto.Description,
                Type = dto.Type
            };
        }

        public static IEnumerable<ErrorLog> MapToLog(this IEnumerable<ErrorDto> dtos)
        {
            return dtos.Select(dto => dto.MapToLog());
        }
        public static ActionLog MapToLOg(this ActionDto dto)
        {
            return new ActionLog
            {
                Id = dto.Id,
                Timestamp = dto.Timestamp,
                Component = dto.Component,
                Description = dto.Description,
                Type = dto.Type
            };
        }

        public static IEnumerable<ActionLog> MapToLog(this IEnumerable<ActionDto> dtos)
        {
            return dtos.Select(dto => dto.MapToLOg());
        }

        public static PositionLog MapToLog(this PositionDto dto)
        {
            return new PositionLog
            {
                Id = dto.Id,
                Timestamp = dto.Timestamp,
                Component = dto.Component,
                Description = dto.Description,
                PositionX = dto.PositionX,
                PositionY = dto.PositionY,
                PositionZ = dto.PositionZ,
                Type = dto.Type
            };
        }

        public static IEnumerable<PositionLog> MapToLog(this IEnumerable<PositionDto> dtos)
        {
            return dtos.Select(dto => dto.MapToLog());
        }

        public static SpeedLog MapToLog(this SpeedDto dto)
        {
            return new SpeedLog
            {
                Id = dto.Id,
                Timestamp = dto.Timestamp,
                Component = dto.Component,
                Description = dto.Description,
                Speed = dto.Speed,
                Type = dto.Type
            };
        }

        public static IEnumerable<SpeedLog> MapToLog(this IEnumerable<SpeedDto> dtos)
        {
            return dtos.Select(dto => dto.MapToLog());
        }


    }
}
