import config
import boto

def scraper_handler(event, context):
    conn = boto.connect_s3(config.accesskey, config.secretkey)
    try:
        bucket = conn.get_bucket(config.bucketname)
    except S3ResponseError:
        return -1



    return 0
