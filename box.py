def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'{" " * 31}╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'{" " * 31}║{space}{title:<{width}}{space}║\n'  # title
        box += f'{" " * 31}║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'{" " * 31}║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'{" " * 31}╚{"═" * (width + indent * 2)}╝'  # lower_border
    return print(box)
