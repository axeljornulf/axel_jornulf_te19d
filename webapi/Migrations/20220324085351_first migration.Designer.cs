﻿// <auto-generated />
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.EntityFrameworkCore.Migrations;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using webapi.models;

namespace webapi.Migrations
{
    [DbContext(typeof(DataContext))]
    [Migration("20220324085351_first migration")]
    partial class firstmigration
    {
        protected override void BuildTargetModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .UseIdentityColumns()
                .HasAnnotation("Relational:MaxIdentifierLength", 128)
                .HasAnnotation("ProductVersion", "5.0.0");

            modelBuilder.Entity("webapi.models.Character", b =>
                {
                    b.Property<int>("Id")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int")
                        .UseIdentityColumn();

                    b.Property<string>("Name")
                        .HasColumnType("nvarchar(max)");

                    b.Property<int>("PrimaryType")
                        .HasColumnType("int");

                    b.Property<int>("SecondaryType")
                        .HasColumnType("int");

                    b.Property<int>("attack")
                        .HasColumnType("int");

                    b.Property<int>("defense")
                        .HasColumnType("int");

                    b.Property<int>("healthpoints")
                        .HasColumnType("int");

                    b.Property<int>("specialattack")
                        .HasColumnType("int");

                    b.Property<int>("specialdefense")
                        .HasColumnType("int");

                    b.Property<int>("speed")
                        .HasColumnType("int");

                    b.HasKey("Id");

                    b.ToTable("characters");
                });
#pragma warning restore 612, 618
        }
    }
}