import pytest
from render import voxel_gi as mod

CASES = [
    ("size", 'm.voxel_size(2, 0.1) == approx(0.4)'),
    ("center", 'm.clipmap_center((5, 3), 2) == (4, 2)'),
    ("fill", 'm.conservative_fill((0, 0, 0, 1, 1, 1), 0.5) == (-0.5, -0.5, -0.5, 1.5, 1.5, 1.5)'),
    ("bounce", 'm.bounce_energy(0.5, 2) == approx(0.75)'),
    ("inject", 'm.dynamic_injection(3, 2) == 5'),
    ("sky", 'm.sky_visibility(0.5) is True'),
    ("key", 'm.camera_clipmap_key("L", 2) == "L:2"'),
    ("barrier", 'm.barrier_needed("voxel", "render") is True'),
    ("axis", 'm.normal_from_axis(1) == (0, 1, 0)'),
    ("light", 'm.light_cache_key(7, 3) == "7:3"'),
    ("blend", 'm.clipmap_blend(0.2, 0.6, 0.5) == approx(0.4)'),
    ("contains", 'm.voxel_contains((0, 0, 0, 2, 2, 2), (1, 1, 1)) is True'),
    ("leak", 'm.leak_mask(0.1, 0.2) is True'),
    ("scale", 'm.indirect_scale(10, 5) == approx(0.5)'),
    ("transition", 'm.level_transition((0, 0), (5, 0), 4) is True')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
