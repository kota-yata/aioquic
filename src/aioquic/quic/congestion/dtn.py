from typing import Iterable

from ..packet_builder import QuicSentPacket
from .base import (
    QuicCongestionControl,
    QuicRttMonitor,
    register_congestion_control,
)

K_LOSS_REDUCTION_FACTOR = 0.5


class DtnCongestionControl(QuicCongestionControl):
    """
    DTN congestion control.
    """

    def __init__(self, *, max_datagram_size: int) -> None:
        super().__init__(max_datagram_size=max_datagram_size)
        self._max_datagram_size = max_datagram_size
        self._congestion_recovery_start_time = 0.0
        self._congestion_stash = 0
        self._rtt_monitor = QuicRttMonitor()

    def on_packet_acked(self, *, now: float, packet: QuicSentPacket) -> None:
        pass

    def on_packet_sent(self, *, packet: QuicSentPacket) -> None:
        pass

    def on_packets_expired(self, *, packets: Iterable[QuicSentPacket]) -> None:
        pass

    def on_packets_lost(self, *, now: float, packets: Iterable[QuicSentPacket]) -> None:
        pass

    def on_rtt_measurement(self, *, now: float, rtt: float) -> None:
        pass


register_congestion_control("dtn", DtnCongestionControl)
