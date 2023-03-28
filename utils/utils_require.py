from functools import wraps

from utils.utils_request import request_failed

MAX_CHAR_LENGTH = 255

# A decorator function for processing `require` in view function.
def Check_Require(check_fn):
    @wraps(check_fn)
    def decorated(*args, **kwargs):
        try:
            return check_fn(*args, **kwargs)
        except Exception as e:
            # Handle exception e
            error_code = -2 if len(e.args) < 2 else e.args[1]
            return request_failed(error_code, e.args[0], 400)  # Refer to below
    return decorated


# Here err_code == -2 denotes "Error in request body"
# And err_code == -1 denotes "Error in request URL parsing"
def require(body, key, type="string", err_msg=None, err_code=-2):

    if key not in body.keys():
        raise KeyError(err_msg if err_msg is not None
                       else f"Invalid parameters. Expected `{key}`, but not found.", err_code)

    val = body[key]

    try:
        if type == "int":
            val = int(val)
        elif type == "float":
            val = float(val)
        elif type == "string":
            val = str(val)
        elif type == "list":
            assert isinstance(val, list)
        else:
            raise NotImplementedError(f"Type `{type}` not implemented.", err_code)
    except:
        raise KeyError(err_msg if err_msg is not None
                       else f"Invalid parameters. Expected `{key}` to be `{type}` type.", err_code)

    return val