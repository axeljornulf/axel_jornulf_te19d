using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using webapi___server.models;
using Microsoft.AspNetCore.Mvc;
using webapi___server.Services.CharacterService;
using webapi___server.Dtos.Character;

namespace webapi___server.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class SuckiController : ControllerBase
    {
        private readonly ICharacterService _characterService;

        public SuckiController(ICharacterService characterService)
        {
            _characterService = characterService;

        }

        [HttpGet("GetAll")]
        public async Task<ActionResult<ServiceResponse<List<GetCharacterDto>>>> Get()
        {
            return Ok(await _characterService.GetAllCharacters());
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<ServiceResponse<GetCharacterDto>>> GetSingle(int id)
        {
            return Ok(await _characterService.GetCharacterById(id));
        }

        [HttpPost]
        public async Task<ActionResult<ServiceResponse<List<GetCharacterDto>>>> AddCharacter(AddCharacterDto newCharacter)
        {
            return Ok(await _characterService.AddCharacter(newCharacter));
        }

        [HttpPut]
        public async Task<ActionResult<ServiceResponse<GetCharacterDto>>> UpdateCharacter(UpdateCharacterDto updateCharacter)
        {
            var response = await _characterService.UpdateCharacter(updateCharacter);

            if(response.Data == null)
            {
                return NotFound(response);
            }

            return Ok(response);
        }

        [HttpDelete("{id}")]
        public async Task<ActionResult<ServiceResponse<List<GetCharacterDto>>>> Delete(int id)
        {
            var response = await _characterService.DeleteCharacter(id);

            if(response.Data == null)
            {
                return NotFound(response);
            }

            return Ok(response);
        }
    }
}