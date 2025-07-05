import names  # type: ignore

# генерация список из 100 имён
name_list = [names.get_first_name() for _ in range(100)]


# две группы по первой букве
group_a_m = [name for name in name_list if "A" <= name[0].upper() <= "M"]
group_n_z = [name for name in name_list if "N" <= name[0].upper() <= "Z"]

print("Имена с A по M:\n", sorted(group_a_m))
print("+++")
print("Имена с N по Z:\n", sorted(group_n_z))
