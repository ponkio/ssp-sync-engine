import pymongo
import os
import logging
import argparse
import datetime

def sync_environment(config):
    logging.debug(f"Triggering sync: {config}")

def main(args, mongoClient):
    

    customer_dbs = mongoClient.list_database_names()

    excluded_dbs = ['admin','config','local','leakengine']
    logging.debug(f"Found {len(customer_dbs)-len(excluded_dbs)} customers")

    for customer in customer_dbs:
        if customer in excluded_dbs:
            continue
        
        logging.debug(f"Connecting to {customer}")
        db = mongoClient[customer]
        config_collection = db['landscape_config']
        
        logging.debug(f"Getting configuration for schedule: {args.schedule}")
        stagged_sync = [config for config in config_collection.find({"schedule":args.schedule})]

        logging.info(f"Syncing {len(stagged_sync)} configs")
        for env in stagged_sync:
            sync_environment(env)


if __name__ == "__main__":
    logging.basicConfig(
        # filename="sync_engine.log",
        level=logging.DEBUG,
        format= '%(created)f:%(levelname)s:%(name)s:%(module)s:%(message)s'
    )
    mongo_url = f"mongodb://root:{os.environ['MONGO_PWD']}@mongo-mongodb.mongo:27017/"
    logging.debug(f"Attempting connection to: {mongo_url.split('@')[1]}")

    mongoClient = pymongo.MongoClient(mongo_url)
    
    parser = argparse.ArgumentParser(
        prog = "Sync Engine",
        description = "Core cli for scheduling enviornment syncs."
    )
    parser.add_argument('-s', '--schedule', description="Schedule in cron format i.e '0 * * * *'", required=True)
    args = parser.parse_args()
    logging.info("Starting Sync Engine")
    main(args, mongoClient)


