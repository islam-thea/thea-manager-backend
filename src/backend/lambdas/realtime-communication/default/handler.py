# ---------------------------------------------------------------
#                           Imports
# ---------------------------------------------------------------

import json

# ---------------------------------------------------------------
#                            Main
# ---------------------------------------------------------------


def lambda_handler(event, context):

    request_body = event["body"]

    # TODO implement
    return {"statusCode": 200, "body": json.dumps(request_body)}
