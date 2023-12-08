using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Wex1.Elephant.Logger.Core.Dto.Actionlogs
{
    public class ActionLogRequestDto
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
