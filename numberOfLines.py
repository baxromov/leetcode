def numberOfLines(widths, S):
    if not S: return 0, 0
    lines, cur_line_width = 1, 0

    for c in S:
        width = widths[ord(c) - ord('a')]
        if cur_line_width + width > 100:
            lines += 1
            cur_line_width = width
        else:
            cur_line_width += width

    return lines, cur_line_width