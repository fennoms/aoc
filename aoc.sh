# This file contains some aliases and functions that are useful for Advent of Code.
# Using the setup.sh file, it will be added to your shell's config file (considering you are using zsh).

# MAKE SURE TO SET THESE ENVIRONMENT VARIABLES
export AOC_SESSION="<session cookie>"
export AOC_DIR="<path to the repository>"

function aoc() {
    if [ $1 = "get" ]; then
        aoc_get_data $2 $3
    fi
    if [ $1 = "run" ]; then
        aoc_run_solution $2
    fi
    if [ $1 = "day" ]; then
        aoc_get_day
    fi
}

# Simply print the current year and day.
function aoc_get_day() {
    year=$(date +"%Y")
    day=$(date +"%d")
    echo "year: $year, day: $day"
}

# Run the solution for the current day, so run part_1.py and part_2.py.
# Print part 1 in red, part 2 in green. If $2 is either 1 or 2 it will only
# run that part.
function aoc_run_solution() {
    if [ -z $1 ]; then
        part=0
    else
        part=$1
    fi

    if [ $part -eq 1 ]; then
        echo "Solution for part 1:"
        output=$(python3 $AOC_DIR/part_1.py)
        echo "\033[0;31m$output\033[0m" # Red
        return 0
    fi

    if [ $part -eq 2 ]; then
        echo "Solution for part 2:"
        output=$(python3 $AOC_DIR/part_2.py)
        echo "\033[0;32m$output\033[0m" # Green
        return 0
    fi

    # Print the solution for part 1
    echo "Solution for part 1:"
    output=$(python3 $AOC_DIR/part_1.py)
    echo "\033[0;31m$output\033[0m" # Red

    # Print the solution for part 2
    echo "Solution for part 2:"
    python3 $AOC_DIR/part_2.py
    echo "\032[0;31m$output\033[0m" # Green
}

# Get the data for a specfic year and day. If $1 and $2 are not set, it will default to the current year and day.
# If the current day is then not in December the function will return an error.
# $1: year
# $2: day
function aoc_get_data() {
    if [ -z $1 ] && [ -z $2 ]; then
        year=$(date +"%Y")
        day=$(date +"%d")
        month=$(date +"%m")

        if [ $month -ne 12 ]; then
            echo "It is currently not December. You can only retrieve data from previous years."
            return 1
        fi
    else
        year=$1
        day=$2
    fi

    if [ $day -lt 1 ] || [ $day -gt 25 ]; then
        echo "Invalid day. The day must be between 1 and 25."
        return 1
    fi

    if [ $year -lt 2015 ] || [ $year -gt $(date +"%Y") ]; then
        echo "Invalid year. The year must be between 2015 and the current year."
        return 1
    fi

    # if the day starts with a 0 we have to remove it
    if [ ${day:0:1} = "0" ]; then
        day=${day:1}
    fi

    input=$(curl --cookie "session=$AOC_SESSION" https://adventofcode.com/$year/day/$day/input)

    if [ $input = "Puzzle inputs differ by user.  Please log in to get your puzzle input." ]; then
        echo "Failed getting puzzle input. Ensure your cookie is correct".
        return 1
    fi
    
    echo $input > $AOC_DIR/input.txt
    echo "Data for day $day of year $year has been saved to $AOC_DIR/input.txt."

    # Create new files for the solution, part_1.py and part_2.py
    rm -f $AOC_DIR/part_1.py
    rm -f $AOC_DIR/part_2.py
    touch $AOC_DIR/part_1.py
    touch $AOC_DIR/part_2.py
}
