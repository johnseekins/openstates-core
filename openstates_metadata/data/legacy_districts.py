from ..models import District

legacy_districts = {
    "md": [
        District("12A", "lower", division_id=None),
        District("12B", "lower", division_id=None),
        District("2C", "lower", division_id=None),
        District("30", "lower", division_id=None),
        District("31", "lower", division_id=None),
        District("33A", "lower", division_id=None),
        District("33B", "lower", division_id=None),
        District("42", "lower", division_id=None),
        District("44", "lower", division_id=None),
        District("47", "lower", division_id=None),
        District("4A", "lower", division_id=None),
        District("4B", "lower", division_id=None),
        District("5A", "lower", division_id=None),
        District("5B", "lower", division_id=None),
    ],
    "nh": [District(str(n), "upper", division_id=None) for n in range(1, 25)],
    "nv": [
        District("Capital Senatorial District", "upper", division_id=None),
        District("Central Nevada Senatorial District", "upper", division_id=None),
        District("Clark County, No. 1", "upper", division_id=None),
        District("Clark County, No. 3", "upper", division_id=None),
        District("Clark County, No. 4", "upper", division_id=None),
        District("Clark County, No. 5", "upper", division_id=None),
        District("Clark County, No. 6", "upper", division_id=None),
        District("Clark County, No. 7", "upper", division_id=None),
        District("Clark County, No. 8", "upper", division_id=None),
        District("Clark County, No. 9", "upper", division_id=None),
        District("Clark County, No. 9", "upper", division_id=None),
        District("Clark County, No. 10", "upper", division_id=None),
        District("Clark County, No. 11", "upper", division_id=None),
        District("Clark County, No. 12", "upper", division_id=None),
        District("Rural Nevada Senatorial District", "upper", division_id=None),
        District("Washoe County, No. 1", "upper", division_id=None),
        District("Washoe County, No. 2", "upper", division_id=None),
        District("Washoe County, No. 3", "upper", division_id=None),
        District("Washoe County, No. 4", "upper", division_id=None),
    ],
    "pr": [District(str(n), "upper", division_id=None) for n in range(1, 8)],
    "vt": [
        District("Addison-Rutland-1", "upper", division_id=None),
        District("Bennington-Rutland-1", "upper", division_id=None),
        District("Chittenden-1-2", "upper", division_id=None),
        District("Chittenden-3-1", "upper", division_id=None),
        District("Chittenden-3-2", "upper", division_id=None),
        District("Chittenden-3-3", "upper", division_id=None),
        District("Chittenden-3-4", "upper", division_id=None),
        District("Chittenden-3-5", "upper", division_id=None),
        District("Chittenden-3-6", "upper", division_id=None),
        District("Chittenden-3-7", "upper", division_id=None),
        District("Chittenden-3-9", "upper", division_id=None),
        District("Chittenden-4", "upper", division_id=None),
        District("Chittenden-8", "upper", division_id=None),
        District("Chittenden-9", "upper", division_id=None),
        District("Franklin-3", "upper", division_id=None),
        District("Grand Isle-Chittenden-1-1", "upper", division_id=None),
        District("Lamoille-4", "upper", division_id=None),
        District("Lamoille-Washington-1", "upper", division_id=None),
        District("Orange-Addison-1", "upper", division_id=None),
        District("Orleans-Caledonia-1", "upper", division_id=None),
        District("Rutland-1-1", "upper", division_id=None),
        District("Rutland-1-2", "upper", division_id=None),
        District("Rutland-7", "upper", division_id=None),
        District("Rutland-8", "upper", division_id=None),
        District("Washington-3-2", "upper", division_id=None),
        District("Washington-3-3", "upper", division_id=None),
        District("Washington-Chittenden-1", "upper", division_id=None),
        District("Windham-2", "upper", division_id=None),
        District("Windham-3-1", "upper", division_id=None),
        District("Windham-3-3", "upper", division_id=None),
        District("Windham-Bennington-1", "upper", division_id=None),
        District("Windham-Bennington-Windsor-1", "upper", division_id=None),
        District("Windsor-1-1", "upper", division_id=None),
        District("Windsor-1-2", "upper", division_id=None),
        District("Windsor-3", "upper", division_id=None),
        District("Windsor-4", "upper", division_id=None),
        District("Windsor-6-1", "upper", division_id=None),
        District("Windsor-6-2", "upper", division_id=None),
    ],
}
