# This file contains some aliases and functions that are useful for Advent of Code.
# Using the setup.sh file, it will be added to your shell's config file (considering you are using zsh).

# MAKE SURE TO SET THESE ENVIRONMENT VARIABLES
export AOC_SESSION="<session cookie>"
export AOC_DIR="<path to the repository>"

function aoc() {
    if [ $1 = "get" ]; then
        aoc_get_data $2 $3
    fi
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
