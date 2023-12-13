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

       

    }
}
