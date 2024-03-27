from app_router import *

# Example usage:
router = Router()
router.loadConfig('config.txt')


print(router.findRoute("customer1.us.ca.sfo"))  # Output: server1
print(router.findRoute("customer1.us.ca.sjc"))  # Output: server2
print(router.findRoute("customer2.us.tx.dfw"))  # Output: server3
print(router.findRoute("customer2.cn.tw.tai"))  # Output: server4
print(router.findRoute("customer10.us.ny.nyc")) # Output: server5
print(router.findRoute("customer1"))            # Output: No Valid Server