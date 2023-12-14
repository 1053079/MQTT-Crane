using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Wex1.Elephant.Logger.Core.Filters
{
    public class DateFilter
    {
        public DateTime? SelectedDate { get; set;}
        public bool NewestFirst { get; set;}

        public DateFilter()
        {
            SelectedDate = null;
            NewestFirst = true;
        }

        public DateFilter(DateTime? selectedDate, bool newestFirst)
        {
            var dateNow = DateTime.UtcNow.Date;
            SelectedDate = selectedDate.Value.Date > dateNow ? dateNow : selectedDate.Value.Date;
            NewestFirst = newestFirst;
        }

    }
}
