def maurice_wins(m_snails, s_snails):
	Outcomes = [(m_snails[0],s_snails[2]),(m_snails[1],s_snails[0]),(m_snails[2],s_snails[1])]
	return True if len([x for x in Outcomes if x[0] > x[1]]) >= 2 else False

print(maurice_wins([6, 8, 9], [7, 12, 14]))
'''
List 1: [s, m, f] for Maurice.
List 2: [s, m, f] for Steve.

maurice_wins([3, 5, 10], [4, 7, 11]) ➞ True
# Since the matches are (3, 11), (5, 4) and (10, 7), Maurice wins 2 out of 3.
Round 1: [s, f] Sacrifice his slowest snail against Steve's fastest.
Round 2: [m, s] Use his middle snail against Steve's slowest.
Round 3: [f, m] Use his fastest snail against Steve's middle.
'''