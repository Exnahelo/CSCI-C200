# HoweLab7Blueprint.md - Blueprint for a NASDAQ Stock Tracker Program

## 1. Overview

This document presents a structured blueprint for a menu-driven NASDAQ stock tracker implemented with arrays. The proposed design satisfies the core lab expectation of using arrays and loops to collect, store, process, and display user-entered data. It also incorporates the extra credit requirement by including search-based edit and delete operations.

The system models a simplified stock portfolio in which each stock record contains identifying and financial attributes. The program accepts multiple entries, stores them in arrays, computes value and portfolio share, and allows records to be added, modified, or removed through a menu-driven search process.

---

## 2. Program Objective

The objective of the program is to construct an array-based stock tracking system capable of the following:

- storing multiple NASDAQ stock records
- accepting user input until the user enters `done` after at least four rows
- displaying all stored records in a structured format
- computing value and portfolio percentage from existing numeric fields
- supporting search, add, edit, and delete functionality
- validating that quantity and purchase price are not negative
- validating that stock symbols contain letters only and are no more than five characters
- requiring at least four stock rows during startup and preventing deletion below four rows

This design reflects a realistic data-processing scenario and demonstrates practical use of arrays in a business-oriented application.

---

## 3. Data Fields

Each stock record should contain the following attributes:

- **Stock Symbol**
- **Quantity**
- **Purchase Price**
- **Value**
- **Portfolio Percentage**

### Derived Field

The **Value** field should not be entered directly by the user. Instead, it should be calculated using the formula:

```text
Value = Quantity × Purchase Price
```

The **Portfolio Percentage** field should also be derived during display using the formula:

```text
Portfolio Percentage = (Value / Total Portfolio Value) × 100
```

These derived values satisfy the requirement that output be computed from previously stored data.

---

## 4. Data Structure Design

The most suitable design for this assignment is a set of **parallel one-dimensional arrays**. In this structure, each array stores one category of information, and the same index across all arrays represents one stock record.

### Proposed Arrays

```text
symbols[]
quantities[]
purchasePrices[]
```

A separate `values[]` or `percentages[]` array is optional. However, computing both during display is preferable because it avoids redundant storage and ensures consistency after edits.

### Design Principle

- Index `0` in all arrays refers to the first stock
- Index `1` in all arrays refers to the second stock
- and so forth

Thus, all arrays must remain synchronized at all times.

---

## 5. Algorithm Design

### 5.1 Overall Control Algorithm

The overall system may be structured around the following high-level process:

```text
1. Initialize arrays and control variables
2. Repeatedly collect stock data until the user enters `done` after at least four rows
3. Repeatedly show the current stock table and a menu for add, edit, delete, or exit
4. Search for a stock when edit or delete is selected
5. Perform the requested operation if the stock is found
6. Continue until the user chooses to exit
```

---

### 5.2 Input Algorithm

The input phase uses a sentinel-controlled loop.

```text
Set count = 0

Repeat
    Prompt for stock symbol
    If stock symbol = `done` and count >= 4
        Exit loop
    If stock symbol = `done` and count < 4
        Display minimum-row message
        Continue loop
    If stock symbol = `cancel`
        Cancel the current row
        Continue loop

    Validate symbol contains only letters
    Validate symbol length <= 5

    Prompt for quantity
    Prompt for purchase price

    Validate that quantity >= 0
    Validate that purchase price >= 0

    If quantity or purchase price input = `cancel`
        Cancel the current row
        Continue loop

    Store each value in its corresponding array at index count
    Increment count
Until finished
```

#### Purpose of This Algorithm

- initializes array contents from user input
- allows an unknown number of entries up to array capacity
- demonstrates loop-controlled data entry
- applies simple validation rules to maintain realistic stock data
- allows a row to be cancelled before anything is saved
- enforces a minimum of four rows before initial entry can end
- lets the user abandon a partially entered row with `cancel`

---

### 5.3 Display Algorithm

The display phase processes all stored records using a loop.

```text
For index from 0 to count - 1
    Compute value = quantities[index] * purchasePrices[index]
    Compute percentage = value / total portfolio value × 100
    Display symbol, quantity, purchase price with `$`, value with `$`, and percentage
End For
```

#### Algorithm Purpose

- traverses all populated array positions
- computes derived financial values
- produces structured, readable output
- keeps currency fields recognizable by displaying them with a dollar sign
- sizes columns dynamically based on the data being displayed

---

### 5.4 Search Algorithm

The extra credit operations should begin with a search. The stock symbol is the most appropriate search key because it is concise and typically unique.

```text
Prompt for stock symbol to search
If search input = `cancel`
    Return to menu
Validate symbol contains only letters
Validate symbol length <= 5
Set foundIndex = -1

For index from 0 to count - 1
    If symbols[index] matches search symbol
        Set foundIndex = index
        Stop loop
End For

If foundIndex = -1
    Display "Stock not found"
Else
    Continue to edit or delete
```

#### Purpose of Algorithm

- identifies the position of a specific stock record
- provides the index needed for later modification
- supports both edit and delete operations
- enforces the same symbol rules used during data entry

---

### 5.5 Edit Algorithm

If the stock is found, the program should allow one or more fields to be updated.

```text
If foundIndex is not -1
    Repeat
        Display edit options
        Prompt for field to modify

        If choice = symbol
            Update symbols[foundIndex]
            Allow `cancel` to abandon the symbol update
        Else if choice = quantity
            Update quantities[foundIndex]
            Validate quantity >= 0
        Else if choice = purchase price
            Update purchasePrices[foundIndex]
            Validate purchase price >= 0
        Else if choice = return
            Exit edit loop
        Else
            Display invalid choice message
    Until user chooses return
End If
```

#### Purpose of The Algorithm

- modifies an existing stock record
- allows one or more selected fields to be updated in the same edit session
- preserves array alignment by changing data at a single shared index

Because value and portfolio percentage are derived, they update automatically when the record is displayed again.

---

### 5.6 Delete Algorithm

Deletion should remove the located record from all arrays. Since arrays are fixed in size, deletion must be simulated by shifting later values one position to the left.

```text
If foundIndex is not -1
    If count <= 4
        Display minimum-row message
        Return to menu

    For index from foundIndex to count - 2
        symbols[index] = symbols[index + 1]
        quantities[index] = quantities[index + 1]
        purchasePrices[index] = purchasePrices[index + 1]
    End For

    Decrement count
End If
```

#### Purpose for This Algorithm

- removes a stock logically from the dataset
- preserves data synchronization across parallel arrays
- reduces the logical size of the stored collection
- prevents the portfolio from dropping below four stocks

---

### 5.7 Menu Algorithm

A repeated menu loop is an appropriate design for the main program flow.

```text
Repeat
    Display the current table
    Display menu
    Prompt for user choice

    If choice = add
        Collect and validate one new stock record
    Else if choice = edit
        Search for stock
        If found, edit record
    Else if choice = delete
        Search for stock
        If found, delete record
    Else if choice = exit
        End program
    Else
        Display invalid choice message
Until user exits
```

#### Reason for This Algorithm

- organizes program behavior into manageable user actions
- supports repeated interaction
- integrates both the base requirements and extra credit features naturally
- keeps the current portfolio visible during menu navigation

---

## 6. Variable Design

A reasonable variable set for this blueprint includes:

- `MAX_SIZE` — maximum number of stocks
- `MIN_INITIAL_ROWS` — minimum number of stocks required before initial exit
- `MAX_SYMBOL_LENGTH` — maximum allowed stock symbol length
- `DONE_COMMAND` — keyword that ends startup entry when minimum rows are met
- `CANCEL_COMMAND` — keyword that abandons the current row or search
- `EXIT_COMMAND` — keyword that ends the menu loop
- `symbols[]` — stock symbols
- `quantities[]` — share quantities
- `purchasePrices[]` — stock purchase prices
- `count` — number of active stock records
- `searchSymbol` — symbol entered for lookup
- `foundIndex` — result of search
- `choice` — menu selection
- `editChoice` — edit submenu selection

### Variable Role Summary

| Variable | Purpose |
| --- | --- |
| `MAX_SIZE` | Defines storage capacity |
| `MIN_INITIAL_ROWS` | Defines minimum startup entries |
| `MAX_SYMBOL_LENGTH` | Limits ticker symbol length |
| `DONE_COMMAND` | Stops startup entry when allowed |
| `CANCEL_COMMAND` | Cancels the current input flow |
| `EXIT_COMMAND` | Ends the program from the menu |
| `count` | Tracks logical number of stored records |
| `foundIndex` | Stores search result location |
| `choice` | Controls main menu flow |
| `editChoice` | Controls edit menu flow |

---

## 7. Program Mapping

### 7.1 Mapping of Requirements to Design

| Lab Requirement | Program Feature |
| --- | --- |
| Real-world scenario | NASDAQ stock portfolio tracker |
| User-entered data | Symbol, quantity, purchase price |
| Array storage | Parallel one-dimensional arrays |
| Loop for input | `done`/`cancel` controlled data entry loop |
| Loop for output | Traversal loop for displaying records |
| Computed values | Value and portfolio percentage |
| Structured output | Table-like stock report |
| Data realism | Symbol, quantity, and price validation |
| Extra credit search | Symbol-based lookup |
| Extra credit edit | Field update using found index |
| Extra credit delete | Left-shift deletion algorithm with 4-row floor |

---

### 7.2 Mapping of Data Fields to Arrays

| Data Field | Storage Method | Type |
| --- | --- | --- |
| Stock Symbol | `symbols[]` | String |
| Quantity | `quantities[]` | Integer |
| Purchase Price | `purchasePrices[]` | Double/Float |
| Value | Computed from arrays | Double/Float |
| Portfolio Percentage | Computed from arrays | Double/Float |

---

### 7.3 Mapping of Operations to Algorithms

| Program Operation | Algorithm Used |
| --- | --- |
| Add stock at startup | Sentinel-controlled input algorithm |
| Add stock from menu | Menu-based add operation with validation |
| Display stocks | Sequential traversal algorithm |
| Compute value/percentage | Formula-based calculation in display loop |
| Search stock | Linear search |
| Edit stock | Search + indexed update |
| Delete stock | Search + shift-left deletion |

---

## 8. Output Design

The output should be formatted in a readable, table-like structure. A conceptually appropriate layout is shown below:

```text
Symbol   Quantity   Purchase Price        Value         %
AAPL     10         $182.50               $1825.00   21.79%
MSFT     5          $410.20               $2051.00   24.46%
NVDA     8          $920.75               $7366.00   53.75%
```

The output can also include a total portfolio value:

```text
Total Portfolio Value: $11242.00
```

This strengthens the overall meaningfulness of the output and summarizes the full portfolio.

---

## 9. Development Sequence

A disciplined implementation order would be:

1. declare arrays and constants
2. create the `done` / `cancel` controlled input loop
3. implement the display loop with dynamic column sizing
4. add value and portfolio percentage computation
5. implement the search process
6. implement the edit operation
7. implement the delete operation with the four-row minimum rule
8. add the menu loop and menu-based add option
9. add validation for symbol, quantity, and purchase price
10. refine formatting, naming, and comments

This sequence reduces complexity by building the program incrementally.

---

## 10. Edge Cases and Design Considerations

The blueprint should account for the following cases:

- fewer than four stocks entered before `done`
- user cancels a partially entered row
- array capacity reached
- duplicate stock symbol entered
- invalid stock symbol entered during add, edit, or search
- negative quantity entered
- negative purchase price entered
- stock symbol not found during search
- invalid menu choice
- attempted deletion when only four stocks remain
- user chooses to return from the edit menu without changes
- edits to price or quantity requiring value and percentage recalculation

These considerations improve program robustness and clarity.

---

## 11. Conceptual Summary

The central principle of the design is that **each index represents one complete stock record**. The arrays operate together as a unified table, where each column is stored separately but each row is identified by a shared index.

Accordingly:

- searching identifies the correct index
- editing changes values at that index
- deleting removes that index from every array
- display logic processes all populated indices

This makes the NASDAQ stock tracker an effective and academically appropriate example of array-based data management.

---

## 12. Concise Design Statement

This program may be defined as a parallel-array stock tracking system in which user-entered NASDAQ stock data is stored by index, processed through loop-based traversal, and managed through search-driven editing and deletion, with value and portfolio percentage computed dynamically from quantity and purchase price.
