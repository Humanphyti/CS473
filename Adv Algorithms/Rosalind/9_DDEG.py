import os
os.chdir('D:\\Desktop')
f = open('rosalind_ddeg.txt')

with open('rosalind_ddeg.txt') as input_data:
        count_vertices={}
        total_number_of_vertices=map(int, input_data.readline().strip().split())[0]
        for line in input_data:
            vertex_pair=[int(i) for i in line.strip().split()]
            if count_vertices.get(vertex_pair[0])==None:
                count_vertices[vertex_pair[0]]=[vertex_pair[1]]
            else:
                count_vertices[vertex_pair[0]]+=[vertex_pair[1]]
            if count_vertices.get(vertex_pair[1])==None:
                count_vertices[vertex_pair[1]]=[vertex_pair[0]]
            else:
                count_vertices[vertex_pair[1]]+=[vertex_pair[0]]

        for vertex in xrange(1,total_number_of_vertices+1):
            total_sum=0
            if count_vertices.get(vertex)==None:
                print total_sum,
                continue
            for neighbor in count_vertices[vertex]:
                total_sum+=len(count_vertices[neighbor])
            print total_sum,
