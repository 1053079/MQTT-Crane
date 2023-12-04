using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Wex1.Elephant.Logger.Core.Dto.ErrorLogs;

namespace Wex1.Elephant.Logger.Core.Interfaces.Services.CrudService
{
    public interface IErrorLogCrudService : ICrudService<ErrorLogRequestDto>
    {
    }
}
