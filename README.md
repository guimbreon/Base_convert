# Base Transformer

This Python script, `base_transformer.py`, is designed to convert numbers from one base to another. It takes a number in a specified base and converts it to base 10 (decimal). It includes the following functions:

## Functions

### `getData(file_link)`

This function reads data from a specified [file](Keys) and returns the values as a list. Each line in the file is expected to contain a number in a specified base.

- `file_link`: A string representing the path to the file containing the data.

### `getValues()`

This function is used to retrieve a user-defined number and its base for conversion. The values should be formated like this: value|base. Ex: 6712AF16.12414AFCD|16

### `hexaToNums(quote)`

This function converts hexadecimal characters (A-F) in the input to their decimal equivalents (10-15) and returns a list of numbers.

### `convertTo10Whole(quote, base)`

This function converts the whole part of a number (before the decimal point) from the specified base to base 10.

- `quote`: The number in the specified base.
- `base`: The base of the input number.

### `convertTo10Frac(quote, base)`

This function converts the fractional part of a number (after the decimal point) from the specified base to base 10.

- `quote`: The fractional part of the number in the specified base.
- `base`: The base of the input number.

### `fromXTo10(quote, base)`

This function combines the conversion of the whole and fractional parts, accounting for the presence of a decimal point in the number. It returns the number in base 10.

- `quote`: The number in the specified base.
- `base`: The base of the input number.

## Example Usage

```
$python converter.py
What do you want to convert?

```
Then you would have to enter the values in this notation:
value|base
Example:
6712AF16.12414AFCD|16

## Usage

1. Save your data to a file, where each line represents a number in the specified base.
2. Modify the `quote` variable in the `getValues` function or provide input interactively.
3. Run the script to convert the number from the specified base to base 10.

Please note that this script supports conversion from bases other than decimal (base 10) to base 10. Modify the `baseConvert` variable if you need a different target base.