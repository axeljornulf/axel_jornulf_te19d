using System.Collections.Generic;
using webapi.models;
using System.Linq;
using System.Threading.Tasks;
using AutoMapper;
using webapi.Dtos.Character;
using System;

namespace webapi.Services.CharacterService
{
    public class CharacterService : ICharacterService
    {
        private static List<Character> characters = new List<Character>
        {
            new Character(),
            new Character{Id = 1, Name = "Glam", healthpoints = 202, attack = 249, defense = 150, specialattack = 90, specialdefense = 150, speed = 90, PrimaryType = types.Poison, SecondaryType = types.None},
            //new Character{Id = 0, Name = "Glörgi", healthpoints = 100, attack = 50, defense = 120, specialattack = 70, specialdefense = 150, speed = 200, PrimaryType = types.Fairy, SecondaryType = types.Bug}
        };

        private readonly DataContext _context;
        private readonly IMapper _mapper;

        public CharacterService(IMapper mapper, DataContext context)
        {
            _mapper = mapper;
            _context = context;
        }

        public async Task<ServiceResponse<List<GetCharacterDto>>> AddCharacter(AddCharacterDto newCharacter)
        {
            var serviceResponse = new ServiceResponse<List<GetCharacterDto>>();
            Character character = _mapper.Map<Character>(newCharacter);
            character.Id = _context.characters.Max(c => c.Id) + 1;
            _context.characters.Add(character);
            await _context.SaveChangesAsync();
            serviceResponse.Data = _context.characters.Select(c => _mapper.Map<GetCharacterDto>(c)).ToList();

            return serviceResponse;
        }

        public async Task<ServiceResponse<List<GetCharacterDto>>> DeleteCharacter(int id)
        {
            var serviceResponse = new ServiceResponse<List<GetCharacterDto>>();

            try
            {
                Character character = _context.characters.First(c => c.Id == id);

                _context.characters.Remove(character);

                serviceResponse.Data = _context.characters.Select(c => _mapper.Map<GetCharacterDto>(c)).ToList();
                await _context.SaveChangesAsync();
            } catch(Exception e)
            {
                serviceResponse.Success = false;
                serviceResponse.Message = e.Message;
            }
            return serviceResponse;
        }

        public async Task<ServiceResponse<List<GetCharacterDto>>> GetAllCharacters()
        {
            var serviceResponse = new ServiceResponse<List<GetCharacterDto>>();
            serviceResponse.Data = _context.characters.Select(c => _mapper.Map<GetCharacterDto>(c)).ToList();
            return serviceResponse;
        }

        public async Task<ServiceResponse<GetCharacterDto>> GetCharacterById(int id)
        {
            var serviceResponse = new ServiceResponse<GetCharacterDto>();
            serviceResponse.Data = _mapper.Map<GetCharacterDto>(_context.characters.FirstOrDefault(c => c.Id == id));
            return serviceResponse;
        }

        public async Task<ServiceResponse<GetCharacterDto>> UpdateCharacter(UpdateCharacterDto updatedCharacter)
        {
            var serviceResponse = new ServiceResponse<GetCharacterDto>();

            try
            {
                Character character = _context.characters.FirstOrDefault(c => c.Id == updatedCharacter.Id);

                character.Name = updatedCharacter.Name;
                character.healthpoints = updatedCharacter.healthpoints;
                character.attack = updatedCharacter.attack;
                character.defense = updatedCharacter.defense;
                character.specialattack = updatedCharacter.specialattack;
                character.specialdefense = updatedCharacter.specialdefense;
                character.speed = updatedCharacter.speed;
                character.PrimaryType = updatedCharacter.PrimaryType;
                character.SecondaryType = updatedCharacter.SecondaryType;

                await _context.SaveChangesAsync();

                serviceResponse.Data = _mapper.Map<GetCharacterDto>(character);
            } catch(Exception e)
            {
                serviceResponse.Success = false;
                serviceResponse.Message = e.Message;
            }
            return serviceResponse;
        }
    }
}