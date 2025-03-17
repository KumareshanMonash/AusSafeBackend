from ..models.LocationModel import Location

dummy_recommendations = [
    {
        "uv_index_range": (0, 2),
        "skin_tone": "fair",
        "skin_type": "sensitive",
        "activity_level": "low",
        "recommendation": {
            "type_of_clothing": "Lightweight clothing covering most skin",
            "amount_of_sunscreen": "Apply a generous amount to all exposed skin",
            "type_of_sunscreen": "Broad-spectrum SPF 30+",
            "reapply_frequency": "Every 2 hours",
            "max_sun_exposure_time": "Up to 1 hour"
        }
    },
    {
        "uv_index_range": (3, 5),
        "skin_tone": "medium",
        "skin_type": "normal",
        "activity_level": "moderate",
        "recommendation": {
            "type_of_clothing": "Protective clothing, hat, and sunglasses",
            "amount_of_sunscreen": "Apply liberally to exposed areas",
            "type_of_sunscreen": "Broad-spectrum SPF 50+",
            "reapply_frequency": "Every 1.5 hours",
            "max_sun_exposure_time": "Up to 45 minutes"
        }
    },
    {
        "uv_index_range": (6, 7),
        "skin_tone": "olive",
        "skin_type": "combination",
        "activity_level": "high",
        "recommendation": {
            "type_of_clothing": "Long-sleeved shirts, pants, wide-brimmed hat",
            "amount_of_sunscreen": "Apply generously to all exposed skin",
            "type_of_sunscreen": "Broad-spectrum SPF 50+ water-resistant",
            "reapply_frequency": "Every hour",
            "max_sun_exposure_time": "Up to 30 minutes"
        }
    },
    {
        "uv_index_range": (8, 10),
        "skin_tone": "dark",
        "skin_type": "oily",
        "activity_level": "low",
        "recommendation": {
            "type_of_clothing": "Full-coverage clothing, hat, and UV-blocking sunglasses",
            "amount_of_sunscreen": "Apply moderately to exposed areas",
            "type_of_sunscreen": "Broad-spectrum SPF 30+",
            "reapply_frequency": "Every 2 hours",
            "max_sun_exposure_time": "Up to 1 hour"
        }
    },
    {
        "uv_index_range": (11, 12),
        "skin_tone": "fair",
        "skin_type": "dry",
        "activity_level": "moderate",
        "recommendation": {
            "type_of_clothing": "UPF-rated clothing, wide-brimmed hat, and sunglasses",
            "amount_of_sunscreen": "Apply a thick layer to all exposed skin",
            "type_of_sunscreen": "Broad-spectrum SPF 50+ with moisturizers",
            "reapply_frequency": "Every 1 hour",
            "max_sun_exposure_time": "Up to 20 minutes"
        }
    },
    {
        "uv_index_range": (0, 2),
        "skin_tone": "medium",
        "skin_type": "sensitive",
        "activity_level": "high",
        "recommendation": {
            "type_of_clothing": "Breathable, long-sleeved activewear",
            "amount_of_sunscreen": "Apply generously to all exposed skin",
            "type_of_sunscreen": "Broad-spectrum SPF 50+ sweat-resistant",
            "reapply_frequency": "Every hour",
            "max_sun_exposure_time": "Up to 1.5 hours"
        }
    },
    {
        "uv_index_range": (3, 5),
        "skin_tone": "olive",
        "skin_type": "normal",
        "activity_level": "low",
        "recommendation": {
            "type_of_clothing": "Lightweight, long-sleeved clothing and hat",
            "amount_of_sunscreen": "Apply moderately to exposed areas",
            "type_of_sunscreen": "Broad-spectrum SPF 30+",
            "reapply_frequency": "Every 2 hours",
            "max_sun_exposure_time": "Up to 2 hours"
        }
    },
    {
        "uv_index_range": (6, 7),
        "skin_tone": "dark",
        "skin_type": "dry",
        "activity_level": "moderate",
        "recommendation": {
            "type_of_clothing": "Protective clothing, hat, and sunglasses",
            "amount_of_sunscreen": "Apply liberally to exposed skin",
            "type_of_sunscreen": "Broad-spectrum SPF 30+ with moisturizers",
            "reapply_frequency": "Every 1.5 hours",
            "max_sun_exposure_time": "Up to 1 hour"
        }
    },
    {
        "uv_index_range": (8, 10),
        "skin_tone": "fair",
        "skin_type": "combination",
        "activity_level": "high",
        "recommendation": {
            "type_of_clothing": "UPF-rated athletic wear, hat, and UV-blocking sunglasses",
            "amount_of_sunscreen": "Apply a generous amount to all exposed skin",
            "type_of_sunscreen": "Broad-spectrum SPF 50+ water and sweat-resistant",
            "reapply_frequency": "Every 45 minutes",
            "max_sun_exposure_time": "Up to 30 minutes"
        }
    },
    {
        "uv_index_range": (11, 12),
        "skin_tone": "medium",
        "skin_type": "oily",
        "activity_level": "low",
        "recommendation": {
            "type_of_clothing": "Full-coverage clothing, wide-brimmed hat, and sunglasses",
            "amount_of_sunscreen": "Apply moderately to exposed areas",
            "type_of_sunscreen": "Broad-spectrum SPF 50+ oil-free formula",
            "reapply_frequency": "Every hour",
            "max_sun_exposure_time": "Up to 20 minutes"
        }
    }
]

dummy_locations = [
    Location(id=1, location_name="Sydney Opera House", state="NSW", country="Australia", zipcode="2000", latitude=-33.856784, longitude=151.215297, area="Sydney"),
    Location(id=2, location_name="Great Barrier Reef", state="QLD", country="Australia", zipcode="4805", latitude=-18.287100, longitude=147.699219, area="Whitsundays"),
    Location(id=3, location_name="Uluru (Ayers Rock)", state="NT", country="Australia", zipcode="0872", latitude=-25.344428, longitude=131.036882, area="Uluru-Kata Tjuta National Park"),
    Location(id=4, location_name="Bondi Beach", state="NSW", country="Australia", zipcode="2026", latitude=-33.890842, longitude=151.274292, area="Sydney"),
    Location(id=5, location_name="Kangaroo Island", state="SA", country="Australia", zipcode="5223", latitude=-35.775200, longitude=137.402206, area="Kingscote"),
    Location(id=6, location_name="Melbourne Cricket Ground", state="VIC", country="Australia", zipcode="3002", latitude=-37.819967, longitude=144.983449, area="Melbourne"),
    Location(id=7, location_name="Blue Mountains National Park", state="NSW", country="Australia", zipcode="2787", latitude=-33.700000, longitude=150.300000, area="Katoomba"),
    Location(id=8, location_name="Daintree Rainforest", state="QLD", country="Australia", zipcode="4873", latitude=-16.170000, longitude=145.418500, area="Mossman"),
    Location(id=9, location_name="Fraser Island", state="QLD", country="Australia", zipcode="4581", latitude=-25.239999, longitude=153.132500, area="Hervey Bay"),
    Location(id=10, location_name="Port Arthur Historic Site", state="TAS", country="Australia", zipcode="7182", latitude=-43.148992, longitude=147.850886, area="Port Arthur"),
    Location(id=11, location_name="Kakadu National Park", state="NT", country="Australia", zipcode="0822", latitude=-12.720000, longitude=132.830000, area="Jabiru"),
    Location(id=12, location_name="Barossa Valley", state="SA", country="Australia", zipcode="5352", latitude=-34.532500, longitude=138.957500, area="Tanunda"),
    Location(id=13, location_name="Phillip Island", state="VIC", country="Australia", zipcode="3922", latitude=-38.483333, longitude=145.233333, area="Cowes"),
    Location(id=14, location_name="Hunter Valley", state="NSW", country="Australia", zipcode="2320", latitude=-32.740000, longitude=151.170000, area="Pokolbin"),
    Location(id=15, location_name="Cradle Mountain", state="TAS", country="Australia", zipcode="7306", latitude=-41.683056, longitude=145.961944, area="Cradle Mountain-Lake St Clair National Park"),
    Location(id=16, location_name="Kings Canyon", state="NT", country="Australia", zipcode="0872", latitude=-24.250000, longitude=131.566667, area="Watarrka National Park"),
    Location(id=17, location_name="Litchfield National Park", state="NT", country="Australia", zipcode="0845", latitude=-13.130000, longitude=130.780000, area="Batchelor"),
    Location(id=18, location_name="Margaret River", state="WA", country="Australia", zipcode="6285", latitude=-33.950000, longitude=115.066667, area="Margaret River"),
    Location(id=19, location_name="Snowy Mountains", state="NSW", country="Australia", zipcode="2627", latitude=-36.500000, longitude=148.333333, area="Jindabyne"),
    Location(id=20, location_name="Rottnest Island", state="WA", country="Australia", zipcode="6161", latitude=-32.000000, longitude=115.500000, area="Rottnest Island"),
]

