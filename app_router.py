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
