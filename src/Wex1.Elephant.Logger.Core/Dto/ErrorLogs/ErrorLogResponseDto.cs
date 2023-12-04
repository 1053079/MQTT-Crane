using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Wex1.Elephant.Logger.Core.Enums;

namespace Wex1.Elephant.Logger.Core.Dto.ErrorLogs
{
    public class ErrorLogResponseDto
    {
        public string Id { get; set; }
        public DateTime EventTimeStamp { get; set; }
        public EventTypes EventType { get; set; }
        public ComponentTypes component { get; set; }
        public string Description { get; set; }
    }
}
