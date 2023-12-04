using System.ComponentModel.DataAnnotations;

namespace Wex1.Elephant.Logger.Core.Dto.ErrorLogs
{
    public class ErrorLogRequestDto
    {
        public string Id { get; set; }
        [Required]
        public DateTime EventTimeStamp { get; set; }
        [Required]
        public string EventType { get; set; }
        [Required]
        public string component { get; set; }
        [Required]
        [MaxLength(255, ErrorMessage = "{0} can't be longer then 255 characters.")]
        public string Description { get; set; }
    }
}
