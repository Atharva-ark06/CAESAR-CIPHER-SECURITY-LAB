"""Demonstrate message validation on synthetic inputs."""
from security_analysis import validate_message
if __name__=="__main__":
    for message in ("hello","","  ","x"*1001):
        print(repr(message[:20]),validate_message(message))