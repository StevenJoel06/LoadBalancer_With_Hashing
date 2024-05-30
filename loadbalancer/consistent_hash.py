import hashlib

class ConsistentHash:
    def __init__(self, m, k, n):
        self.m = m  # Number of slots
        self.k = k  # Number of virtual nodes
        self.num_servers = n
        self.hash_ring = {}

        for i in range(n):
            self.add_server(f"Server {i + 1}")

    def _hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16) % self.m

    def add_server(self, server_id):
        for i in range(self.k):
            virtual_node = f"{server_id}#{i}"
            hash_val = self._hash(virtual_node)
            self.hash_ring[hash_val] = server_id

    def add_servers(self, n):
        for i in range(n):
            self.add_server(f"Server {self.num_servers + 1}")
            self.num_servers += 1

    def remove_server(self, server_id):
        for i in range(self.k):
            virtual_node = f"{server_id}#{i}"
            hash_val = self._hash(virtual_node)
            if hash_val in self.hash_ring:
                del self.hash_ring[hash_val]

    def remove_servers(self, n):
        for i in range(n):
            self.remove_server(f"Server {self.num_servers}")
            self.num_servers -= 1

    def get_server(self, key):
        hash_val = self._hash(key)
        sorted_hashes = sorted(self.hash_ring.keys())
        for h in sorted_hashes:
            if hash_val <= h:
                return self.hash_ring[h]
        return self.hash_ring[sorted_hashes[0]]

    def get_servers(self):
        return list(set(self.hash_ring.values()))