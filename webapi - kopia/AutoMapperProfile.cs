using AutoMapper;
using webapi___server.models;
using webapi___server.Dtos.Character;

namespace webapi___server
{
    public class AutoMapperProfile : Profile
    {
        public AutoMapperProfile()
        {
            CreateMap<Character, GetCharacterDto>();
            CreateMap<AddCharacterDto, Character>();
        }
    }
}