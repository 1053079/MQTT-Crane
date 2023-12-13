using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Wex1.Elephant.Logger.Core.Filters
{
    public class DateFilter
    {
        public DateOnly? SelectedDate { get; set;}
        public bool NewestFirst { get; set;}

        public DateFilter()
        {
            SelectedDate = null;
            NewestFirst = true;
        }

        public DateFilter(DateOnly selectedDate)
        {
            var dateNow = DateOnly.FromDateTime(DateTime.UtcNow);
            SelectedDate = selectedDate > dateNow ? dateNow : selectedDate;
        }

        public DateFilter(bool newestFirst)
        {
            NewestFirst = newestFirst;
        }

        public DateFilter(DateOnly selectedDate, bool newestFirst)
        {
            var dateNow = DateOnly.FromDateTime(DateTime.UtcNow);
            SelectedDate = selectedDate > dateNow ? dateNow : selectedDate;
            NewestFirst = newestFirst;
        }

    }
}
