def parse_file(file_location, list_return_type) -> list:

    try:

        with open(file_location, encoding="utf8") as input_file:


            line_count = 1

            # specific to avacados.csv
            list_id = []
            list_date = []
            list_average_price = []
            list_total_volume = []
            list_4046 = []
            list_4225 = []
            list_4770 = []
            list_total_bags = []
            list_small_bags = []
            list_large_bags = []
            list_xlarge_bags = []
            list_type = []
            list_year = []
            list_region  = []

            for line in input_file:

                try:

                    if line_count == 1:
                        line_count = line_count + 1
                        continue

                    if line_count == 20:
                        break

                    value_id, value_date, value_average_price, value_total_volume, value_4046, value_4225, value_4770, value_total_bags, value_small_bags, value_large_bags, value_xlarge_bags, value_type, value_year, value_region = line.split(",")

                    value_id = value_id.strip()
                    value_date = value_date.strip()
                    value_average_price = value_average_price.strip()
                    value_total_volume = value_total_volume.strip()
                    value_4046 = value_4046.strip()
                    value_4225 = value_4225.strip()
                    value_4770 = value_4770.strip()
                    value_total_bags = value_total_bags.strip()
                    value_small_bags = value_small_bags.strip()
                    value_large_bags = value_large_bags.strip()
                    value_xlarge_bags = value_xlarge_bags.strip()
                    value_type = value_type.strip()
                    value_year = value_year.strip()
                    value_region = value_region.strip()

                    list_id.append(float(value_id))
                    list_date.append(value_date)
                    list_average_price.append(float(value_average_price))
                    list_total_volume.append(float(value_total_volume))
                    list_4046.append(float(value_4046))
                    list_4225.append(float(value_4225))
                    list_4770.append(float(value_4770))
                    list_total_bags.append(float(value_total_bags))
                    list_small_bags.append(float(value_small_bags))
                    list_large_bags.append(float(value_large_bags))
                    list_xlarge_bags.append(float(value_xlarge_bags))
                    list_type.append(value_type)
                    list_year.append(float(value_year))
                    list_region.append(value_region)


                except Exception as e :

                    print(f"Was unable line parse line : {line_count} of the file {file_location}")
                    print(e)

                    # with open("", "a") as log_file:
                        # print(f"Was unable line parse line : {line} of the file {file_location}")

                line_count = line_count + 1

    except:

        print("unable to locate file")

    # Return a column from the list
    if list_return_type == "average_price":
        return list_average_price
    if list_return_type == "total_volume":
        return list_total_volume
    if list_return_type == "4046":
        return list_4046
    if list_return_type == "4225":
        return list_4225
    if list_return_type == "4770":
        return list_4770
    if list_return_type == "total_bags":
        return list_total_bags
    if list_return_type == "small_bags":
        return list_small_bags
    if list_return_type == "large_bags":
        return list_large_bags
    if list_return_type == "xlarge_bags":
        return list_xlarge_bags
    if list_return_type == "type":
        return list_type
    if list_return_type == "year":
        return list_year
    if list_return_type == "list_region":
        return list_region

    if list_return_type == "all":
        return list_id, list_date, list_average_price, list_total_volume, list_4046, list_4225, list_4770, list_total_bags, list_small_bags, list_large_bags, list_xlarge_bags, list_type, list_year, list_region

    return -1