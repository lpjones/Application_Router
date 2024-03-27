# Application_Router

# Task Explanation:

Designing an application router that can load routing configuration from a file and use that configuration to choose the best server for a given input is the problem at hand.

There should be two primary purposes for the router:

This function, loadConfig(), is used just once at the beginning of an application. To load the routing rules into an internal data structure, it reads a routing configuration file and parses its information. The server names for each pattern are specified in the routing rules. These guidelines ought to be kept in the function for further use.

findRoute(input): This function accepts an input string representing a customer ID, nation, state, and city as a parameter. By comparing the input to the loaded routing rules, the function's task is to find the suitable server name based on the input. Based on the most specific rule, the function should return the server name that fits the input.

The routing configuration file must adhere to a specified format in order to accomplish this. A routing rule is represented by each line in the file, which is formatted as route_pattern=server_name. To match any value for a certain area of the input, use the * wildcard in the pattern.

Given the routing guidelines in the configuration file, for instance: <br>
customer1.us.ca.\*=server1   <br>
customer2.us.\*.\*=server3    <br>
customer2.\*.\*.\*=server4 <br>
\*.\*.\*.\*=server5 <br>
customer1.us.ca.sjc=server2 <br>

The router should return server2 if we run findRoute("customer1.us.ca.sjc") since it is the most precise match for the input. Similar to this, finding server4 by running findRoute("customer2.cn.tw.tai") should work because server4 matches the customer2.*.*.* criterion.

Based on the input passed to the findRoute() function, the router implementation should successfully read the configuration file, interpret the rules, and deliver the required server name.

# Usage
Clone the repo using:
```console
git clone https://github.com/lpjones/Application_Router.git
```

To run the example script:
```console
python3 main.py
```