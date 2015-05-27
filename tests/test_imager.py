from plugins.imager import Imager
from . utils import Runner

class TestImager(Runner):
    ENHANCER = Imager
    INPUT = [
        {"id": 1, "image_urls": "foobar"}, # image_urls should be overwritten
        {"id": "23"},
        {"id": 561},
        {"id": 903542}  # this image has a url but no location
    ]
    OUTPUT = [
        {"id":1,
         "image_ids":[6245048,6245049,6245046,6245047],
         "image_locations":["https://www.foobar.com/63266a92559ce8535b80a71ad81db53eaf908c76.jpg",
            "https://www.foobar.com/9dcfd2b6459a44c44381bd55be9a858b3301dcd9.jpg",
            "https://www.foobar.com/e6088c37fadb0626deb421494843fa912be600f1.jpg",
            "https://www.foobar.com/68b019ba27a82a6e0738d060f83fa72db7a25567.jpg"],
        "image_urls":["http://www.foobar.com/p/47d54e1275de633f76574b225cf39461.jpg",
            "http://www.foobar.com/p/8a32ad3567cb05f05d41bf18967eb7f0.jpg",
            "http://www.foobar.com/p/6cd94b9fb05ad53e906c5743292ffaf7.jpg",
            "http://www.foobar.com/p/992882507616e6125b1bc98927392b1e.jpg"]},
        {"id":"23",
         "image_ids":[6245114,6245115,6245116],
         "image_locations":["https://www.foobar.com/0c2d999edbcbddad1349e62e44788fae7fa3561f.jpg",
            "https://www.foobar.com/a72c789777ec09890291831eb7a25976ce3ed81f.jpg",
            "https://www.foobar.com/a96e55bab4d75da84ca375b5a980522afc9edba2.jpg"],
        "image_urls":["http://www.foobar.com/p/fec585148b3361016e6fdac8f50e861d.jpg",
            "http://www.foobar.com/p/6e4b559f8b23c94ddb767f4bea00859f.jpg",
            "http://www.foobar.com/p/a7843bfe3bd3416d53fe6254564c1be9.jpg"]},
        {"id":561,
         "image_ids":[6247010,6247011],
         "image_locations":["https://www.foobar.com/a0353b184faddbb2f3e8f02d9592f8ef893e7967.jpg",
            "https://www.foobar.com/5a25e401f828aa029fb245b49742bbbb788dc613.jpg"],
        "image_urls":["http://www.foobar.com/p/5eca2ebdd24ae3f5905c939712285870.jpg",
            "http://www.foobar.com/p/1d6ae58869732bc7e4af3d65afc699a9.jpg"]},
        {"id": 903542,
         "image_locations":[""],
         "image_urls":["http://www.foobar.com/00M0M_hCu6gBYFwvv_600x450.jpg"],
         "image_ids":[5879551]}
    ]
