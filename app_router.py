class Node:
    def __init__(self):
        self.routes = {}
        self.server = ''

class Tree:
    def __init__(self):
        self.root = Node()

    def insert(self, str):
        pattern, server = str.split('=')
        sub_domains = pattern.split('.')
        cur_node = self.root
        
        # Loop through all subdomains
        for dom in sub_domains:
            # At end of subdomain list
            if dom == '*':
                break
            
            # Check if domain is in routes list
            if dom not in cur_node.routes:
                cur_node.routes[dom] = Node()
            cur_node = cur_node.routes[dom]

        cur_node.server = server


class Router:
    def __init__(self):
        self.tree = Tree()

    def loadConfig(self, config_file):
        with open(config_file, 'r') as file:
            for line in file:
                self.tree.insert(line.strip())

    def findRoute(self, str):
        pattern = str.split('.')
        cur_node = self.tree.root
        for pat in pattern:
            if pat in cur_node.routes:
                cur_node = cur_node.routes[pat]
            else:
                break
        if (cur_node.server == ''):
            return "No Valid Server"
        return cur_node.server

# Example usage:
# router = Router()
# router.loadConfig('config.txt')


# print(router.findRoute("customer1.us.ca.sfo"))  # Output: server1
# print(router.findRoute("customer1.us.ca.sjc"))  # Output: server2
# print(router.findRoute("customer2.us.tx.dfw"))  # Output: server3
# print(router.findRoute("customer2.cn.tw.tai"))  # Output: server4
# print(router.findRoute("customer10.us.ny.nyc")) # Output: server5
# print(router.findRoute("customer1"))            # Output: No Valid Server
