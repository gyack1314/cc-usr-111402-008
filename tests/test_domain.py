"""资料与现有领域接口的核对。"""
import unittest,tempfile,json
from pathlib import Path
from lake.storage import Storage
from lake.spatial import inspect

class DomainTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name);self.store=Storage(self.root/'objects')
        self.data=json.loads(Path('data/source.json').read_text(encoding='utf-8'))
    def test_existing_reader(self):
        self.assertTrue(inspect(self.data,self.store,self.root))

    def test_bounds_only_and_bad_ring(self):
        from lake.spatial import bounds
        self.assertEqual(bounds(self.data['regions'][0]['geometry']),[0,0,10,10])
        self.assertEqual(bounds(self.data['tracks'][1]['geometry']),[5,5,5,5])
        with self.assertRaises(ValueError):bounds({'type':'Polygon','rings':[[[0,0],[1,0],[1,1],[2,2]]]})
