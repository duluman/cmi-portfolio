## Nightly worker

1. Database (very large), relational (SQLite)
2. Daily writes > 1m
3. Data: 
   1. Sensor data 
      1. information about a machine (id, name)
      2. timestamp
      3. sensor type
      4. sensor reading
      5. sensor reading error
4. We have a worker that runs based on events (messages) and computes a report
5. We have multiple report types 
   1. Average Sensor Reading by MachineID
   2. MovingAverage Sensor Reading by MachineID
6. The worker creates a csv report and stores it on HDD 
7. The worker sends a notification (message) when a report is done or error occured

### Technical requirements
1. Messaging system: RabbitMQ
2. Database: SQLite