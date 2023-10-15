# Base Transformer

This Python script, `base_transformer.py`, is designed to convert numbers from one base to another. It takes a number in a specified base and converts it to base 10 (decimal). It includes the following functions:

##

With this app you can convert this bases:
    From 2, 8 and 16 --> 10
    From 8, 10 and 16 --> 2

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