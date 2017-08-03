import sys

if len(sys.argv) < 2:
    print('Missing filename argument')
    sys.exit()

def set_edge(f, node1, node2, type):
    if type == 'arrow_none':
        f.write(node2 + ' activates ' + node1 + '\n')
    elif type == 'none_arrow':
        f.write(node1 + ' activates ' + node2 + '\n')
    elif type == 'inhib_none':
        f.write(node2 + ' inhibits ' + node1 + '\n')
    elif type == 'none_inhib':
        f.write(node1 + ' inhibits ' + node2 + '\n')
    elif type == 'arrow_inhib':
        f.write(node2 + ' activates_inhibits ' + node1 + '\n')
    elif type == 'inhib_arrow':
        f.write(node1 + ' activates_inhibits ' + node2 + '\n')
    elif type == 'inhib_inhib':
        f.write(node2 + ' double_inhibits ' + node1 + '\n')
    elif type == 'arrow_arrow':
        f.write(node2 + ' double_activates ' + node1 + '\n')
    elif type == 'arrow_loop':
        f.write(node1 + ' self_activates ' + node2 + '\n')
    elif type == 'inhib_loop':
        f.write(node1 + ' self_inhibits ' + node2 + '\n')

num = 0;

f = open(sys.argv[1],'w')

for first_loop in ['none', 'arrow_loop', 'inhib_loop']:
    for second_loop in ['none', 'arrow_loop', 'inhib_loop']:
        for third_loop in ['none', 'arrow_loop', 'inhib_loop']:
            for first_edge in ['none', 'arrow_none', 'none_arrow', 'inhib_none', 'none_inhib', 'arrow_inhib', 'inhib_arrow', 'arrow_arrow', 'inhib_inhib']:
                for second_edge in ['none', 'arrow_none', 'none_arrow', 'inhib_none', 'none_inhib', 'arrow_inhib', 'inhib_arrow', 'arrow_arrow', 'inhib_inhib']:
                    for third_edge in ['none', 'arrow_none', 'none_arrow', 'inhib_none', 'none_inhib', 'arrow_inhib', 'inhib_arrow', 'arrow_arrow', 'inhib_inhib']:
                        first = 'n' + str(num).zfill(5)
                        second = 'n' + str(num+1).zfill(5)
                        third = 'n' + str(num+2).zfill(5)
                        set_edge(f, first, first, first_loop)
                        set_edge(f, second, second, second_loop)
                        set_edge(f, third, third, third_loop)
                        set_edge(f, first, second, first_edge)
                        set_edge(f, second, third, second_edge)
                        set_edge(f, third, first, third_edge)
                        num += 3

f.close()
