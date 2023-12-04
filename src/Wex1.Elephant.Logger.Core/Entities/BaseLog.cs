using MongoDB.Bson;
using MongoDB.Bson.Serialization;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Wex1.Elephant.Logger.Core.Enums;

namespace Wex1.Elephant.Logger.Core.Entities
{
    public class BaseLog
    {

        public ObjectId Id { get; set; }
        public DateTime EventTimeStamp { get; set; }
        public string EventType { get; set; }
        public string Component { get; set; }
        public string Description { get; set; }
    }
}
