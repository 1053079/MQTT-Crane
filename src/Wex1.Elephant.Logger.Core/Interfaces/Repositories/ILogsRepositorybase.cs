using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Wex1.Elephant.Logger.Core.Entities;

namespace Wex1.Elephant.Logger.Core.Interfaces.Repositories
{
    public interface ILogsRepositorybase<T> where T : BaseLog
    {
        IQueryable<T> GetAll();
        Task<IEnumerable<T>> GetListAsync();
        Task<IEnumerable<T>> GetPagedData(IEnumerable<T> data, int pageNumber, int pageSize);
        Task<T> GetByIdAsync(Guid id);
        Task AddAsync(T entity);
        Task<bool> UpdateAsync(T entity);
        Task<bool> DeleteAsync(T entity);
    }
}
