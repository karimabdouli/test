"""
    addition
"""
import random

from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram

class PeerQ4(Peer):

    def send_data_to_backend(self):
        """
            Question 4: implement this method
        """
        connection_duration_list = []
        for key, value in random.sample(self.peer_pool.items(), min(len(self.peer_pool.items()), 100)) :
            connection_duration_list.append(value)
        return connection_duration_list
    ## we just take at most 100 peers in the peer pool
    
    
class SimulationQ4(Simulation):

    def generate_network(self):
        self.network = [PeerQ4() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
            Question 4: implement this method
        """
        datas = []
        for peer in random.sample(self.network, min(len(self.network), 10000)) :
            datas += peer.send_data_to_backend()
        ## we just take at most 10000 peers to work with their peer pools
            
            
        result = compute_histogram_bins(datas, BINS)
        for i in range(len(result[0])) :
            result[0][i] = result[0][i]/2


if __name__ == "__main__":

    s = SimulationQ4(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()
