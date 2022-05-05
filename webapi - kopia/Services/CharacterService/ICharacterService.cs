using System.Collections.Generic;
using System.Threading.Tasks;
using webapi.models;
using webapi.Dtos.Character;

//Note: Asynchronous methods are being used as an example of when and how to use it; necessary for larger projects

namespace webapi.Services.CharacterService
{
    public interface ICharacterService
    {
        //1: Hämta alla karaktärer som finns i systemet
         Task<ServiceResponse<List<GetCharacterDto>>> GetAllCharacters();
         //2: Hämtar en metod som lägger till en ny karaktär
         Task<ServiceResponse<GetCharacterDto>> GetCharacterById(int id);
         //3: Skapa en metod som lägger till karaktärer
         Task<ServiceResponse<List<GetCharacterDto>>> AddCharacter(AddCharacterDto newCharacter);
         //4: Uppdaterar listan
         Task<ServiceResponse<GetCharacterDto>> UpdateCharacter(UpdateCharacterDto updatedCharacter);
         //5: Tar bort karaktärer
         Task<ServiceResponse<List<GetCharacterDto>>> DeleteCharacter(int id);
    }
}