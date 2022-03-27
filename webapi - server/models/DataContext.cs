using Microsoft.EntityFrameWorkCore;

namespace webapi___server.models
{
    public class DataContext : DbContext
    {
        public DataContext(DbContextOptions<DataContext> options)
        {
            
        }
    }
}