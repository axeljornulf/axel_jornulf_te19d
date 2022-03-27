using Microsoft.EntityFrameworkCore;

namespace webapi.models
{
    public class DataContext : DbContext
    {
        public DataContext(DbContextOptions<DataContext> options):base(options)
        {
            
        }

        public DbSet<Character> characters {get; set;}
    }
}