import datetime

# ISO8601 format: 2022-11-11T14:13:05.390261

def print_iso_datetime(dt = datetime.datetime.now()):

    # How format strings work
    # print('{:<10s}{:<4s}'.format("hello", "world"))
    # print('{:<10s}{:<4s}'.format("goodbye", "world"))
    # print('{:<10s}{:<4s}{:>6s}'.format("foo", "bar", "baz"))
    # print("\n")

    # Get current time
    dt = datetime.datetime.now() # get current datetime
    print("{:<50s}{}".format("default format", str(dt)))
    
    # Print ISO8601 format    
    now_iso_default_str = dt.isoformat()
    print("{:<50s}{}".format("ISO8601 format", now_iso_default_str))

    # Print ISO8601 format with timezone
    now_utc_aware = dt.replace(tzinfo=datetime.timezone.utc) # Add UTC timezone to now
    iso_utc_str = now_utc_aware.isoformat()
    print("{:<50s}{}".format("ISO8601 UTC aware format", iso_utc_str))
   
    # Print ISO8601 format without milliseconds decimal
    iso_utc_no_dec = now_utc_aware.replace(microsecond=0)
    iso_utc_no_dec_str = iso_utc_no_dec.isoformat()
    print("{:<50s}{}".format("ISO8601 UTC aware format without microseconds",iso_utc_no_dec_str))
  
    # Replace +00.00 with "Z"
    iso_utc_z_str = iso_utc_no_dec_str.replace("+00:00", "Z")
    print("{:<50s}{}".format("ISO8601 UTC aware Z format without microseconds",iso_utc_z_str))

def parse_z_timestamp(dt_str):
    #print(dt_str)
    dt_str = dt_str.replace("Z", "+00:00")
    dt_obj = datetime.datetime.fromisoformat(dt_str)
    return dt_obj

def print_time_delta(start_datetime, end_datetime):
    delta_time = end_datetime - start_datetime
    print(delta_time)
    return(delta_time)

if __name__ == "__main__":
    #print_iso_datetime() # if no datetime object passed, then now() is used

    notAfter_str = "2023-01-06T01:26:48Z"
    notAfter_dt = parse_z_timestamp(notAfter_str)
    notBefore_str = "2022-10-08T01:26:48Z"
    notBefore_dt = parse_z_timestamp(notBefore_str)
    renewalTime_str = "2022-12-07T01:26:48Z"
    renewalTime_dt = parse_z_timestamp(renewalTime_str)

    print_time_delta(renewalTime_dt, notAfter_dt)
    print_time_delta(start_datetime=notBefore_dt, end_datetime=renewalTime_dt)
    print_time_delta(notBefore_dt, notAfter_dt)
    