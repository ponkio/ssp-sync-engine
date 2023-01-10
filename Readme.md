# Sync Engine

This application is meant to run every hour to execute environment syncs for customers who have configured Landscape monitoring for their cloud accounts. 

Kubernetes is configured with 3 cron jobs to execute hourly, daily, and weekly. Each time the job is executed the customers configured for that timeframe are pulled and sent to the scanners to sync a customer environment. 


## Required Infra
- namespace
- mongo password in namespace
- 