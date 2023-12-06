namespace Wex1.Elephant.Liveviewer.Services
{
    public interface ILogProvider<T> where T : class
    {
        Task<IEnumerable<T>> GetAll(/*int pageNumber, int pageSize*/);
        Task<T> Get(string id);

    }
}
