#!/bin/bash

# ======== Controls ========
start_or_pause_key="F1"
exit_key="Esc"
default_delay=1  # seconds

# ==== Global variables ====
pause=true
running=false
delay=$default_delay

function display_controls {
  echo "F1 = Start / Pause"
  echo "Esc = Exit"
}

function choose_delay {
  read -p "Enter wanted delay (seconds): " input_delay
  if [[ $input_delay =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
    delay=$input_delay
  else
    echo "Invalid input. Using default delay: $default_delay seconds"
    delay=$default_delay
  fi
}

function key_press {
  if [[ $1 == $start_or_pause_key ]]; then
    pause=!$pause
    echo "< Pause >" || echo "< Start >"
    [[ $pause == "false" ]] && click_periodically
  elif [[ $1 == $exit_key ]]; then
    running=false
    echo "< Exit >"
    exit
  fi
}

function click_periodically {
  while [[ $running == "true" && $pause == "false" ]]; do
    xdotool click 1
    sleep $delay
  done
}

function main {
  choose_delay
  echo "Delay = $delay seconds"
  display_controls

  while [[ $running == "true" ]]; do
    read -rsn1 key
    key_press $key
  done
}

main
