using System.Text.Json.Serialization;

namespace webapi___server.models
{
    [JsonConverter(typeof(JsonStringEnumConverter))]
    public enum types
    {
        None,
        Water,
        Fire,
        Grass,
        Electric,
        Rock,
        Ground,
        Poison,
        Bug,
        Psychic,
        Ghost,
        Dragon,
        Flying,
        Dark,
        Steel,
        Fairy,
    }
}