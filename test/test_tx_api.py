"""
    MetaSV API Spec

    API definition for MetaSV provided apis  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Contact: heqiming@metasv.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import metasv_mvc_client
from metasv_mvc_client.api.tx_api import TxApi  # noqa: E501


class TestTxApi(unittest.TestCase):
    """TxApi unit test stubs"""

    def setUp(self):
        self.api = TxApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tx_broadcast_post(self):
        """Test case for tx_broadcast_post

        Broadcast tx to metasv fullnode.  # noqa: E501
        """
        pass

    def test_tx_txid_get(self):
        """Test case for tx_txid_get

        Get transaction detail by specific txid.  # noqa: E501
        """
        pass

    def test_tx_txid_raw_get(self):
        """Test case for tx_txid_raw_get

        Get transaction raw hex by specific txid.  # noqa: E501
        """
        pass

    def test_tx_txid_seen_get(self):
        """Test case for tx_txid_seen_get

        Whether MetaSV have seen this tx before. This is a fast approach to know if the tx exist or not.  # noqa: E501
        """
        pass

    def test_vin_txid_detail_get(self):
        """Test case for vin_txid_detail_get

        Get all output point of vins in the tx with detailed output script.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()