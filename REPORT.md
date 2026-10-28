# TP2 — Part 5: Professional Debugging

## 1. Diagnosis

The program failed inside `compute_weighted_metric()` at the following line:

```python
return volume * weight
```

Using the Python interactive debugger (`pdb`), I inspected the runtime values and types of the variables:

```text
volume = '120'
weight = '2'
type(volume) = <class 'str'>
type(weight) = <class 'str'>
```

Both `volume` and `weight` were strings because they were extracted directly from the comma-separated input using `split(",")`.

The multiplication therefore attempted to multiply a string by another string:

```python
'120' * '2'
```

This produced the following runtime error:

```text
TypeError: can't multiply sequence by non-int of type 'str'
```

The root cause was that the numeric fields were not converted from strings to numeric values when the API record was parsed.

## 2. Call Stack

The Python debugger showed the following call stack at the point of failure:

```text
<module>
    ↓
aggregate_telemetry
    ↓
compute_weighted_metric
```

The error occurred in `compute_weighted_metric()` when executing:

```python
return volume * weight
```

## 3. Fix

The numeric fields were converted to `float` values when parsing each API record.

### Before

```python
"volume": parts[2],
"weight": parts[4]
```

### After

```python
"volume": float(parts[2]),
"weight": float(parts[4])
```

The corrected `parse_api_record()` function is:

```python
def parse_api_record(raw_entry: str) -> dict:
    parts = raw_entry.strip().split(",")
    return {
        "id": parts[0],
        "entity": parts[1],
        "volume": float(parts[2]),
        "status": parts[3],
        "weight": float(parts[4])
    }
```

This ensures that `volume` and `weight` are numeric values before they are passed to `compute_weighted_metric()`.

## 4. Validation

After applying the fix, the program was executed using:

```bash
uv run python scripts/debug_challenge.py
```

The program produced:

```text
Aggregate Result: {'successful_entries': 3, 'total_volume': 650.0, 'avg_volume': 216.66666666666666, 'high_impact_count': 1}
```

The corrected program therefore produces the expected results:

| Metric | Result |
|---|---:|
| Successful entries | 3 |
| Total volume | 650.0 |
| Average volume | approximately 216.67 |
| High-impact count | 1 |

The debugging issue was successfully identified and fixed, and the program now produces the expected aggregate telemetry results.
