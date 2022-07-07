# Cape Functions

## Getting Started

To run these functions with Cape, you need to first install the [Cape CLI](https://github.com/capeprivacy/cli).

### Cape login

Log into Cape by running:
```
cape login
```

### Cape Deploy

Deploys a `function_dir` to Cape. Returns a `function_id`.

```
cape deploy <function_dir>
```

### Cape Run

Runs a cape function by `function_id` and `input_file`. Returns a `result`.

```
cape run <function_id> <input_file>
```

## Examples

### echo

A simple function that returns whatever you send it.

```
cape deploy echo
```

```
cape run 4b4961ef-1f04-4027-850a-3fd39a9501f2 input.echo.data
```

### isprime

```
cape deploy isprime
```

```
cape run 28028ae0-cf5c-47f8-8e8e-0da42b6dc142 input.isprime.data
```

### np-stats
A simple example with numpy dependencies and `pycape.io_serialize` decorator to deserialize/serialize the input and output of a cape function.


