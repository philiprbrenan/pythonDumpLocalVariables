def dump_locals_variables():                                                    # Dump local variables
  import inspect, pprint
  d = ''
  frame = inspect.currentframe().f_back                                         # Caller's stack frame
  local_vars = frame.f_locals

  d += f"\n{'Name':<20} | {'Type':<15} | Value\n"                               # Headers
  d += ("-" * 60) +"\n";

  for name, value in sorted(local_vars.items()):
    if name.startswith('__'):
        continue                                                                # Skip magic variables
    if callable(value):
        continue                                                                # Skip functions/methods
    d += f"{name:<20} | {type(value).__name__:<15} | {pprint.pformat(value)}\n"

  return d

if __name__ == "__main__":                                                      # Tests
  def aaa():                                                                    # Create a stack frame
    a = 1
    b = 2
    return dump_locals_variables()

  assert aaa() == '''
Name                 | Type            | Value
------------------------------------------------------------
a                    | int             | 1
b                    | int             | 2
'''
