def arithmetic_arranger(problems, show_answers=False):
    final = {
        'fline': '',
        'sline': '',
        'tline': '',
        'foline': ''
    }
    
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    for i in problems:
        fnum, oper, snum = i.split()

        if not fnum.isdigit() or not snum.isdigit():
            return 'Error: Numbers must only contain digits.'

        if oper not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        
        if len(fnum) > 4 or len(snum) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        width = max(len(fnum), len(snum)) + 2
        final['fline'] += fnum.rjust(width) + '    '
        final['sline'] += oper + snum.rjust(width - 1) + '    '
        final['tline'] += '-' * width + '    '
        
        if show_answers:
            if oper == '+':
                result = str(int(fnum) + int(snum))
            else:
                result = str(int(fnum) - int(snum))
            final['foline'] += result.rjust(width) + '    '

    # Removing extra spaces at the end
    arranged_problems = f"{final['fline'].rstrip()}\n{final['sline'].rstrip()}\n{final['tline'].rstrip()}"
    if show_answers:
        arranged_problems += f"\n{final['foline'].rstrip()}"
    
    return arranged_problems

# Example usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
