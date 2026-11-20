import curses

def main(stdscr):
    curses.curs_set(0)

    options = ["Storage", "Folder Size", "Task Manager",
               "Time & Date", "Screentime", "Exit"]

    selected = 0

    while True:
        stdscr.clear()

        stdscr.addstr(0, 2, "SULAKA - System Management")

        for index, option in enumerate(options):
            if index == selected:
                stdscr.addstr(index + 2, 2, f"> {option}", curses.A_REVERSE)
            else:
                stdscr.addstr(index + 2, 2, f"  {option}")

        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected = (selected - 1) % len(options)

        elif key == curses.KEY_DOWN:
            selected = (selected + 1) % len(options)

        elif key in [10, 13, curses.KEY_ENTER]:
            if options[selected] == "Exit":
                break

            stdscr.addstr(len(options) + 3, 2,
                          f"You selected: {options[selected]}")
            stdscr.refresh()
            stdscr.getch()

        elif key == ord('q'):
            break


curses.wrapper(main)