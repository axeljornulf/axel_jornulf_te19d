using webapi___server.models;

namespace webapi___server.Dtos.Character
{
    public class UpdateCharacterDto
    {
        public int Id {get; set;}
        public string Name {get; set;} = "Glörgi";
        public int healthpoints {get; set;} = 100;
        public int attack {get; set;} = 50;
        public int defense {get; set;} = 120;
        public int specialattack {get; set;} = 70;
        public int specialdefense {get; set;} = 150;
        public int speed {get; set;} = 200;
        public types PrimaryType {get; set;} = types.Fairy;
        public types SecondaryType {get; set;} = types.Bug;
    }
}