# Building a datacenter

You've following on-prem choices, if you decide to go with deploying to datacenter:
- Greenfield buildout - Buy or lease whole datacenter yourself
- Cage colocation - Lease space inside a datacenter (enclosed by mesh walls)
- Rack colocation - Lease racks in a data center

In a co located datacenter, cost of power is generally greater than the cost of leasing the space. So you've to decide the compute based on how much power you want to draw. 

## Pre requisites

### Power
Power is the single most critical resource in a datacenter. It takes a long time to recover from an outage. Hence, redundancy is critical. You need two independent power feeds per rack. 

PDU (Power Distribution Unit), ranges from glorified extension cables to advanced with full management features like control and metered individual sockets. 

### Network
After power, network is 2nd most critical resource. You need a tier 1 ISP and peering with internet exchanges (IX) for low latency. 

### Cooling
Airflow and cooling will be required. 

## Inventory

You've bought the inventory: servers with dual redundant NICs, multiple redundant NVME drives, PDUs, network switches etc. 

Neat cabling requires professional experience. Cabling matrix and rack elevation are the docs which communicate how to rack and wire up. This step is closer to building a house than to deploying a terraform stack. Every place is different with different challenges and different solutions, hard to maintain uniformity. Common problem at this stage: "Cables are too short"

## Deployment

Next steps:
- network devices needs configuring
	- installing sonic os 
- router config needs writing
- RIR (Regional Internet Registry) records needs updating
- redfish api to connect to BMC
- pxe booting

## Sources
- https://blog.railway.com/p/data-center-build-part-one
## Related
- 