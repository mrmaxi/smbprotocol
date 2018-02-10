from smbprotocol.transport import DirectTCPPacket


class TestDirectTcpPacket(object):

    def test_create_message(self):
        message = DirectTCPPacket()
        message['smb2_message'] = b"\xfe\x53\x4d\x42"
        expected = b"\x00\x00\x00\x04" \
                   b"\xfe\x53\x4d\x42"

        actual = message.pack()
        assert len(message) == 8
        assert message['stream_protocol_length'].get_value() == 4
        assert actual == expected

    def test_parse_message(self):
        actual = DirectTCPPacket()
        data = b"\x00\x00\x00\x04" \
               b"\xfe\x53\x4d\x42"
        actual.unpack(data)
        assert len(actual) == 8
        assert actual['stream_protocol_length'].get_value() == 4
        assert isinstance(actual['smb2_message'].get_value(), bytes)

        actual_header = actual['smb2_message']
        assert len(actual_header) == 4
        assert actual_header.get_value() == b"\xfe\x53\x4d\x42"
