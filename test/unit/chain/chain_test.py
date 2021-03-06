# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from hfc.api.chain.chain import Chain
from hfc.api.peer import Peer
from hfc.api.orderer import Orderer


class ChainTest(unittest.TestCase):

    @unittest.expectedFailure
    def test_create_chain(self):
        # TODO impl
        chain = Chain()
        chain.add_peer(Peer())
        chain.add_orderer(Orderer())
        self.fail()


if __name__ == '__main__':
    unittest.main()
